# Generated by Django 4.0.1 on 2022-02-08 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lembretes', '0012_alter_lembrete_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lembrete',
            name='descricao',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
