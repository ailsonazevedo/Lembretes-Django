# Generated by Django 4.0.1 on 2022-02-08 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lembretes', '0014_alter_lembrete_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lembrete',
            name='concluido',
            field=models.BooleanField(default=False, verbose_name='Concluído'),
        ),
    ]
