from django import forms
from .models import userdata

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = userdata
        field = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'institute', 'handle', 'codechef_handle','codeforces_handle','hackerrank', 'hackererth','spoj', 'linkedin', 'github']
        exclude = ()

    # def clean(self):
    #     cleaned_data = super(UserRegistrationForm, self).clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")
    #
    #     if password != confirm_password:
    #         raise forms.ValidationError(
    #             "password and confirm_password does not match"
    #         )