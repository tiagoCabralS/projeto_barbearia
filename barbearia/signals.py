from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from .models import Perfil


@receiver(user_signed_up)
def criar_perfil_apos_cadastro_social(request, user, sociallogin=None, **kwargs):
    if sociallogin is None:
        return

    dados_google = {}
    dados_google = sociallogin.account.extra_data

    telefone = dados_google.get('phone_number', dados_google.get('phone', ''))
    Perfil.objects.get_or_create(
        usuario=user,
        defaults={'telefone': telefone[:20]},
    )
    request.session['telefone_pendente'] = True
    request.session.modified = True