from django.db import models

from django.db import models

class Kit(models.Model):
    identificacao = models.CharField(max_length=255, unique=True)
    codigo = models.AutoField(primary_key=True)
    preco = models.IntegerField()

class Modulo(models.Model):
    kit_module_id = models.AutoField(primary_key=True)
    conexao = models.CharField(max_length=255, unique=True)
    quantidade = models.IntegerField()
    modelo = models.CharField(max_length=255, unique=True)
    potencia = models.IntegerField(unique=True)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)

class Inversor(models.Model):
    kit_inversor_id = models.AutoField(primary_key=True)
    quantidade = models.IntegerField()
    tipo = models.CharField(max_length=255, unique=True)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)

class Cabo(models.Model):
    kit_cabo_id = models.AutoField(primary_key=True)
    modelo_vermelho = models.IntegerField()
    modelo_preto = models.CharField(max_length=255, unique=True)
    quantidade_vermelho = models.IntegerField()
    quantidade_preto = models.IntegerField(unique=True)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)

class Estrutura(models.Model):
    kit_estrutura_id = models.AutoField(primary_key=True)
    mod_estrutura_1 = models.IntegerField(unique=True)
    mod_estrutura_2 = models.CharField(max_length=255, unique=True)
    mod_estrutura_3 = models.CharField(max_length=255, unique=True)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)