from django.contrib import admin
from django.urls import path
from .views import cerrar_sesion, login, home, busqueda_usuarios, chat, crearEncuesta, crearEvento,agregar_parti_evento, crearPublicacion, editar_encuesta, notificacion, olvidarContrasenia, pagina404,perfilUsuarios , perfil, resultadoEncuesta, editarPerfil,editarPublicacion, adminUsuarios, adminPublicaciones, adminEventos, adminEncuestas, modUsuario, modPublicacion, editar_evento, modEncuesta, repcontrasenia, adminDashboard, eliminar_publi, agregar_comentario, agregar_like_publi, archivar_publicacion_inicio, archivar_evento_inicio, agregar_respuesta_encuesta
from . import views

urlpatterns = [
    path('notificacion/',notificacion,name='NOT'),

    path('resultado_encuesta/',resultadoEncuesta,name='RES_ENC'),
    
    ################# INICIO DE SESION #################
    path('',login,name='LOGIN'),
    path('cerrar/',cerrar_sesion,name='CERRAR'),


    ################# OLVIDAR CONTRASENIA Y ENVIO DE CORREO #################
    path('olvidar_contrasenia/',olvidarContrasenia,name='OLV'),
    path('repetir_contrasenia/<str:numero_encriptado>/',repcontrasenia,name='REP_CONT'),

    path('enviar_correo',views.enviar_correo,name='enviar_correo'),
    

    ################# HOME #################
    path('Home/',home,name='HOME'),

    
    ################# PUBLICACION #################
    path('crear_publicacion/<int:id>/',crearPublicacion,name='CREA_PUBL'),
    path('archivar_publicacion_inicio/', archivar_publicacion_inicio, name='ARCH_PUB_INI'),
    path('editar_publicacion/<int:id>/',editarPublicacion,name='EDI_PUBLI'),
    path('eliminar_publi/',eliminar_publi, name='eliminar_publi'),

    path('obtener_publis_sede', views.obtener_publis_sede, name='obtener_publis_sede'),

    path('agregar_comentario', agregar_comentario, name='AGRE_COME'),
    path('eliminar_comentario/', views.eliminar_comentario, name='eliminar_comentario'),
    path('listar_comentarios/', views.listar_comentarios, name='listar_comentarios'), 

    path('agregar_like_publi',views.agregar_like_publi, name='agregar_like_publi'),
    

    ################# EVENTO #################
    path('crear_evento/<int:id>/',crearEvento,name='CREA_EVE'),
    path('archivar_evento_inicio/', archivar_evento_inicio, name='ARCH_EVE_INI'),
    path('editar_evento/<int:id>/',editar_evento,name='EDI_EVE'),
    path('eliminar_evento/', views.eliminar_evento, name='eliminar_evento'),

    path('agregar_parti_evento/<int:id>/',agregar_parti_evento,name='agregar_parti_evento'),


    ################# ENCUESTA #################
    path('crear_encuesta/<int:id>/',crearEncuesta,name='CREA_ENC'),
    path('archivar_encuesta_inicio/', views.archivar_encuesta_inicio, name='archivar_encuesta_inicio'),
    path('editar_encuesta/<int:id>/',editar_encuesta,name='EDI_ENC'),
    path('eliminar_encuesta/', views.eliminar_encuesta, name='eliminar_encuesta'),

    path('agregar_respuesta_encuesta', views.agregar_respuesta_encuesta, name='AGRE_RESP_ENC'),
    path('listar_resp_encu/', views.listar_resp_encu, name='LIST_RESP_ENCU'),


    ################# PERFIL DE USUARIO #################
    path('perfil/<int:id>/',perfil,name='PERF'),
    path('editar_perfil/<int:id>/',editarPerfil,name='EDI_PER'),

    path('perfil_usuarios/<int:id>/',perfilUsuarios,name='PER_USU'),
    path('busqueda_usuarios/',busqueda_usuarios,name='BUS_USU'),


    ################# CHAT #################
    path('chat/',chat,name='CHAT'),
    path('enviar_mensaje', views.enviar_mensaje, name='enviar_mensaje'),
    path('obtener_mensajes', views.obtener_mensajes, name='obtener_mensajes'),
    path('crear_chat', views.crear_chat, name='crear_chat'),

    #########################################
    #########################################
    #########################################
    ################# ADMIN #################
    path('Dashboard/',adminDashboard,name='DASH'),
    
    path('admin_usuarios/',views.adminUsuarios,name='ADM_USER'),
    path('admin_publicaciones/',views.adminPublicaciones,name='ADM_PUB'),
    path('admin_eventos/',views.adminEventos,name='ADM_EVE'),
    path('admin_encuestas/',views.adminEncuestas,name='ADM_ENC'),
    
    path('adm_modificar_publicacion/<int:id>/', views.modPublicacion, name='adm_modificar_publicacion'),
    path('adm_modificar_usuario/<int:id>/', views.modUsuario, name='adm_modificar_usuario'),
    path('adm_modificar_evento/<int:id>/', views.modEvento, name='adm_modificar_evento'),
    path('modificar_encuesta/<int:id>/',views.modEncuesta,name='adm_modificar_encuesta'),
    
    path('archivar_usuario', views.archivar_usuario, name='archivar_usuario'),
    path('archivar_publicacion', views.archivar_publicacion, name='archivar_publicacion'),
    path('archivar_evento', views.archivar_evento, name='archivar_evento'),
    path('archivar_encuesta', views.archivar_encuesta, name='archivar_encuesta'),
    
    path('modificar_usuario/',views.mod_actualizar_usuario,name='MOD_USER'),
    path('modificar_publicacion/',views.mod_actualizar_publicacion,name='MOD_PUB'),
    path('modificar_evento',views.mod_actualizar_evento,name='MOD_EVE'),
    path('modificar_encuesta/',views.mod_actualizar_encuesta,name='MOD_ENCU'),


    ################# PAGINA DE 404 #################
    path('pagina_404/',pagina404,name='404'),
    
    ################# SECCIONES #################
    path('secciones/',views.secciones,name='secciones'),
    path('seccion_modificar/<int:id>/',views.seccion_modificar,name='seccion_modificar'),
    path('agregar_usuario_seccion',views.agregar_usuario_seccion,name='agregar_usuario_seccion'),
    path('eliminar_usuario_seccion',views.eliminar_usuario_seccion,name='eliminar_usuario_seccion'),
    path('seccion_crear/',views.seccion_crear,name='seccion_crear'),
    path('form_seccion_crear',views.form_seccion_crear,name='form_seccion_crear'),
    
    
    path('grafico_respuestas',views.grafico_respuestas,name='grafico_respuestas'),
    path('guardar-token/',views.guardar_token,name='GUARDART'),
]