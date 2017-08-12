from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import SenhaReset

from core.mail import send_mail_template
from core.utils import generate_hash_key

User = get_user_model()

class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmacao nao esta correta')
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']

class EditarContaForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email']

class SenhaResetForm(forms.Form):

    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError(
            'Nenhum usuario encontrado com este e-mail'
        )

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = SenhaReset(key=key, user=user)
        reset.save()
        template_name = 'conta/password_reset_mail.html'
        subject = 'Criar nova senha no MammonTrading'
        context = {
            'reset': reset,
        }
        send_mail_template(subject, template_name, context, [user.email])