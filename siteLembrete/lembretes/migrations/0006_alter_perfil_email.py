# Generated by Django 4.0.1 on 2022-02-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lembretes', '0005_lembrete_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]