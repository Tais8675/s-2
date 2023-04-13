from django.contrib import admin
from .models import  app, lista, Compra, ListaCompras


admin.site.register(lista)
#admin.site.register(app)
admin.site.register(Compra)
admin.site.register(ListaCompras)
#admin.site.register(ListaComprasAdmin)

