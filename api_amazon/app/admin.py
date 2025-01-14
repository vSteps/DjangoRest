from django.contrib import admin #type: ignore
from .models import  Cliente, Endereco, Pedido, Item, Vendedor, Forma_Pagamento

# Register your models here.

admin.site.register(Cliente) #type: ignore
admin.site.register(Endereco)
admin.site.register(Pedido)
admin.site.register(Item)
admin.site.register(Vendedor)
admin.site.register(Forma_Pagamento)
