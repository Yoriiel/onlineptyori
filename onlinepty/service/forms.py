from django import forms
from .models import Service

class PageForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['title','content','image','image1','image2','video','categoria','telefono','instagram','gps','ubicacion','distrito']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Titulo'}),
            'content': forms.Textarea(attrs={'class':'form-control ','placeholder':'Contenido'}),
            'telefono': forms.TextInput(attrs={'class':'form-control','placeholder':'telefono'}),
            'gps': forms.URLInput(attrs={'class':'form-control','placeholder':'embed de ubicacion'}),
            'instagram': forms.URLInput(attrs={'class':'form-control','placeholder':' Url de instagram'}),
            'distrito': forms.TextInput(attrs={'class':'form-control','placeholder':'distrito'}),
            
        }
  

      
