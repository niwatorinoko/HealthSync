from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','image']
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
        self.fields['body'].label = 'Body'
        self.fields['image'].label = 'Image'

    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input mb-5'
        }
    ))

    body = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input mb-5'
        }
    ))

    image = forms.ImageField(widget=forms.FileInput(
        attrs={
            'class': 'mb-5'
        }
    ))

class CommentForm(forms.ModelForm):
    """
    コメント用フォーム
    """
    body = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input'
        }
    ))

    class Meta:
        model = Comment
        fields = ['body']