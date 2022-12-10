from django import forms
from .models import Twitt

MAX_TWITT_LENGTH = 512

class TwittForm(forms.ModelForm):
    class Meta:
        model = Twitt
        fields = ['content']
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_TWITT_LENGTH:
            raise forms.ValidationError("Maximum content length exceeded.")
        return content