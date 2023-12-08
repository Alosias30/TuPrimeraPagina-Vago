from django import forms

class ViajeroFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class DestinoFormulario(forms.Form):   
    nombre = forms.CharField(max_length=30)
    pais = forms.CharField(max_length=30)

class EstablecimientoFormulario(forms.Form):
    nombre = forms.CharField()
    rubro = forms.CharField()
    calificacion = forms.IntegerField()

