# Generated by Django 4.0.1 on 2022-02-13 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_id_estabelecimento_agendamento_estabelecimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='estabelecimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estabelecimento', verbose_name='ID do Estabelecimento'),
        ),
        migrations.AlterField(
            model_name='agendamento_cidadao',
            name='agendamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.agendamento', verbose_name='ID do Agendamento'),
        ),
        migrations.AlterField(
            model_name='agendamento_cidadao',
            name='cidadao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ID do Cidadão'),
        ),
    ]