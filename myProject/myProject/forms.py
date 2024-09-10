from myApp.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class signupform(UserCreationForm):
    class Meta:
        model = customuser
        fields=UserCreationForm.Meta.fields+("display_name","usertype","email",)
        
class signinform(AuthenticationForm):
    class Meta:
        model = customuser
        fields=("username","password")
        




class jobform(forms.ModelForm):
    class Meta:
        model=jobmodel
        exclude=["created_by"]
        
    
class jobapplyform(forms.ModelForm):
    class Meta:
        model = applyjob
        exclude=["applied_by","apply_to","status"]
        

class editprofileformforrecruiter(forms.ModelForm):
    class Meta:
        model = customuser
        fields=("display_name","email","company_name","company_address","company_description")
        

class editprofileformforseeker(forms.ModelForm):
    class Meta:
        model = customuser
        fields=("display_name","email","skills","education","qualifications")