# Generated by Django 2.2.6 on 2019-11-04 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191104_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacao',
            name='descricao',
            field=models.CharField(default='Não definida', max_length=30),
        ),
    ]
