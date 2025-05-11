from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

#importar modelo de tabla
from .models import *

    

# MODULO INICIO DE SESIÓN
def inicio_sesion(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is None:
            messages.error(request, 'Usuario o contraseña incorrectos. 😕')
        else:
            login(request, user)
            return redirect('apps:index')
    return render(request, 'login/inicio_sesion.html', {
        'titulo': 'Iniciar Sesión',
        })
        

# PAGINA DE INICIO
@login_required
def index(request):
    return render(request, 'login/index.html', {
        'titulo': 'Index',
    })


# MODULO DE PROVEEDORES
@login_required
def proveedores(request):
    if request.method == 'POST':
        id_proveedor = request.POST.get('id_proveedor')
        nombres = request.POST.get('nombres')
        nit = request.POST.get('nit')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        conductor = request.POST.get('conductor')
        identificacion = request.POST.get('identificacion')
        telefono = request.POST.get('telefono')
        desactivar = request.POST.get('desactivar')

        if desactivar and id_proveedor:
            proveedor = get_object_or_404(Proveedor, id_proveedor=id_proveedor)
            proveedor.activo = 0
            proveedor.save()

        elif id_proveedor:
            proveedor = get_object_or_404(Proveedor, id_proveedor=id_proveedor)
            proveedor.nombres = nombres
            proveedor.nit = nit
            proveedor.correo = correo
            proveedor.direccion = direccion
            proveedor.conductor = conductor
            proveedor.identificacion = identificacion
            proveedor.telefono= telefono
            proveedor.save()
            messages.success(request, 'Proveedor actualizado correctamente. 🤩!')
        else:
            Proveedor.objects.create(
                nombres=nombres,
                nit=nit,
                correo=correo,
                direccion=direccion,
                conductor=conductor,
                identificacion=identificacion,
                telefono=telefono,
                activo=1
            )
            messages.success(request, 'Proveedor creado correctamente. 🎉!')
            return redirect('apps:proveedor')

    contexto = {
        'proveedor': Proveedor.objects.filter(activo=1),
        'titulo': 'Proveedores',
    }
    return render(request, 'proveedor/proveedor.html', contexto)



# MODULO DE PRODUCTOS
def productos(request):
    if request.method == 'POST':
        if request.POST.get('desactivar'):
            id_productos = request.POST.get('id_productos')
            producto = get_object_or_404(Productos, id_productos=id_productos)
            producto.activo = 0
            producto.save()
            messages.success(request, 'Producto desactivado correctamente ❌')
            return redirect('apps:productos')

        id_productos = request.POST.get('id_productos')
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombres')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('precio')
        pasillo = get_object_or_404(Pasillo, id_pasillo=request.POST.get('pasillo'))
        proveedor = get_object_or_404(Proveedor, id_proveedor=request.POST.get('proveedor'))

        if id_productos:
            producto = get_object_or_404(Productos, id_productos=id_productos)
            producto.codigo = codigo
            producto.nombre = nombre
            producto.cantidad = cantidad
            producto.precio = precio
            producto.pasillo = pasillo
            producto.proveedor = proveedor
            producto.save()
            messages.success(request, 'Producto actualizado correctamente 🤩')
        else:
            Productos.objects.create(
                codigo=codigo,
                nombre=nombre,
                pasillo=pasillo,
                precio=precio,
                cantidad=cantidad,
                proveedor=proveedor
            )
            messages.success(request, 'Producto creado correctamente 🎉')
            return redirect('apps:productos')

    contexto = {
        'pasillos': Pasillo.objects.all(),
        'proveedor': Proveedor.objects.filter(activo=1),
        'productos': Productos.objects.filter(activo=1),
        'titulo': 'Productos',
    }
    return render(request, 'productos/productos.html', contexto)


# MODULO SOPORTE TECNICO
def soporte(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        context = {
            'nombre': nombre,
            'email': email,
            'asunto': asunto,
            'mensaje': mensaje
        }

        contenido = render_to_string('email/email.html', context)
        texto_contenido = f'Nombre: {nombre}\nEmail: {email}\nAsunto: {asunto}\nMensaje: {mensaje}'

        email_usuario = EmailMultiAlternatives(
            subject=asunto,
            body=texto_contenido,
            from_email=settings.EMAIL_HOST_USER,
            to=['gestyinventarios@gmail.com']
        )
        email_usuario.attach_alternative(contenido, 'text/html')

        try:
            email_usuario.send()
            messages.success(request, 'Mensaje enviado correctamente.🤩!')
        except Exception as e:
            messages.error(request, 'Error al enviar el mensaje. Por favor, inténtelo de nuevo más tarde. 😕')
        return redirect('apps:soporte')
    
    return render(request, 'email/soporte.html', {
        'titulo': 'Soporte Técnico',
    })


@login_required
def usuarios(request):
    if request.method == 'POST':
        id_usuario = request.POST.get('id_usuario')
        nombres = request.POST.get('nombres')
        identificacion = request.POST.get('identificacion')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        producto_id = request.POST.get('productos')
        cantidad_asignada = int(request.POST.get('cantidad_asignada', 0))

        producto = get_object_or_404(Productos, id_productos=producto_id)

        if id_usuario:
            usuario = get_object_or_404(Usuarios, id_usuario=id_usuario)
            usuario.nombres = nombres
            usuario.identificacion = identificacion
            usuario.email = email
            usuario.celular = celular
            usuario.save()
        else:
            usuario = Usuarios.objects.create(
                nombres=nombres,
                identificacion=identificacion,
                celular=celular,
                email=email,
            )

        usuario_producto, creado = UsuarioProducto.objects.get_or_create(
            usuario=usuario,
            producto=producto,
            defaults={'cantidad_asignada': cantidad_asignada}
        )

        if creado:
            if producto.cantidad < cantidad_asignada:
                messages.error(request, 'No hay suficiente inventario disponible. 😓')
                return redirect('apps:usuarios')
            producto.cantidad -= cantidad_asignada
        else:
            cantidad_anterior = usuario_producto.cantidad_asignada
            diferencia = cantidad_asignada - cantidad_anterior
            if diferencia > 0:
                if producto.cantidad < diferencia:
                    messages.error(request, 'No hay suficiente inventario para aumentar la cantidad asignada. 😓')
                    return redirect('apps:usuarios')
                producto.cantidad -= diferencia
            elif diferencia < 0:
                producto.cantidad += abs(diferencia)

            usuario_producto.cantidad_asignada = cantidad_asignada

        usuario_producto.save()
        producto.save()

        messages.success(request, 'Usuario registrado y producto asignado correctamente. 🎉!')
        return redirect('apps:usuarios')

    contexto = {
        'usuarios': Usuarios.objects.all(),
        'productos': Productos.objects.filter(activo=1),
        'titulo': 'Usuarios',
    }
    return render(request, 'usuario/usuario.html', contexto)




# CERRAR SESIÓN
def salir(request):
    logout(request)
    return redirect('login')
