from django import forms
from .models import Profile




class ProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields= ['Avatar','bio','link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio':forms.Textarea(attrs={'class': 'form-control mt-3','rows':3, 'placeholder':'Biografia'}),
            'link':forms.URLInput(attrs={'class': '"form-control mt-3','rows':3, 'placeholder':'Enlace'})
        }


