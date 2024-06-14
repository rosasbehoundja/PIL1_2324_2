# Chemin du fichier modèle
MODEL_PATH = os.path.join(settings.BASE_DIR, 'Youme/models/youme_cleaned_model.pkl')

# Charger le modèle
model = joblib.load(MODEL_PATH)

@login_required
def suggestion_profiles(request):
    suggested_profiles = []
    if not request.user.is_active:
        return redirect('connexion')

    current_user = request.user
    try:
        profile = Profile.objects.get(utilisateur=current_user)
        utilisateurs = Profile.objects.all()
        user_id = current_user.id
        data_u = list(utilisateurs.values('id','age', 'height','sex', 'body_type', 'education', 'orientation', 'offspring', 'smokes', 'drugs', 'diet', 'location'))
        interval = len(data_u)-user_id
        if interval != 2001:
            comp = 2001 - interval
            interval+=comp
        data = data_u[-interval:]
        df = pd.DataFrame(data)
    except Profile.DoesNotExist:
        messages.error(request, "Votre profil n'existe pas. Veuillez le créer.")
        return redirect('maj_profile')  # Rediriger vers la page de mise à jour du profil


  
    features = ['id','age', 'height','sex','body_type', 'education', 'orientation', 'offspring', 'smokes', 'drugs', 'diet', 'location']
    
    user_name = current_user.nom
    user_sex = profile.sex	
    user_orientation = profile.orientation	
    
     # Synchroniser les index avant la normalisation
    df.reset_index(drop=True, inplace=True)

    X = df[features].copy()
    
    # Convertir les colonnes en catégories et obtenir les codes numériques
    for feat in features[2:]:  # commence à partir de 'height'
        X[feat] = df[feat].astype('category').cat.codes

    scaler = StandardScaler()
    scaler.set_output(transform='pandas')
    X_scaled = scaler.fit_transform(X)

    if len(X_scaled) != len(model.labels_):
        raise ValueError(f"Mismatch between DataFrame length ({len(X_scaled)}) and model labels length ({len(model.labels_)})")
        

    df['membership'] = model.labels_
    # df.membership.value_counts()

    # Ensure that the user's index is properly identified
    user_index_list = df.index[df['id'] == user_id].tolist()
    print(user_index_list)
    print(user_id)
    # print(user_index_list)
    if not user_index_list:
        raise ValueError(f"User name {user_name} not found in the DataFrame.")
    user_index = user_index_list[0]

    id = user_id
    info = df.loc[id:id, features]
    print(info)
    if user_orientation == 'Hétérosexuel' and user_sex == 'f': 
        opposite_sex = 'm'
        users = df.loc[(df.sex == opposite_sex) & (df.orientation == 'Hétérosexuel') & (df.membership == df.at[0, 'membership'])].index
    elif user_orientation == 'Homosexuel' and user_sex == 'f':
        users = df.loc[(df.sex == user_sex) & (df.orientation == 'Homosexuel') & (df.membership == df.at[0, 'membership'])].index
    elif user_orientation == 'Hétérosexuel' and user_sex == 'm': 
        opposite_sex = 'f'
        users = df.loc[(df.sex == opposite_sex) & (df.orientation == 'Hétérosexuel') & (df.membership == df.at[0, 'membership'])].index
    elif user_orientation == 'Homosexuel' and user_sex == 'm':
        users = df.loc[(df.sex == user_sex) & (df.orientation == 'Homosexuel') & (df.membership == df.at[0, 'membership'])].index
    elif user_orientation == 'Bisexuel':
        users = df.loc[(df.membership ==df.at[0, 'membership']) & ((df.sex == user_sex) | (df.sex!= user_sex))].index
    else:
        users = df.loc[(df.membership == df.at[0, 'membership'])].index
    print(f'So we have found {len(users)} users in the same cluster.\n')

    def distance(row, user):
        result = 0
        for i, v in enumerate(row):
            result += (v - user[i])**2
        return result ** 0.5
    
    user = X_scaled.loc[user_index]
    distances = X_scaled.loc[users].apply(distance, axis=1, args=(user,)).sort_values()
    
    for y in X:
        nan_indices = df[y].isna()
        if nan_indices.any():
            if pd.api.types.is_categorical_dtype(df[y]):
            # Add 0 to the categories if it's a categorical column
                df[y] = df[y].cat.add_categories([0])
            df.loc[nan_indices, y] = 0

    gamma = 1 / (len(features))
    suggested_users = df.loc[distances.index, features]
    S = pd.DataFrame(distances.apply(lambda x: round(np.exp(-x * gamma)*100, 1)).rename('affinity'))

    suggested_profiles = Profile.objects.filter(id__in=suggested_users.id)
    return render(request, 'profile/suggestion_profiles.html', {'suggested_profiles': suggested_profiles})