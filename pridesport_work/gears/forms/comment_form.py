from django import forms

from pridesport_work.gears.models import Comment


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields= '__all__' - за да не се избират опции за предмета, като той вече е избран

class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs=
            {'class': 'form-control rounded-2',}

        )
    )