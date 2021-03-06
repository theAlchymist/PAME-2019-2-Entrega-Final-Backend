# Generated by Django 2.2.6 on 2019-11-01 18:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=254)),
                ('cpf', models.BigIntegerField()),
                ('admissão', models.DateTimeField(default=django.utils.timezone.now)),
                ('cargo', models.CharField(max_length=20)),
                ('salario', models.IntegerField()),
            ],
        ),
    ]
