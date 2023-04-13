from django.db import models

# Create your models here.

class Lista(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome}"

class App(models.Model):
    compra = models.CharField(max_length=64)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"ID:{self.id} Preço:{self.preco}  Produto:{self.compra}"



#class Compra(models.Model):
#    comprar = models.CharField(max_length=64)
#    valor = models.DecimalField(max_digits=10, decimal_places=2)
#    
 #   def __str__(self):
 #       return f"ID:{self.id} Preço:{self.valor}  Produto:{self.comprar}"
