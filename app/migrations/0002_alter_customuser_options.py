# Generated by Django 4.0.1 on 2022-02-07 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'usuário', 'verbose_name_plural': 'usuários'},
        ),
    ]
