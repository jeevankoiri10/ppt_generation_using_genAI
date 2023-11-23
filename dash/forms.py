from django import forms
from .models import GenerationHistory


class GenerationForm(forms.ModelForm):
    class Meta:
        model = GenerationHistory
        fields = ('title', 'document', 'author_override', 'author')
