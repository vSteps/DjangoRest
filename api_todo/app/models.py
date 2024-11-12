from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length = 120)
    done = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.nome