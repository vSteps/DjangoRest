from django.contrib import admin #type: ignore
from .models import  *

# Register your models here.

admin.site.register(Usuario) #type: ignore
admin.site.register(Endereco) #type: ignore
admin.site.register(Pedido) #type: ignore
admin.site.register(Item) #type: ignore
admin.site.register(Forma_Pagamento) #type: ignore
