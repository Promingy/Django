from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    title       = forms.CharField(widget=forms.TextInput({attrs={ "placeholder": "Your Title"}}))
    content     = forms.CharField(widget=forms.Textarea({attrs={
                                                        "placeholder": "Your Article"
                                                    }}))
    active      = forms.BooleanField()

    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "active"
        ]