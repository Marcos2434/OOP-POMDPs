from django import forms
from enum import Enum
from django.core.exceptions import ValidationError

OOP_MODEL_CHOICES = (
    ("Line", "Line"),
    ("Grid", "Grid"),
    ("Maze", "Maze"),
)

def validate_odd(value): 
    if value % 2 == 0: raise ValidationError('%(value)s has to be an odd number!', params={'value': value})

class OOP_Form(forms.Form):
    model = forms.ChoiceField(choices=OOP_MODEL_CHOICES)
    size = forms.IntegerField(min_value=1, step_size=1)
    target = forms.IntegerField(min_value=0, step_size=1) # (goal)
    budget = forms.IntegerField(min_value=1, step_size=1)
    threshold = forms.DecimalField(min_value=1, step_size=.05)
    deterministic = forms.BooleanField(required=False)
    sensor_selection = forms.BooleanField(required=False)
    
    rows = forms.IntegerField(min_value=1, step_size=1)
    columns = forms.IntegerField(min_value=1, step_size=1, validators=[validate_odd])
    observables = forms.CharField(label='Observables', required=False)
    # Another possibility:
    # observables = forms.CharField(label='Observables', required=False, widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))

    def get_clean_observables(self):
        data = self.cleaned_data['observables']
        observables_list = [tuple(map(int, pair.strip().split())) for pair in data.split('|')]
        return observables_list
    
    def __init__(self, *args, **kwargs):
        initial_values = kwargs.pop('initial', {})
        super().__init__(*args, **kwargs)
        
        # self.initial['observables'] = initial_values.get('observables', '0 0 | 1 1 | 3 3 | 4 4 | 5 5 | 6 6 | 7 7 | 8 8 | 9 9 | 10 10 | 11 11 | 12 12 | 13 13 | 14 14 | 15 15 | 16 16 | 17 17 | 18 18 | 19 19 | 20 20 | 21 21 | 22 22 | 23 23 | 24 24 | 25 25 | 26 26 | 27 27 | 28 28 | 29 29 | 30 30 | 31 31 | 32 32 | 33 33 | 34 34 | 35 35 | 36 36 | 37 37 | 38 38 | 39 39 | 40 40 | 41 41 | 42 42 | 43 43 | 44 44 | 45 45 | 46 46 | 47 47 | 48 48 | 49 49 | 50 50 | 51 51 | 52 52 | 53 53 | 54 54 | 55 55 | 56 56 | 57 57 | 58 58 | 59 59 | 60 60 | 61 61 | 62 62 | 63 63 | 64 64 | 65 65 | 66 66 | 67 67 | 68 68 | 69 69 | 70 70 | 71 71 | 72 72 | 73 73 | 74 74 | 75 75 | 76 76 | 77 77 | 78 78 | 79 79 | 80 80 | 81 81 | 82 82 | 83 83 | 84 84 | 85 85 | 86 86 | 87 87 | 88 88 | 89 89 | 90 90 | 91 91 | 92 92 | 93 93 | 94 94 | 95 95 | 96 96 | 97 97 | 98 98 | 99 99')
        
        # # non deterministic
        # self.initial['model'] = initial_values.get('model', 'Line')
        # self.initial['size'] = initial_values.get('size', 5)
        # self.initial['target'] = initial_values.get('target', 2)
        # self.initial['budget'] = initial_values.get('budget', 1)
        # self.initial['threshold'] = initial_values.get('threshold', 10)
        # self.initial['deterministic'] = initial_values.get('deterministic', False)
        # self.initial['rows'] = initial_values.get('row', 5)
        # self.initial['columns'] = initial_values.get('column', 5)
        # self.initial['sensor_selection'] = initial_values.get('sensor_selection', False)
        
        
        
        # self.initial['model'] = initial_values.get('model', 'Line')
        # self.initial['size'] = initial_values.get('size', 5)
        # self.initial['target'] = initial_values.get('target', 2)
        # self.initial['budget'] = initial_values.get('budget', 2)
        # self.initial['threshold'] = initial_values.get('threshold', 1.5)
        # self.initial['deterministic'] = initial_values.get('deterministic', True)
        # self.initial['rows'] = initial_values.get('row', 5)
        # self.initial['columns'] = initial_values.get('column', 5)
        # self.initial['sensor_selection'] = initial_values.get('sensor_selection', False)
        
        # self.initial['sensor_selection'] = initial_values.get('sensor_selection', True)
        # self.initial['observables'] = initial_values.get('observables', '0 0 | 1 1 | 3 3 | 4 4')
        
        # non deterministic
        # self.initial['model'] = initial_values.get('model', 'Grid')
        # self.initial['size'] = initial_values.get('size', 3)
        # self.initial['target'] = initial_values.get('target', 4)
        # self.initial['budget'] = initial_values.get('budget', 4)
        # self.initial['threshold'] = initial_values.get('threshold', 1.5)
        # self.initial['deterministic'] = initial_values.get('deterministic', False)
        # self.initial['rows'] = initial_values.get('row', 5)
        # self.initial['columns'] = initial_values.get('column', 5)
        # self.initial['sensor_selection'] = initial_values.get('sensor_selection', False)
        
        # self.initial['model'] = initial_values.get('model', 'Grid')
        # self.initial['size'] = initial_values.get('size', 3)
        # self.initial['target'] = initial_values.get('target', 8)
        # self.initial['budget'] = initial_values.get('budget', 2)
        # self.initial['threshold'] = initial_values.get('threshold', 2.25)
        # self.initial['deterministic'] = initial_values.get('deterministic', True)
        # self.initial['rows'] = initial_values.get('row', 5)
        # self.initial['columns'] = initial_values.get('column', 5)
        # self.initial['sensor_selection'] = initial_values.get('sensor_selection', False)
        
        
        # self.initial['sensor_selection'] = initial_values.get('sensor_selection', True)
        # self.initial['observables'] = initial_values.get('observables', '0 0 | 1 1 | 2 2 | 3 3 | 4 4 | 5 5 | 6 6 | 7 7 | 8 8')
        
        
        # self.initial['model'] = initial_values.get('model', 'Grid')
        # self.initial['size'] = initial_values.get('size', 3)
        # self.initial['target'] = initial_values.get('target', 4)
        # self.initial['budget'] = initial_values.get('budget', 4)
        # self.initial['threshold'] = initial_values.get('threshold', 1.5)
        # self.initial['deterministic'] = initial_values.get('deterministic', True)
        # self.initial['rows'] = initial_values.get('row', 5)
        # self.initial['columns'] = initial_values.get('column', 5)
        # self.initial['sensor_selection'] = initial_values.get('sensor_selection', False)
        
        self.initial['model'] = initial_values.get('model', 'Maze')
        self.initial['size'] = initial_values.get('size', 3)
        self.initial['target'] = initial_values.get('target', 9)
        self.initial['budget'] = initial_values.get('budget', 4)
        self.initial['threshold'] = initial_values.get('threshold', 3.9)
        self.initial['deterministic'] = initial_values.get('deterministic', True)
        self.initial['rows'] = initial_values.get('row', 3)
        self.initial['columns'] = initial_values.get('column', 5)
        self.initial['sensor_selection'] = initial_values.get('sensor_selection', False)