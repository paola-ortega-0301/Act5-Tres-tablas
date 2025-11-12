from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicio, Evento, Empleado
from django.core.exceptions import ValidationError

# Página de inicio
def inicio_evento(request):
    return render(request, 'inicio.html')

# Agregar servicio
def agregar_servicio(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        costo = request.POST['costo']
        duracion_horas = request.POST['duracion_horas']
        tipo = request.POST['tipo']
        disponible = request.POST.get('disponible', False) == 'on'

        nuevo = Servicio(
            nombre=nombre,
            descripcion=descripcion,
            costo=costo,
            duracion_horas=duracion_horas,
            tipo=tipo,
            disponible=disponible
        )
        nuevo.save()
        return redirect('ver_servicio')
    return render(request, 'servicio/agregar_servicio.html')


# Ver servicios
def ver_servicio(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicio/ver_servicio.html', {'servicios': servicios})


# Actualizar servicio
def actualizar_servicio(request, id):
    print(f"DEBUG: Accediendo a actualizar_servicio para ID: {id}")
    servicio = Servicio.objects.get(id=id)
    return render(request, 'servicio/actualizar_servicio.html', {'servicio': servicio})


# Realizar actualización
def realizar_actualizacion_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    if request.method == 'POST':
        servicio.nombre = request.POST['nombre']
        servicio.descripcion = request.POST['descripcion']
        servicio.costo = request.POST['costo']
        servicio.duracion_horas = request.POST['duracion_horas']
        servicio.tipo = request.POST['tipo']
        servicio.disponible = request.POST.get('disponible', False) == 'on'
        servicio.save()
        return redirect('ver_servicio')
    return redirect('ver_servicio')


# Borrar servicio
def borrar_servicio_confirmar(request, id):
    servicio = get_object_or_404(Servicio, id=id) # Usa get_object_or_404 para manejar IDs no válidos
    return render(request, 'servicio/borrar_servicio.html', {'servicio': servicio})

# Vista que realmente borra el servicio (ahora solo con POST)
def borrar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    if request.method == 'POST': # Asegúrate de que solo se borre con una petición POST
        servicio.delete()
        return redirect('ver_servicio')
    # Si alguien intenta acceder directamente con GET a esta URL, lo redirigimos
    return redirect('ver_servicio')

# Vistas de EMPLEADO (Nuevas)
def agregar_empleado(request):
    eventos = Evento.objects.all() # Necesitamos los eventos para el ForeignKey
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        puesto = request.POST['puesto']
        salario = request.POST['salario']
        telefono = request.POST['telefono']
        email = request.POST['email']
        fecha_contratacion = request.POST['fecha_contratacion']
        evento_id = request.POST['evento']

        # Obtener la instancia del evento
        evento = get_object_or_404(Evento, id=evento_id)

        nuevo_empleado = Empleado(
            nombre=nombre,
            apellido=apellido,
            puesto=puesto,
            salario=salario,
            telefono=telefono,
            email=email,
            fecha_contratacion=fecha_contratacion,
            evento=evento
        )
        nuevo_empleado.save()
        return redirect('ver_empleado')
    return render(request, 'empleado/agregar_empleado.html', {'eventos': eventos})

def ver_empleado(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})

def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    eventos = Evento.objects.all()
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado, 'eventos': eventos})

def realizar_actualizacion_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.puesto = request.POST['puesto']
        empleado.salario = request.POST['salario']
        empleado.telefono = request.POST['telefono']
        empleado.email = request.POST['email']
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        evento_id = request.POST['evento']
        empleado.evento = get_object_or_404(Evento, id=evento_id)
        empleado.save()
        return redirect('ver_empleado')
    return redirect('ver_empleado')

def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.delete()
    return redirect('ver_empleado')

# Vista de confirmación de borrado para empleados (opcional, pero buena práctica)
def confirmar_borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleado')
    return render(request, 'empleado/confirmar_borrar_empleado.html', {'empleado': empleado})

# Vistas de EVENTO (Nuevas)
# ==========================================
def agregar_evento(request):
    servicios = Servicio.objects.all() # Necesitamos los servicios para la relación ManyToMany
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        ubicacion = request.POST['ubicacion']
        capacidad = request.POST['capacidad']
        precio_base = request.POST['precio_base']
        servicios_seleccionados_ids = request.POST.getlist('servicios') # Obtener una lista de IDs

        nuevo_evento = Evento(
            nombre=nombre,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            ubicacion=ubicacion,
            capacidad=capacidad,
            precio_base=precio_base
        )
        nuevo_evento.save() # Guarda el evento primero para poder añadir servicios a la relación ManyToMany
        nuevo_evento.servicios.set(servicios_seleccionados_ids) # Asigna los servicios

        return redirect('ver_evento')
    return render(request, 'evento/agregar_evento.html', {'servicios': servicios})

def ver_evento(request):
    eventos = Evento.objects.all()
    return render(request, 'evento/ver_evento.html', {'eventos': eventos})

def actualizar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    servicios = Servicio.objects.all()
    return render(request, 'evento/actualizar_evento.html', {'evento': evento, 'servicios': servicios})

def realizar_actualizacion_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.nombre = request.POST['nombre']
        evento.descripcion = request.POST['descripcion']
        evento.fecha_inicio = request.POST['fecha_inicio']
        evento.fecha_fin = request.POST['fecha_fin']
        evento.ubicacion = request.POST['ubicacion']
        evento.capacidad = request.POST['capacidad']
        evento.precio_base = request.POST['precio_base']
        servicios_seleccionados_ids = request.POST.getlist('servicios')

        evento.save() # Guarda los cambios del evento
        evento.servicios.set(servicios_seleccionados_ids) # Actualiza la relación ManyToMany

        return redirect('ver_evento')
    return redirect('ver_evento')

def borrar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    evento.delete()
    return redirect('ver_evento')

def confirmar_borrar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('ver_evento')
    return render(request, 'evento/confirmar_borrar_evento.html', {'evento': evento})