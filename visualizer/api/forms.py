from django import forms
from enum import Enum
from django.core.exceptions import ValidationError

OOP_MODEL_CHOICES = (
    ("Line", "Line"),
    ("Grid", "Grid"),
    ("Maze", "Maze"),
)

def validate_odd(value): 
    if value % 2 == 0: raise ValidationError('%(value)s is not an odd number', params={'value': value})

class OOP_Form(forms.Form):
    model = forms.ChoiceField(choices=OOP_MODEL_CHOICES)
    size = forms.IntegerField(min_value=1, max_value=1000, step_size=1)
    target = forms.IntegerField(min_value=0, max_value=1000, step_size=1) # (goal)
    budget = forms.IntegerField(min_value=1, max_value=1000, step_size=1)
    threshold = forms.DecimalField(min_value=1, max_value=1000, step_size=.05)
    deterministic = forms.BooleanField(required=False)
    
    rows = forms.IntegerField(min_value=1, max_value=1000, step_size=1)
    columns = forms.IntegerField(min_value=1, max_value=1000, step_size=1, validators=[validate_odd])
    
    def __init__(self, *args, **kwargs):
        initial_values = kwargs.pop('initial', {})
        super().__init__(*args, **kwargs)
        self.initial['size'] = initial_values.get('size', 5)
        self.initial['target'] = initial_values.get('target', 2)
        self.initial['budget'] = initial_values.get('budget', 2)
        self.initial['threshold'] = initial_values.get('threshold', 1.5)
        self.initial['deterministic'] = initial_values.get('deterministic', 1)
        self.initial['rows'] = initial_values.get('row', 5)
        self.initial['columns'] = initial_values.get('column', 5)