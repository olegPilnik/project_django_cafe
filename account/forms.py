from django import forms
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={}))

    def clean(self):
        username = self.cleaned_data['username'].strip()
        password = self.cleaned_data['password'].strip()

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                return forms.ValidationError('Username or password wrong')
        return super().clean()


class RegistrationUserForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] == data['password2']:
            return data['password2']

        return forms.ValidationError('Passwords must be equals')

    class Meta:
        model = User
        fields = ('username', )
