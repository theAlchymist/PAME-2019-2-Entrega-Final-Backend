# Generated by Django 2.2.6 on 2019-11-04 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_delete_funcionario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('join_date', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=1)),
                ('data_nascimento', models.DateTimeField()),
                ('naturalidade', models.CharField(default='Rio de Janeiro - RJ', max_length=30)),
                ('nacionalidade', models.CharField(default='Brasil', max_length=20)),
                ('estado_civil', models.CharField(default='Solteiro(a)', max_length=10)),
                ('endereco', models.TextField()),
                ('telefone', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=20)),
                ('rg', models.CharField(max_length=12)),
                ('cpf', models.CharField(max_length=14)),
                ('ctps', models.CharField(max_length=12)),
                ('pis_pasep', models.CharField(max_length=14)),
                ('titulo_eleitoral', models.CharField(max_length=14)),
                ('certificado_reservista', models.CharField(max_length=12)),
                ('data_admissao', models.DateTimeField()),
                ('cargo', models.CharField(max_length=20)),
                ('turno', models.CharField(max_length=10)),
                ('salario', models.CharField(max_length=20)),
                ('ferias', models.TextField(default='Não definido')),
                ('acidentes_doencas', models.TextField(default='Não possui')),
                ('encargos_sociais', models.TextField(default='Não possui')),
                ('filiacao', models.CharField(default='Não possui', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
