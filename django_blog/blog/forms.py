from django import forms
from .models import Post, Comment, Tag

class TagWidget(forms.TextInput):
    pass
class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=TagWidget()
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError("Comment can't be empty.")
        return content
    