from django.db import models #type: ignore
from django.contrib.auth.models import AbstractUser, User #type: ignore
from django.contrib.auth.models import AbstractUser, Group, Permission

class Cliente(AbstractUser):
    # Other fields for Cliente model
    
    groups = models.ManyToManyField(
        Group,
        related_name='cliente_groups',  # Add a related_name to avoid conflict
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='cliente_permissions',  # Add a related_name to avoid conflict
        blank=True
    )


class Cliente(AbstractUser): 
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)   

    groups = models.ManyToManyField(
        Group,
        related_name='cliente_groups',  # Add a related_name to avoid conflict
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='cliente_permissions',  # Add a related_name to avoid conflict
        blank=True
    )

    def __str__(self):
        return self.username, self.email, self.first_name, self.last_name, self.nome, self.telefone, self.data_cadastro   
    
class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    cep = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.rua
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    itens = models.ManyToManyField('Item')
    vendedor = models.ForeignKey('Vendedor', on_delete=models.CASCADE)
    forma_pagamento = models.ForeignKey('Forma_Pagamento', on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.cliente.nome

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='produtos', blank=True)

    def __str__(self):
        return self.nome
    
class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.nome

class Forma_Pagamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome