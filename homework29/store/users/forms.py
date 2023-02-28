from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, 
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                label='Старый Пароль')
    new_password1 = forms.CharField(max_length=100, 
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                label='Новый Пароль',
                                help_text="""
                                        <li>Ваш пароль не может быть слишком похож на другую вашу личную информацию.</li>
                                        <li>Ваш пароль должен содержать не менее 8 символов.</li>
                                        <li>Ваш пароль не может быть широко используемым паролем.</li>
                                        <li>Ваш пароль не может быть полностью числовым.</li>
                                        """
                                    )
    new_password2 = forms.CharField(max_length=100, 
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                label='Подтверждение пароля')

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def clean(self):
        clean_data = super().clean()
        user = self.user
        new = clean_data.get('new_password1')
        if user.check_password(new):
            raise ValidationError('Новый пароль совпадает со старым!')
        else:
            return clean_data


class UserRegistrationForm(UserCreationForm):
    error_messages = {
        "password_mismatch": ("Пароли не совпадают."),
    }
    username = forms.CharField(max_length=100, 
                                widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
                                label='Имя',
                                help_text=(
                                    "Необходимо. 150 символов или меньше. Только буквы, цифры и @/./+/-/_."
                                        ),
                                error_messages={
                                    "unique": ("Пользователь с таким именем уже существует."),
                                            },
                                )
    password1 = forms.CharField(max_length=100, 
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                label='Пароль',
                                help_text="""
                                        <li>Ваш пароль не может быть слишком похож на другую вашу личную информацию.</li>
                                        <li>Ваш пароль должен содержать не менее 8 символов.</li>
                                        <li>Ваш пароль не может быть широко используемым паролем.</li>
                                        <li>Ваш пароль не может быть полностью числовым.</li>
                                        """
                                )
    password2 = forms.CharField(max_length=100, 
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                label='Подтверждение пароля',
                                help_text=("Введите тот же пароль, что и раньше, для проверки.")
                                )