from django import forms
from .models import RegModel
class RegForm(forms.ModelForm):
    class Meta:
        model=RegModel
        fields=['Fname','Lname','Uname','Password','Cpassword','Email','Mobno']
        widgets={'Password':forms.PasswordInput(),'Cpassword':forms.PasswordInput()}