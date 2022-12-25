from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    idade = models.IntegerField()
    data_de_nascimento = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    apelido = models.CharField(max_length=50, null=True)
    observacao = models.CharField(max_length=500, null=True)

    # nome, sobrenome, idade, data de nascimento e e-mail obrigatórios