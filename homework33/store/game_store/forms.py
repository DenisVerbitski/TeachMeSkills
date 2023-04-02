from .models import Comment

from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'grade')
        labels = {
            'text': 'Комментарий',
            'grade': 'Оценка Игры',
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий'}),
            'grade': forms.Select(attrs={'class': 'form-control'}),
        }