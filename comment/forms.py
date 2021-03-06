from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '4', 'cols': '50'}), required=True)

    class Meta:
        model = Comment
        fields = ('body',)
