from .models import * 
from .forms import *
import django_filters

class UserFilter(django_filters.FilterSet):
    body_type = django_filters.MultipleChoiceFilter(
        choices=Profile.BodyTypeChoices.choices,
        widget= forms.CheckboxSelectMultiple()
        )
    class Meta:
        model = Profile
        fields = {
            'age': ['lt', 'gt'],
            'sex': ['exact'],
            'orientation': ['exact'],
            # 'body_type':['exact'],
            'location' : ['istartswith'],
            'hobbies': ['istartswith'],
        }