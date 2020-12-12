from django import forms

from pridesport_work.gears.models import Gear



class GearForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Gear
        exclude = ("created_by", )

class FilterForm(forms.Form):
    ORDER_ASC = 'asc'
    ORDER_DESC = 'desc'

    ORDER_CHOICES = (
        (ORDER_ASC, 'Ascending'),
        (ORDER_DESC, 'Descending'),
    )

    text = forms.CharField(required=False,)
    order = forms.ChoiceField(
        choices=ORDER_CHOICES,
        required=False,
    )