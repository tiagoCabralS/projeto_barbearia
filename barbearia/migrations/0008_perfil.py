from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def criar_perfis_existentes(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Perfil = apps.get_model('barbearia', 'Perfil')

    Perfil.objects.bulk_create(
        [Perfil(usuario_id=user.id, telefone='') for user in User.objects.all()]
    )


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barbearia', '0007_agendamento_fim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(blank=True, max_length=20)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(criar_perfis_existentes, migrations.RunPython.noop),
    ]