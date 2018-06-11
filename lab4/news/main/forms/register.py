from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import MinimumLengthValidator
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator
from django.contrib.auth.password_validation import CommonPasswordValidator
from django.contrib.auth.password_validation import NumericPasswordValidator

from django.utils.translation import gettext as _

class RegisterForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'email_occupation' : 'Данный адрес почты уже используется',
    }

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = True

    password1 = forms.CharField(label=_("Password"),
            widget=forms.PasswordInput,
            validators=[
                        MinimumLengthValidator(min_length=8).validate,
                        UserAttributeSimilarityValidator().validate,
                        CommonPasswordValidator().validate,
                        NumericPasswordValidator().validate
                       ])

    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification.")
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                self.error_messages['email_occupation'],
                code='email_occupation',
            )
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user
