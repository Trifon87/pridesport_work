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
        fields = '__all__'
        # widgets = {
        #     'image_url': forms.TextInput(
        #         attrs={
        #             'id': 'img_input',
        #         }
        #     )
        # }