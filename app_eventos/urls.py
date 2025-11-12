from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_evento, name='inicio_evento'),
    path('agregar_servicio/', views.agregar_servicio, name='agregar_servicio'),
    path('ver_servicio/', views.ver_servicio, name='ver_servicio'),
    path('actualizar_servicio/<int:id>/', views.actualizar_servicio, name='actualizar_servicio'),
    path('realizar_actualizacion_servicio/<int:id>/', views.realizar_actualizacion_servicio, name='realizar_actualizacion_servicio'),

    # Nuevas URLs para la confirmación de borrado
    path('borrar_servicio/<int:id>/', views.borrar_servicio_confirmar, name='borrar_servicio_confirmar'), # Muestra el formulario de confirmación
    path('confirmar_borrar_servicio/<int:id>/', views.borrar_servicio, name='confirmar_borrar_servicio'), # Ejecuta el borrado real


    # URLs de Empleado (Nuevas)
    path('agregar_empleado/', views.agregar_empleado, name='agregar_empleado'),
    path('ver_empleado/', views.ver_empleado, name='ver_empleado'),
    path('actualizar_empleado/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('realizar_actualizacion_empleado/<int:id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('borrar_empleado/<int:id>/', views.borrar_empleado, name='borrar_empleado'),
    path('confirmar_borrar_empleado/<int:id>/', views.confirmar_borrar_empleado, name='confirmar_borrar_empleado'),

    # URLs de Evento (Nuevas)
    path('agregar_evento/', views.agregar_evento, name='agregar_evento'),
    path('ver_evento/', views.ver_evento, name='ver_evento'),
    path('actualizar_evento/<int:id>/', views.actualizar_evento, name='actualizar_evento'),
    path('realizar_actualizacion_evento/<int:id>/', views.realizar_actualizacion_evento, name='realizar_actualizacion_evento'),
    path('borrar_evento/<int:id>/', views.borrar_evento, name='borrar_evento'),
    path('confirmar_borrar_evento/<int:id>/', views.confirmar_borrar_evento, name='confirmar_borrar_evento'),
]