from django import forms

from gears.models import Gear


# class GearForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         for (_, field) in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#
#     class Meta:
#         model = Gear
#         fields = '__all__'

class GearForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Gear
        fields = "__all__"
        # exclude = ('created_by', )
        # widgets = {
        #     'image_url': forms.TextInput(
        #         attrs={
        #             'id': 'img_input',
        #         }
        #     )
        # }
class FilterForm(forms.Form):
    ORDER_ASC = 'asc'
    ORDER_DESC = 'desc'

    ORDER_CHOICES = (
        (ORDER_ASC, 'Ascending'),
        (ORDER_DESC, 'Descending'),
    )

    text = forms.CharField(required=False,)
    # price = forms.IntegerField(required=False,)
    order = forms.ChoiceField(
        choices=ORDER_CHOICES,
        required=False,
    )