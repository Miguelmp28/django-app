from django.db import models

    
class Pasillo(models.Model):
    id_pasillo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'pasillo'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()
        super(Pasillo, self).save(*args, **kwargs)


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=70)
    nit = models.CharField(max_length=16, blank=True, null=True)
    correo = models.EmailField(max_length=70)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    conductor = models.CharField(max_length=70, blank=True, null=True)
    identificacion = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        db_table = 'proveedor'
        ordering = ['id_proveedor']

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.nombres, self.identificacion, self.correo, self.telefono)
    
    def save(self, *args, **kwargs):
        if self.nombres:
            self.nombres = self.nombres.upper()
        if self.correo:
            self.correo = self.correo.upper()
        super(Proveedor, self).save(*args, **kwargs)



class Productos(models.Model):
    id_productos = models.AutoField(primary_key=True)
    codigo = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=70)
    cantidad = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pasillo = models.ForeignKey(Pasillo, on_delete=models.CASCADE, blank=True, null=True, related_name='pasillo')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True, related_name='proveedor')
    activo = models.BooleanField(default=True, blank=True, null=True)
    fecha_ingreso = models.DateField(auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table = 'productos'
        ordering = ['id_productos']

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.nombre, self.cantidad)
    
    @property
    def total(self):
        return self.precio * self.cantidad
    
    def save(self, *args, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()
        super(Productos, self).save(*args, **kwargs)


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=70)
    identificacion = models.CharField(max_length=16)
    email = models.EmailField(max_length=70)
    celular = models.CharField(max_length=20)
    productos = models.ManyToManyField(Productos, through='UsuarioProducto', related_name='usuarios')

    class Meta:
        db_table = 'usuarios'
        ordering = ['id_usuario']

    def __str__(self):
        return self.nombres
    
    def save(self, *args, **kwargs):
        if self.nombres:
            self.nombres = self.nombres.upper()
        if self.email:
            self.email = self.email.upper()
        super(Usuarios, self).save(*args, **kwargs)


class UsuarioProducto(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_asignada = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'usuario_producto'
        unique_together = ('usuario', 'producto')

    def save(self, *args, **kwargs):
        if self.producto.cantidad is not None and self.producto.cantidad >= self.cantidad_asignada:
            self.producto.cantidad -= self.cantidad_asignada
            self.producto.save()
        super(UsuarioProducto, self).save(*args, **kwargs)




















    """
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - by ' + self.user.username
    """
    