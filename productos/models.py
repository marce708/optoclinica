from django.db import models


class Producto(models.Model):

    LADO_OPCIONES = (
        ('izquierdo', 'Izquierdo'),
        ('derecho', 'Derecho')
    )
    DISTANCIA_OPCIONES = (
        ('lejos', 'Lejos'),
        ('cerca', 'Cerca')
    )

    nombre = models.CharField(max_length=100, unique=True)
    codigo_producto = models.CharField(max_length=100, blank=True, null=True)
    precio = models.DecimalField(max_digits=14, decimal_places=2, default=0.0)
    # Modificar stock (todo)
    stock = models.PositiveIntegerField(blank=True, null=True, default=1)

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

    def __str__(self):
        return f"Nombre: {self.nombre} / Codigo: {self.codigo_producto} / Precio : {self.precio}"
