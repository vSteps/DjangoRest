from django.db import models #type: ignore
from django.contrib.auth.models import AbstractUser, Group, Permission, User #type: ignore


class Usuario(AbstractUser):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    PERFIL = (
        ('admin', 'Administrador'),
        ('vendedor', 'Vendedor'),
        ('cliente', 'Cliente'),
    )

    perfil = models.CharField(max_length=15, choices=PERFIL)
    
    groups = models.ManyToManyField(Group, related_name='usuario_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='usuario_permissions', blank=True)

    def __str__(self):
        return f"{self.username} - {self.email} - {self.first_name} {self.last_name} - {self.nome} - {self.telefone}"

    
    def __str__(self):
        return f"{self.username} - {self.email} - {self.first_name} {self.last_name} - {self.nome} - {self.telefone}"

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    cep = models.IntegerField()
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'perfil': 'cliente'})

    def __str__(self):
        return self.rua
    
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos_cliente')  
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    itens = models.ManyToManyField('Item')
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'perfil': 'vendedor'}, related_name='pedidos_vendedor')
    forma_pagamento = models.ForeignKey('Forma_Pagamento', on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.nome} ({self.status})"

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='produtos', blank=True)

    def __str__(self):
        return self.nome

class Forma_Pagamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome