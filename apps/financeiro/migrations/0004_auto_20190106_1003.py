# Generated by Django 2.1.3 on 2019-01-06 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0003_auto_20170820_1808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lancamento',
            options={'verbose_name': 'Lançamento'},
        ),
        migrations.AlterModelOptions(
            name='planocontasgrupo',
            options={'verbose_name': 'Grupo do Plano de Contas'},
        ),
    ]