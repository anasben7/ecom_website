from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm

class UserPwChange(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'password',
            }))
    new_password1= forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'password',
            }))
    new_password2= forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'password',
            }))
    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password
    class Metal:
        model = User 
        fields = ['old_password','new_password1','new_password2']
class UserEditForm(UserChangeForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'value': 'Stage lkher',
            }))
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email goes here',
            }))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'FirstName goes here',
                
            }))
    class Meta:
        model = User
        fields = ['username','first_name','email','password']




class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'UserName goes here',
            }))
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email goes here',
            }))
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'FirstName goes here',
                
            }))
    
    password1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Pw goes here',
                'aria-describedby':"defaultRegisterFormPasswordHelpBlock",
                'type':'password',
            }))
    
    password2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Verification PW goes here',
                'aria-describedby':"defaultRegisterFormPasswordHelpBlock",
                'type':'password',
            }))
    
    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']
