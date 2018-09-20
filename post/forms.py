from django import forms

from .models import Post


class MessageForm(forms.ModelForm):
    message = forms.CharField(
        label='message',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ask message',
            }))

    class Meta:
        model = Post
        fields = ('message', )


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='comment',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'comment message',
            }))

    class Meta:
        model = Post
        fields = ('comment', )
