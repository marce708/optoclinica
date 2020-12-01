from django.db import models
from uuid import uuid4;

#@ver Tutorial Youtube
class Producto(models.Model):
    
    id = models.UUIDField(primary_key=True,
                          default=uuid4,
                          editable=False,
                          verbose_name="UUID"
                          )

    LADO_OPCIONES = (
        ('izquierdo', 'izquierdo'),
        ('derecho', 'derecho')
    )
    
    DISTANCIA_OPCIONES = (
        ('lejos', 'lejos'),
        ('cerca', 'cerca')
    )

    nombre = models.CharField(max_length=100, unique=True)
    codigo_producto = models.CharField(max_length=100, blank=True, null=True)
    precio = models.DecimalField(max_digits=14, decimal_places=2, default=0.0)
    stock = models.PositiveIntegerField(blank=True, null=True, default=1) # @Modificar stock 

    armazon = models.BooleanField(default=False)
    lente = models.BooleanField(default=False)

    lado = models.CharField(
        max_length=10,
        choices=LADO_OPCIONES,
        default='izquierdo',
        blank=True,
        null=True,
        #verbose_name="Para que ojo"
    )
    distancia = models.CharField(
        max_length=5,
        choices=DISTANCIA_OPCIONES,
        default='lejos',
        blank=True,
        null=True,
        # verbose_name="Distancia"
    )

    #Define COMO se muestra una tabla dentro de la interfaz de manejo de la base de datos.
    def __str__(self):
      return f"Nombre: {self.nombre} / id: {self.id} / Codigo: {self.codigo_producto} / Precio : {self.precio}"
