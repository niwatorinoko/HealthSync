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

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Enter the title of your post',
                'id': 'title',
                'required': True
            }
        ),
        label='Title'
    )

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-input',
                'placeholder': "Write something...",
                'id': 'content',
                'rows': 5,
                'required': True
            }
        ),
        label="What's on your mind?"
    )

    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-input',
                'id': 'media',
                'accept': 'image/*',
                'onchange': 'previewImage(event)'
            }
        ),
        label='Upload Image',
        required=False
    )

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