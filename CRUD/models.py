from django.db import models


class Credenciales(models.Model):
    id_credencial = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE, db_column='id_usuario')
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'credenciales'


class DetalleOrden(models.Model):
    id_detalle_orden = models.BigAutoField(primary_key=True)
    id_orden = models.ForeignKey('Ordenes', on_delete=models.CASCADE, db_column='id_orden')
    id_producto = models.ForeignKey('Productos', on_delete=models.CASCADE, db_column='id_producto')
    cantidad = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'detalle_orden'


class EstadoOrden(models.Model):
    id_estado_orden = models.BigAutoField(primary_key=True)
    estado = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'estado_orden'
        ordering = ['estado']

    def save(self, *args, **kwargs):
        if self.estado:
            self.estado = self.estado.upper()
        super(EstadoOrden, self).save(*args, **kwargs)


class Ordenes(models.Model):
    id_orden = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE, db_column='id_usuario')
    id_estado_orden = models.ForeignKey(EstadoOrden, on_delete=models.CASCADE, db_column='id_estado_orden')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    total_orden = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'ordenes'


class Pago(models.Model):
    id_pago = models.BigAutoField(primary_key=True)
    id_orden = models.ForeignKey(Ordenes, on_delete=models.CASCADE, db_column='id_orden')
    metodo_pago = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'pago'

    def save(self, *args, **kwargs):
        if self.metodo_pago:
            self.metodo_pago = self.metodo_pago.upper()
        super(Pago, self).save(*args, **kwargs)



class Productos(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'productos'
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()
        super(Productos, self).save(*args, **kwargs)


class Roles(models.Model):
    id_rol = models.BigAutoField(primary_key=True)
    id_credencial = models.ForeignKey(Credenciales, on_delete=models.CASCADE, db_column='id_credencial')
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'roles'
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()
        super(Roles, self).save(*args, **kwargs)

class Stock(models.Model):
    id_stock = models.BigAutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE, db_column='id_producto')
    cantidad_disponible = models.IntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'stock'
        ordering = ['id_producto']


class Usuarios(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    numero_documento = models.CharField(max_length=15, unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    foto_perfil = models.ImageField(upload_to='foto_perfil', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'usuarios'
        ordering = ['nombres']

    def save(self, *args, **kwargs):
        if self.nombres and self.apellidos and self.direccion and self.email:
            self.nombres = self.nombres.upper()
            self.apellidos = self.apellidos.upper()
            self.direccion = self.direccion.upper()
            self.email = self.email.upper()
        super(Usuarios, self).save(*args, **kwargs)
