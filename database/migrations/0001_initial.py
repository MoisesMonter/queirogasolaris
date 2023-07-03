# Generated by Django 4.2.3 on 2023-07-03 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('identificacao', models.CharField(max_length=255, unique=True)),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('preco', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('kit_module_id', models.AutoField(primary_key=True, serialize=False)),
                ('conexao', models.CharField(max_length=255, unique=True)),
                ('quantidade', models.IntegerField()),
                ('modelo', models.CharField(max_length=255, unique=True)),
                ('potencia', models.IntegerField(unique=True)),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.kit')),
            ],
        ),
        migrations.CreateModel(
            name='Inversor',
            fields=[
                ('kit_inversor_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
                ('tipo', models.CharField(max_length=255, unique=True)),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.kit')),
            ],
        ),
        migrations.CreateModel(
            name='Estrutura',
            fields=[
                ('kit_estrutura_id', models.AutoField(primary_key=True, serialize=False)),
                ('mod_estrutura_1', models.IntegerField(unique=True)),
                ('mod_estrutura_2', models.CharField(max_length=255, unique=True)),
                ('mod_estrutura_3', models.CharField(max_length=255, unique=True)),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.kit')),
            ],
        ),
        migrations.CreateModel(
            name='Cabo',
            fields=[
                ('kit_cabo_id', models.AutoField(primary_key=True, serialize=False)),
                ('modelo_vermelho', models.IntegerField()),
                ('modelo_preto', models.CharField(max_length=255, unique=True)),
                ('quantidade_vermelho', models.IntegerField()),
                ('quantidade_preto', models.IntegerField(unique=True)),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.kit')),
            ],
        ),
    ]
