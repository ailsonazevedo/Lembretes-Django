# Generated by Django 4.0.1 on 2022-02-08 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lembretes', '0011_rename_ativo_lembrete_concluido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lembrete',
            name='nome',
            field=models.CharField(max_length=180),
        ),
    ]
