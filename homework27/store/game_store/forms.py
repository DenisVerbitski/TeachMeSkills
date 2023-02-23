from .models import Comment, Game
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text', 'grade')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 30, 'rows':7}),
        }