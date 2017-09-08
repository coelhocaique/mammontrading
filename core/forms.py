from django import forms
from .mail import send_mail_template
from django.conf import settings

class FaleConosco(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=150)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea, max_length=512)

    def send_email(self):
        subject = '[%s] Contato' % self.nome
        context = {
            'name': self.cleaned_data['nome'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['mensagem'],
        }
        template_name = 'core/contact_email.html'
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )

        pass
