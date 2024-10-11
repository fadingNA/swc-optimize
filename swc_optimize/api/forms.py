from django import forms
from .models import Rune

class RuneSelectionForm(forms.Form):
    rune_set = forms.ChoiceField(choices=[])
    # Dynamically add fields for slots 1-6
    for slot in range(1, 7):
        locals()[f'slot_{slot}'] = forms.ChoiceField(required=False, choices=[])

    def __init__(self, *args, **kwargs):
        super(RuneSelectionForm, self).__init__(*args, **kwargs)
        rune_sets = Rune.objects.values_list('set_id', flat=True).distinct()
        rune_set_choices = [(set_id, Rune.RUNE_SET_CHOICES.get(set_id, 'Unknown')) for set_id in rune_sets]
        self.fields['rune_set'].choices = rune_set_choices

        # Initialize choices for slots as empty; they will be populated via AJAX
        for slot in range(1, 7):
            self.fields[f'slot_{slot}'].choices = []