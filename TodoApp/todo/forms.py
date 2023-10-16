from django import forms
from .models import Day, Todo


class todoForm(forms.ModelForm):
    day_id = forms.ModelChoiceField(
        queryset=Day.objects.all(),
        empty_label=None,
        label="Day",
        # to_field_name="id",
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    todo = forms.CharField(
        label="Add a todo Item",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "e.g Mow the lawn",
                "style": "font-size: 12px"
            }
        )
    )
    created = forms.TimeField(
        label="Select time",
        widget=forms.TimeInput(
            attrs={
                "type": "time",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Todo
        fields = ["todo", "created"]
