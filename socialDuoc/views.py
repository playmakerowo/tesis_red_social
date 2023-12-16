#####################################################################################
#####################################################################################
#####################################################################################
from django.shortcuts import render, redirect
# importar el modelo de la tabla user
from django.contrib.auth.models import  User
# importar librerias para validar el login
from django.contrib.auth import authenticate, logout, login as login_aut
# importar librerias para no ingresar si no se esta logeado
from django.contrib.auth.decorators import login_required

import cx_Oracle
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, reverse
from django.urls import reverse 
from django.http import JsonResponse
from django.shortcuts import render, redirect
import base64
from datetime import datetime
from django.core.paginator import Paginator 

#imports de recuperar contrasenia
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import ChangePasswordForm
#imports de enviar correo
from django.core.mail import send_mail
import secrets
from cryptography.fernet import Fernet
from django.http import HttpResponse, HttpResponseServerError
#####################################################################################
#####################################################################################
#####################################################################################
import firebase_admin
from firebase_admin import credentials, messaging
import threading
import json

firebase_cred =  credentials.Certificate({
  "type": "service_account",
  "project_id": "social-duoc-4909a",
  "private_key_id": "d3b6ff3b9278ff9f8b14e2ea9e226a8f1238521c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDO/bihV8EGasmc\nyhnv2FCrxpdnb4w/qvYTfoPTVuBHLTG5pdYJAvZrw1YOvwa7BfPHENwE2+f7jKbz\nxS/DfK11ARBgS+jnwQzPWSUKHccUvb00Xo4xyfqRNuAdPfkCnidBmVl3Yz/1Xb5N\nRxELbUYfRq6uAGNgfFUSLp/2YoGlLoArKT0YqgupuKz3lw/XFzzxjYMc4fL2m9Ul\nuT914UKJ8pCn/0G2dbfPf+nTwCpE8G+VY66Og5x2kUipueoQZQZcFnLOIxW0eU1o\nNwFE4vhcHDtm/jVRGDbZYjoCnLrmNz9vaJISoNkA9bfFicuIKSJ1/4p1cYyymkQt\n4nfL2J/JAgMBAAECgf9VZxnmd+6MV0MYDcrlyrp+JVISu1OCcWdWY7zAVffzZhI+\nJs5IqZBCpjW7n9WHFM2gNLSSzKjKgR3hNlqerbJjtCytjqRp+pzucDl4ExEw3ZhT\nIzBIGq3nfFy7s/Ypvlc0GbFwMOMSubrq54eAz3U/MkqgQEjAZowzFEmrvrj/DZKb\nm9elMBz7gcEnN54qTDSl+Al+zQzlWS3cfbgRklKKWVlHICL7qTfG/EJSm3udykhq\nQKrGSl0BpAml8F1iWVeOsLw2tzVHL6e7ROUHVbFOYOBxPZp3Uo2P1ulmu+g0jCub\n6jZscuoIB9FCDU7Hbr+L4ZOKcPs21+Fb8DyR9EECgYEA6STsj5UcNiczhLDNJU22\nQvLKJr9F3zMD0GIpwcarSLnNhPVRw4elQePSFcFvqZb6vDc/TYRxLSV6hBI0yWAt\nP+TssCL5btfj+lQOrPpuy2x/X8B83RPDox/hZi8pYfyjjnEaqm2uWAolXt3SeAnF\nz7tVAwgSxFCILtQgNTk3BIkCgYEA40hyuZ9aT33824sF2dsUVodHAFpd3CX/ctXu\nbOB+pZ9BfU2NSJlXF9mdYWmWWfbqvEMXwjkiKE+Qc031MN72F0eFJpMLi5xPMyon\nauWeW0AHDmA8w+UL0hyHQOnRupy8SU4UK0rhU0PmOU3TpRieB/MBe80P9cC3RQfL\nHeTgcUECgYEAsEV4jf6A+/ibnQFHuaKN4QRMDwuiumSJx63QQHAC5NOGLbaFAT63\nlZ+4ITbFRAWgwVlMBUHTh/zEKsLRIkgTLjHZOjrXOBUGiyeuiN43kpoPm8efIE9n\nJRhfhLC3qxwmVPXy4VRX8ryJELbKAHPzGWJbnhUmi0MQE8fSKit+C3ECgYEAj/bL\n9JfjdIaxK78brar/bu+xIaAb496NuAeaRozMq8v8h4of++RlLk5BSfq/qaylcyps\nWjImWLJNJTw0GwifiI9c39o0bfJMmHQTE7ruW45q6cg7tTnYCvbXFV8F4dZ1zVkP\nnXyIzV0s7w9FCEZXk2FxhyGVAm1XqPoOxpi7MgECgYAs7HysnS9pY+Hqi6te79fp\njuZVR+5KBsjj7EQBlQI4HR9w9WVpGggCjNLomcKUpORMiWv8LaB8Qbe9GVmP44zt\nyYXPrsmGNSb/1TSkDnioClcedaZr08emGWQRylKCMaqG5rwlsy/I54F9NQ/cfhOV\nKhtP4FbYc5+fG7aIH1gtdw==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-7siy8@social-duoc-4909a.iam.gserviceaccount.com",
  "client_id": "113518070356986281184",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-7siy8%40social-duoc-4909a.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})
firebase_app = firebase_admin.initialize_app(firebase_cred)


def enviar_notificacion():                
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()    
    proceso.callproc('SP_LISTAR_TOKENS', [v_salida])
    tokens = []
    for row in v_salida:
        token_value = row[1]
        tokens.append(token_value)
        
    #tokens_prueba = ["clkVecUL6Ek:APA91bF1ZocwZs_JDrixYs9G3KXpye3QlwN-chnBv7WWUCKtorykbocIB8cfy_KYp4h5i06QfAJJgqVVBwNPtL6RaGD45h4MYwGum_jwV38j-U-OT3mN5mVjKfDeNeuUARsbRapTsxvX"]
    global_message  = messaging.MulticastMessage(
        notification=messaging.Notification(
            title='Novedades',
            body='Novedades en la plataforma Social Duoc'
        ),
        tokens=tokens,   
    )
    print("enviando:", tokens) 
    messaging.send_multicast(global_message)

@csrf_exempt
def guardar_token(request):
    try:
        body = request.body.decode('utf-8')
        datos_body = json.loads(body)
        token = datos_body['token']
        user = request.user
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()

        # Llamada al procedimiento almacenado
        proceso.callproc('SP_TOKEN', [token, user.id])
        success = f'GUARDADO '
        print(success)
        return HttpResponse(success)

    except Exception as e:
        return (json.dumps({'mensaje': f'error al guardar: {str(e)}'}))


@login_required(login_url='/cerrar/')
def notificacion(request):
    return render(request,"notificacion.html")


@login_required(login_url='/cerrar/')
def resultadoEncuesta(request):
    return render(request,"ver_resultado_encuesta.html")


################# PAGINA DE 404 #################
@login_required(login_url='/cerrar/')
def pagina404(request):
    return render(request,"pagina_404.html")


################# RECUPERAR CONTRASEÑA #################
def olvidarContrasenia(request):
    return render(request,"olvidar_contrasenia.html")

def repcontrasenia(request, numero_encriptado):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']
            # Desencripta el número
            try:
                numero_str = base64.b64decode(numero_encriptado.encode()).decode()
                numero = int(numero_str)
            except Exception as e:
                # Manejo de errores en caso de que la desencriptación falle
                messages.error(request, 'No se pudo desencriptar el número')
                return redirect('404')  # Asegúrate de que '404' sea la URL correcta para mostrar el error.
            # Busca el usuario por ID
            user = User.objects.filter(id=numero).first()
            if user:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Contraseña cambiada exitosamente')
                return redirect('LOGIN')  # Cambia esto al nombre de tu vista de inicio de sesión
            else:
                messages.error(request, 'Usuario no encontrado')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
    else:
        form = ChangePasswordForm()

    return render(request, 'repetir_contrasenia.html', {'form': form})

################# ENVIAR CORREO #################
# Genera un token seguro
def generate_token():
    return secrets.token_urlsafe(32)

# Cifra el correo electrónico del destinatario
def encrypt_email(email, token):
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_email = f.encrypt(email.encode())
    return encrypted_email, key

# Descifra el correo electrónico del destinatario
def decrypt_email(encrypted_email, key):
    f = Fernet(key)
    decrypted_email = f.decrypt(encrypted_email).decode()
    return decrypted_email

# Envia el correo por medio de un link
def enviar_correo(request):
    if request.method == 'POST':
        destinatario = request.POST['correo']
        subject = 'Solicitud de recuperacion de contraseña'
        # Genera un token y cifra el correo electrónico
        token = generate_token()
        encrypted_email, key = encrypt_email(destinatario, token)
        from_email = ''
        recipient_list = [destinatario]
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida = instancia.connection.cursor()
        v_salida2 = instancia.connection.cursor()
        try:
            proceso.callproc('SP_verificar_correo', [destinatario, v_salida])
            resultado = []
            for row in v_salida:
                resultado.append(row)
            #Correo no valido
            if(resultado[0] == (0,)):
                success = f'El correo {destinatario} ingresado no es valido '
                return HttpResponse(success)
            proceso.callproc('SP_ENVIAR_CORREO', [ destinatario, v_salida2])
            correo = []
            for row in v_salida2:
                correo.append(row)
            numero = correo[0]
            # Envía el correo con el enlace de un solo uso
            if correo and len(correo[0]) > 0:
                numero = correo[0][0]  # Accede al primer elemento de la tupla
                numero_str = str(numero)  # Convierte el número en una cadena
                numero_encriptado = base64.b64encode(numero_str.encode()).decode()  # Encripta el número y convierte a cadena
                token_url = f'http://127.0.0.1:8000/repetir_contrasenia/{numero_encriptado}?token={token}'
                message = f'Haz clic en el siguiente enlace para restablecer tu contraseña: {token_url}'
                send_mail(subject, message, from_email, recipient_list)
                success = f'Correo enviado a {destinatario} exitosamente'
                return HttpResponse(success)
        except Exception as e:
            error_message = f'Error al enviar el correo a {destinatario}: {str(e)}'
            return HttpResponseServerError(error_message)
        

from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta


################# SECCION INICIO Y CIERRE DE SESION #################
@csrf_exempt
def login(request):
    # Obtener el contador de intentos de inicio de sesión de la sesión
    login_attempts = request.session.get('login_attempts', 0)
    last_login_attempt_time_str = request.session.get('last_login_attempt_time', None)

    if last_login_attempt_time_str:
        last_login_attempt_time = datetime.strptime(last_login_attempt_time_str, '%Y-%m-%d %H:%M:%S')
    else:
        last_login_attempt_time = None

    if request.POST:
        usuario = request.POST.get("txtCorreo")
        contra = request.POST.get("txtContra")

        current_time = datetime.now()

        if last_login_attempt_time:
            # Calcular la diferencia de tiempo desde el último intento fallido
            time_diff = current_time - last_login_attempt_time
            if time_diff < timedelta(minutes=1):
                # Si no ha pasado 1 minuto, mostrar un mensaje de espera
                tiempo_espera = (last_login_attempt_time + timedelta(minutes=1) - current_time).seconds
                contexto = {"mensaje": f"Demasiados intentos fallidos. Debe esperar {tiempo_espera} segundos antes de intentarlo nuevamente."}
                return render(request, "login.html", contexto)

        us = authenticate(request, username=usuario, password=contra)

        if us is not None and us.is_active:
            # Restablecer el contador de intentos si la autenticación es exitosa
            request.session['login_attempts'] = 0
            request.session['last_login_attempt_time'] = None
            login_aut(request, us)
            return redirect(reverse('HOME'))
        else:
            # Incrementar el contador de intentos
            login_attempts += 1
            request.session['login_attempts'] = login_attempts

            if login_attempts >= 4:
                # Si hay 4 o más intentos fallidos, guardar el tiempo del último intento como una cadena
                last_login_attempt_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
                request.session['last_login_attempt_time'] = last_login_attempt_time_str
                tiempo_espera = 60  # 1 minuto
                contexto = {"mensaje": f"Demasiados intentos fallidos. Debe esperar {tiempo_espera} segundos antes de intentarlo nuevamente."}
                return render(request, "login.html", contexto)

            contexto = {"mensaje": "Usuario o contraseña incorrectos"}
            return render(request, "login.html", contexto)

    return render(request, "login.html")


def cerrar_sesion(request):
    logout(request)
    return render(request, 'login.html')


################# HOME #################
@login_required(login_url='/cerrar/')
def home(request):
    from .models import contenido
    user = request.user
    # Conexión a la base de datos Oracle a través de Django
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    # Llamada al procedimiento almacenado
    v_salida0 = instancia.connection.cursor()
    proceso.callproc('SP_LISTAR_HOME', [v_salida0])
    contenidos = []
    for row in v_salida0:
        row_list = list(row)  # Convierte la tupla en una lista
        for i in [13, 14]:  # Process images at indexes 8 and 9
            blob_data = row_list[i]
            if blob_data is not None:
                imagen_bytes = blob_data.read()
                imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                
                if len(imagen_base64) > 0:
                    row_list[i] = imagen_base64
                else:
                    # Handle the case when the image is empty (assign a default image or handle it as needed)
                    row_list[i] = '0'
        # Convierte la lista nuevamente en una tupla y agrégala a la lista de publicaciones
        contenidos.append(tuple(row_list))
        
    lista_contenido = []
    for row in contenidos:
        contenido_item = contenido(
            tipo=row[0],
            id_publicacion=row[1],
            titulo=row[2],
            fecha=row[3],
            fecha_fin=row[4],
            nombre_usuario=row[5],
            descripcion=row[6],
            pregunta=row[7],
            link=row[8],
            respuesta_uno=row[9],
            respuesta_dos=row[10],
            like_count=row[11],
            id_usuario=row[12],  # Suponiendo que existe un objeto Usuario con el id dado
            foto_usuario=row[13],
            foto_publicacion=row[14],
            sede=row[15],
            usuario=row[16],
        )
        lista_contenido.append(contenido_item)
        
    v_salida2 = instancia.connection.cursor()
    proceso.callproc('SP_LISTAR_COMENTARIO', [v_salida2])
    comentarios = []
    for row in v_salida2:
        row_list = list(row)  # Convierte la tupla en una lista
        for i in [5]:  # Process images at indexes 8 and 9
            blob_data = row_list[i]
            if blob_data is not None:
                imagen_bytes = blob_data.read()
                imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                if len(imagen_base64) > 0:
                    row_list[i] = imagen_base64
                else:
                    # Handle the case when the image is empty (assign a default image or handle it as needed)
                    row_list[i] = '0'
        # Convierte la lista nuevamente en una tupla y agrégala a la lista de publicaciones
        comentarios.append(tuple(row_list))

    v_salida9 = instancia.connection.cursor()
    proceso.callproc("SP_ADM_SEDE", [v_salida9])
    sedes = []
    for row in v_salida9:
        sedes.append(row)
            
    v_salida7 = instancia.connection.cursor()
    # Llamada al procedimiento almacenado 
    proceso.callproc('SP_BUSCAR_USUARIO_ID', [user.id ,v_salida7])
    usuarios = []
    for row in v_salida7:
        row_list = list(row)  # Convierte la tupla en una lista
        blob_data = row_list[9] #ESPECIFICAS EN QUE PARTE DEL ARREGLO VIENE LA IMAGEN
        if blob_data is not None:
            imagen_bytes = blob_data.read()
            imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
            # Modifica la lista para agregar la representación en base64
            if len(imagen_base64) > 0:
                row_list[9] = imagen_base64
            else:
                # Si la imagen en base64 está vacía, puedes asignar una imagen predeterminada o manejarla de otra manera.
                row_list[9] = '0'
        # Convierte la lista nuevamente en una tupla y agrégala a la lista de usuarios
        usuarios.append(tuple(row_list))
    

    proceso = instancia.connection.cursor()
    v_salida11 = instancia.connection.cursor()  
    res_encu = []
    proceso.callproc("SP_ADM_TODA_ENCUESTA_RESPUESTAS", [v_salida11])
    for row in v_salida11:
        row_list = list(row)  # Convierte la tupla en una lista
        blob_data = row_list[6] #ESPECIFICAS EN QUE PARTE DEL ARREGLO VIENE LA IMAGEN
        if blob_data is not None:
            imagen_bytes = blob_data.read()
            imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
            # Modifica la lista para agregar la representación en base64

            if len(imagen_base64) > 0:
                row_list[6]=(imagen_base64)
            else:
                # Si la imagen en base64 está vacía, puedes asignar una imagen predeterminada o manejarla de otra manera.
                row_list[6]=('0')
        # Convierte la lista nuevamente en una tupla y agrégala a la lista de usuarios
        res_encu.append(tuple(row_list))

    proceso = instancia.connection.cursor()
    v_salida12 = instancia.connection.cursor()
    proceso.callproc('SP_LISTAR_ME_GUSTA', [v_salida12])
    megu = []
    for row in v_salida12:
        megu.append(row)


    # Realiza la búsqueda si se proporciona un término de búsqueda en la URL
    search_query = request.POST.get('q', '')  # Obtiene el término de búsqueda de la URL
    if search_query:
        lista_contenido = [lista_contenido for lista_contenido in lista_contenido if search_query.lower() in " ".join(map(str, lista_contenido)).lower()]

    paginator = Paginator(lista_contenido, 5)  # 5 usuarios por página
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    contexto ={"contenido":page, "search_query": search_query, "comentarios":comentarios, "respuestas":res_encu, "usuario":usuarios, "sedes":sedes, "megu":megu}
    return render(request,"Home.html", contexto)


################# CHAT #################
import queue

def enviar_notificacion_personal(id, id_origen):                
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()    
    v_salida2 = instancia.connection.cursor()   
    proceso.callproc('SP_LISTAR_TOKENS_USUARIO', [id,v_salida])
    proceso.callproc('SP_ADM_BUSCAR_USUARIO_ID', [id_origen,v_salida2])
    
    tokens = []
    for row in v_salida:
        token_value = row[1]
        tokens.append(token_value)
    usuario = []
    for row in v_salida2:
        nombre = row[2]
        usuario.append(nombre)        
    print(usuario)
    global_message  = messaging.MulticastMessage(
        notification=messaging.Notification(
            title='Mensajes: '+ usuario[0],
            body='Tienes mensajes en la plataforma Social Duoc'
        ),
        tokens=tokens,   
    )
    print("enviando:", tokens) 
    messaging.send_multicast(global_message)
    
def enviar_notificacion_grupal(id, id_origen):                
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()    
    v_salida2 = instancia.connection.cursor()   
    proceso.callproc('SP_LISTAR_TOKENS_GRUPOS', [id,id_origen,v_salida])
    tokens = []
    for row in v_salida:
        token_value = row[1]
        tokens.append(token_value)
        
    proceso.callproc('SP_BUSCAR_SECCION_ID', [id,v_salida2])
    seccion = []
    for row in v_salida2:
        nom_sseccion = row[1]
        seccion.append(nom_sseccion)
        
    global_message  = messaging.MulticastMessage(
        notification=messaging.Notification(
            title='Mensaje: '+ seccion[0],
            body='Tienes mensajes de grupos en Social Duoc'
        ),
        tokens=tokens,   
    )
    print("enviando:", tokens) 
    messaging.send_multicast(global_message)

#ejecuciones en segundo plano para notificar el chat
def worker(q, id_origen):
    while True:
        id_usuario_recep = q.get()
        enviar_notificacion_personal(id_usuario_recep, id_origen)
        q.task_done()

def worker_grupo(q, id_origen):
    while True:
        id_usuario_recep = q.get()
        enviar_notificacion_grupal(id_usuario_recep, id_origen)
        q.task_done()

@login_required(login_url='/cerrar/')
def crear_chat(request):
        try:
            if request.method == 'POST':
                user = request.user
                id_usuario = request.POST['usuario_id']
                instancia = connection.cursor()
                proceso = instancia.connection.cursor()
                # Llamada al procedimiento almacenado para eliminar al usuario por su ID
                proceso.callproc('SP_AGREGAR_CHAT', [user.id ,id_usuario])
                return redirect(chat)
        except Exception as e:
                error_message = f"Error: {str(e)}"
                return HttpResponse(error_message, status=400)

@login_required(login_url='/cerrar/')
def chat(request):
    user = request.user
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    v_salida2 = instancia.connection.cursor()
    
    proceso.callproc('SP_ADM_LISTAR_Chats', [user.id, v_salida2])
    chats = []

    for row in v_salida2:
        row_list = list(row)
        blob_data = row_list[3]  # ESPECIFICAS EN QUÉ PARTE DEL ARREGLO VIENE LA IMAGEN
        if blob_data is not None:
            imagen_bytes = blob_data.read()
            imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
            if len(imagen_base64) > 0:
                row_list[3] = imagen_base64
            else:
                row_list[3] = '0'
        # Convierte la lista nuevamente en una tupla y agrégala a la lista de usuarios
        chats.append(tuple(row_list))

    # Ahora, puedes construir la lista de diccionarios utilizando un bucle for
    chat_dicts = []
    for row in chats:
        chat_dict = {'id_chat': row[0], 'nombre_origen': row[1], 'nombre_receptor': row[2], 'foto': row[3], 'id_receptor': row[4], 'tipo': row[6]}
        chat_dicts.append(chat_dict)

    return render(request,"chat.html", {'chats':chat_dicts})
        
def enviar_mensaje(request):
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()

    if request.method == 'POST':
        chat_id = request.POST.get('chatIdInput')
        id_usuario = request.POST.get('id_usuario')
        id_usuario_recep = request.POST.get('id_usuario_recep')
        mensaje = request.POST.get('mensaje')
        tipo = request.POST.get('tipo')
        # Verificar si el mensaje está en blanco
        if not mensaje.strip():
            return JsonResponse({'estado': 'Error', 'mensaje': 'El mensaje no puede estar en blanco'})

        proceso.callproc('SP_AGREGAR_Mensaje', [mensaje, id_usuario_recep, id_usuario, chat_id, tipo])
            # Crear una cola y un hilo para procesar notificaciones en segundo plano
        if tipo == '1':
            q = queue.Queue()
            thread = threading.Thread(target=worker, args=(q, id_usuario))
            thread.daemon = True
            thread.start()

            # Agregar el trabajo a la cola
            q.put(id_usuario_recep)
            
        if tipo == '2':
            q = queue.Queue()
            thread = threading.Thread(target=worker_grupo, args=(q,id_usuario))
            thread.daemon = True
            thread.start()

            # Agregar el trabajo a la cola
            q.put(id_usuario_recep)

        return JsonResponse({'estado': 'OK'})

    return JsonResponse({'estado': 'Error', 'mensaje': 'La solicitud debe ser de tipo POST'})

def obtener_mensajes(request):
    user = request.user
    usuario_r_id = request.GET.get('usuario_id')
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    proceso.callproc('SP_ADM_LISTAR_Chat', [user.id,usuario_r_id, v_salida])
    
    mensajes_json = []
    for row in v_salida:
        mensaje = {
            'mensaje': row[0],
            'id_usu_origen': row[1],
            'id_usu_recep': row[2],
            'nombre_origen': row[3],
            'nombre_receptor': row[4],
            'fecha': row[5],
        }
        
        # Define el lado en base al usuario de origen
        if mensaje['id_usu_origen'] == user.id:
            mensaje['lado'] = 'left'
            mensaje['cuerpo'] = 'cuerpo-usuario'
            mensaje['color'] = 'background-color: #5D6D7E'
            
        else:
            mensaje['lado'] = ''
            mensaje['cuerpo'] = 'cuerpo'
            mensaje['color'] = 'background-color: #1F618D'
        
        mensajes_json.append(mensaje)

    return JsonResponse({'mensajes': mensajes_json})

################# SECCION PUBLICACION #################
@login_required(login_url='/cerrar/')
def crearPublicacion(request, id):
    connection = cx_Oracle.connect("SOCIALDUOC/SOCIALDUOC@//localhost:1521/xe")
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    
    # Llamada al procedimiento almacenado
    proceso.callproc('SP_LISTAR_SEDE', [v_salida])
    sede = []
    for row in v_salida:
        sede.append(row)
    
    if request.user.is_staff == 1:
        if request.method == 'POST':
            # Obtén los datos del formulario
            descripcion = request.POST.get('txtDesc')
            imagen_base64 = request.FILES.get('txtImg')
            sede_id = request.POST.get('cboSede')  # Cambia el nombre de la variable para evitar conflictos
            
            # Verifica si la descripción contiene solo espacios en blanco o está vacía
            if not descripcion.strip():
                messages.error(request, "La descripción no puede estar en blanco.")
                return redirect(reverse('CREA_PUBL', args=[id]))
            elif not sede_id:
                messages.error(request, "Debe seleccionar una sede.")
                return redirect(reverse('CREA_PUBL', args=[id]))
            elif not imagen_base64:
                messages.error(request, "Debe seleccionar una imagen.")
                return redirect(reverse('CREA_PUBL', args=[id]))
            else:
                try:
                    contenido_imagen = imagen_base64.read()
                    
                    # Configura la conexión a la base de datos Oracle
                    connection = cx_Oracle.connect("SOCIALDUOC/SOCIALDUOC@//localhost:1521/xe")
                    cursor = connection.cursor()
                    
                    # Llama al procedimiento PL/SQL para agregar una publicación
                    cursor.callproc("AGREGAR_PUBLICACION", [descripcion, id, contenido_imagen, sede_id])
                    connection.commit()
                    messages.success(request, "EXITO")
                    return redirect(reverse('CREA_PUBL', args=[id]))
                except Exception as e:
                    messages.error(request, "Error: ", e )
                    return redirect(reverse('CREA_PUBL', args=[id]))
    else:
        return redirect('404')
    
    contexto = {"sede": sede}
    return render(request, "crear_publicacion.html", contexto)

@login_required(login_url='/cerrar/')
def editarPublicacion(request, id):
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida2 = instancia.connection.cursor()
    proceso.callproc('SP_LISTAR_SEDE', [v_salida2])
    sede = []
    for row in v_salida2:
        sede.append(row)
    mensaje = ''
    estilo_mensaje = 'dysplay: none;'
    
    if request.method == 'POST':
        descripcion = request.POST.get('txtDesc')
        imagen_base64 = request.FILES.get('txtImg', None)
        nueva_sede = request.POST.get('cboSede', None)
        # Verificar si se proporcionó una nueva imagen
        if imagen_base64:
            try:
                contenido_imagen = imagen_base64.read()
                proceso = instancia.connection.cursor()
                proceso.callproc('SP_ACTUALIZAR_IMAGEN', [id, contenido_imagen])
                messages.success(request, "EXITO")
                connection.commit()
                return redirect(reverse('EDI_PUBLI', args=[id]))
            except Exception as e:
                messages.error(request, "Error al procesar la foto: " + ({'error': str(e)}))
                return redirect(reverse('EDI_PUBLI', args=[id]))
        # Verifica si la descripción contiene solo espacios en blanco o está vacía
        if not descripcion.strip():
            messages.error(request, "La descripción no puede estar en blanco.")
            return redirect(reverse('EDI_PUBLI', args=[id]))
        else:
            # Llamada al procedimiento almacenado para modificar la publicación
            proceso = instancia.connection.cursor()
            proceso.callproc('SP_MODIFICAR_PUBLICACION', [id, descripcion, nueva_sede])
            connection.commit()
            messages.success(request, "EXITO")
            return redirect(reverse('EDI_PUBLI', args=[id]))
    
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    proceso.callproc('SP_LISTAR_PUBLICACION_USU', [id, v_salida])
    publicaciones = []
    for row in v_salida:
            row_list = list(row)  # Convierte la tupla en una lista
            for i in [9]:  # Process images at indexes 8 and 9
                blob_data = row_list[i]
                if blob_data is not None:
                    imagen_bytes = blob_data.read()
                    imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                    
                    if len(imagen_base64) > 0:
                        row_list[i] = imagen_base64
                    else:
                        # Handle the case when the image is empty (assign a default image or handle it as needed)
                        row_list[i] = '0'
            # Convierte la lista nuevamente en una tupla y agrégala a la lista de publicaciones
            publicaciones.append(tuple(row_list))
    contexto = {"publicaciones": publicaciones, "mensaje": mensaje, "sede":sede, "estilo_mensaje":estilo_mensaje}
    return render(request, "editar_publicacion.html", contexto)

@login_required(login_url='/cerrar/')
def agregar_comentario(request):
    if request.method == 'POST':
        id_publi = request.POST.get('id_publi')
        comentario = request.POST.get('comentario')
        id_usuario = request.POST.get('id_usuario')
        
        # Elimina espacios en blanco al inicio y al final del comentario
        comentario = comentario.strip()
        # Verifica que el comentario no esté en blanco
        if not comentario:
            return HttpResponse('ERROR: El comentario no puede estar en blanco.')
        try:
            instancia = connection.cursor()
            proceso = instancia.connection.cursor()
            v_salida = instancia.connection.cursor()
            # Ejecuta el procedimiento almacenado SP_AGREGAR_COMENTARIO
            proceso.callproc("SP_AGREGAR_COMENTARIO", [comentario, id_publi, id_usuario])
            connection.commit()
            proceso.callproc('SP_LISTAR_COMENTARIO', [v_salida])
            comentarios = []
            for row in v_salida:
                row_list = list(row)  # Convierte la tupla en una lista
                for i in [5]:  # Process images at indexes 8 and 9
                    blob_data = row_list[i]
                    if blob_data is not None:
                        imagen_bytes = blob_data.read()
                        imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                        if len(imagen_base64) > 0:
                            row_list[i] = imagen_base64
                        else:
                            # Handle the case when the image is empty (assign a default image or handle it as needed)
                            row_list[i] = '0'
                # Convierte la lista nuevamente en una tupla y agrégala a la lista de publicaciones
                comentarios.append(tuple(row_list))
                id_publi = int(id_publi)
            comentarios_filtrados = [comentario for comentario in comentarios if comentario[0] == id_publi]
            comentarios_filtrados_dic = []
            for row in comentarios_filtrados:
                comentario_dic = {
                    'id_publi': row[0],
                    'id_usuario': row[1],
                    'comentario': row[2],
                    'nombre': row[3],
                    'id_comentario': row[4],
                    'imagen': row[5],
                    'usuario': row[6]
                }
                comentarios_filtrados_dic.append(comentario_dic)
            return JsonResponse({'success': 'EXITO','comentarios': comentarios_filtrados_dic})
        except cx_Oracle.Error as error:
            # Maneja el error de manera apropiada
            print("Error al ejecutar el procedimiento almacenado:", error)
            connection.rollback()
    success = 'ERROR'
    return HttpResponse(success)

@login_required(login_url='/cerrar/')
def eliminar_comentario(request):
    try:
        if request.method == 'POST':
            publicacion_id = request.POST['publicacion_id'] 
            comentario_id = request.POST['comentario_id'] 
            instancia = connection.cursor()
            proceso = instancia.connection.cursor()
            proceso.callproc('SP_ELI_COMENT', [publicacion_id, comentario_id])
            mensaje = "Comentario eliminado con éxito"  # Corregir el mensaje
            contexto = {"mensaje": mensaje}
            return redirect('HOME')  # Corregir la redirección a 'home'
    except Exception as e:
        mensaje = "Error al eliminar el comentario: " + str(e)
        return render(request, 'Home.html', {"mensaje": mensaje})

@login_required(login_url='/cerrar/')
def agregar_like_publi(request):
    try:
        if request.method == 'POST':
            id_usuario = request.POST['id_usuario']
            id_publi = request.POST['id_publi']
            # Llamada al procedimiento almacenado para agregar el "Me gusta"
            with connection.cursor() as instancia:
                instancia.callproc('SP_AGREGAR_LIKE', [id_publi, id_usuario])
            success = 'Ya se dio Me gusta'
            return HttpResponse(success)
        else:
            # Maneja el caso en el que no es una solicitud POST
            return HttpResponse('Método no permitido')
    except Exception as e:
        error_message = f'Error: {str(e)}'
        return HttpResponse(error_message)

@login_required(login_url='/cerrar/')
def archivar_publicacion_inicio(request):
    try:
        publicacion_id = request.POST['publicacion_id'] 
        # Llamada al procedimiento almacenado para eliminar la publicación por su ID
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida = instancia.connection.cursor()
        proceso.callproc('SP_ADM_ARCHIVAR_PUBLICACION', [publicacion_id, v_salida])
        connection.commit()
        mensaje = "Publicación archivada con éxito"
        # Redirecciona de nuevo a la página de inicio
        contexto = {"mensaje": mensaje}
        return redirect(reverse('HOME'), contexto)
    except Exception as e:
        mensaje = "Error al archivar la publicación: " + str(e)
        # Redirecciona de nuevo a la página de inicio
        return render(request, 'Home.html', {"mensaje": mensaje})

@login_required(login_url='/cerrar/')
def eliminar_publi(request):
    try:
        publicacion_id = request.POST['publicacion_id'] 
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        proceso.callproc('ELIMINAR_PUBLICACION', [publicacion_id])
        mensaje = "Publicación eliminada con éxito"
        contexto = { "mensaje": mensaje}
        return redirect(reverse('HOME'), contexto)
    except Exception as e:
        mensaje = "Error al eliminar la publicación: " + str(e)
        # Redirecciona de nuevo a la página de inicio
        return render(request, 'Home.html', {"mensaje": mensaje})

@login_required(login_url='/cerrar/')
def listar_comentarios(request):
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    # Llamada al procedimiento almacenado
    proceso.callproc('SP_LISTAR_COMENTARIO', [v_salida])
    comentarios = []
    for row in v_salida:
        comentarios.append(row)
    contexto ={"comentarios":comentarios}
    return render(request,"Home.html", contexto)

def obtener_publis_sede(request):
    if request.method == 'POST':
        id_sede = request.POST.get('id_sede')
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida = instancia.connection.cursor()
        v_salida2 = instancia.connection.cursor()
        # Llamada al procedimiento almacenado
        proceso.callproc('SP_LISTAR_PUBLICACION_SEDE', [id_sede, v_salida])
        publicaciones = []
        for row in v_salida:
            row_list = list(row)  # Convierte la tupla en una lista
            for i in [8, 9]:  # Process images at indexes 8 and 9
                blob_data = row_list[i]
                if blob_data is not None:
                    imagen_bytes = blob_data.read()
                    imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                    
                    if len(imagen_base64) > 0:
                        row_list[i] = imagen_base64
                    else:
                        # Handle the case when the image is empty (assign a default image or handle it as needed)
                        row_list[i] = '0'
            # Convierte la lista nuevamente en una tupla y agrégala a la lista de publicaciones
            publicaciones.append(tuple(row_list))
        publicaciones_dicts = []  # Inicializa una lista vacía fuera del bucle
        for row in publicaciones:
            publicacion_dict = {
                'id_publi': row[0],
                'nombre_publicador': row[1],
                'fecha': row[2],
                'descripcion': row[3],
                'estado': row[4],
                'likes': row[5],
                'id_publicador': row[6],
                'sede': row[7],
                'foto': row[8],
                'foto_user': row[9]
            }
            publicaciones_dicts.append(publicacion_dict)  # Agrega el diccionario a la lista
        proceso.callproc('SP_LISTAR_COMENTARIO', [v_salida2])
        comentarios = []
        for row in v_salida2:
            row_list = list(row)  # Convierte la tupla en una lista
            for i in [5]:  # Process images at indexes 8 and 9
                blob_data = row_list[i]
                if blob_data is not None:
                    imagen_bytes = blob_data.read()
                    imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                    
                    if len(imagen_base64) > 0:
                        row_list[i] = imagen_base64
                    else:
                        # Handle the case when the image is empty (assign a default image or handle it as needed)
                        row_list[i] = '0'
            # Convierte la lista nuevamente en una tupla y agrégala a la lista de publicaciones
            comentarios.append(tuple(row_list))
        comentarios_dicts = [] 
        for row in comentarios:
            comentarios_dict = {
                'id_publi': row[0],
                'id_usuario': row[1],
                'comentario': row[2],
                'nombre': row[3],
                'id_coment': row[4],
                'foto': row[5],
            }
            comentarios_dicts.append(comentarios_dict)
        return JsonResponse({'publicaciones': publicaciones_dicts, 'id_sede': id_sede, 'comentarios':comentarios_dicts})
    

################# SECCION ENCUESTA #################
@login_required(login_url='/cerrar/')
def crearEncuesta(request, id):
    if request.user.is_staff == 1:
        if request.method == 'POST':
            # Obtén los datos del formulario
            titulo = request.POST.get('txtTitulo')
            pregunta = request.POST.get('txtPregunta')
            descripcion = request.POST.get('txtDesc')
            link = request.POST.get('txtlink')
            fechaI = request.POST.get('fechaI')
            fechaF = request.POST.get('fechaF')
            respuesta_uno = request.POST.get('respuesta_uno')
            respuesta_dos = request.POST.get('respuesta_dos')
            

            # Verifica si alguno de los campos contiene solo espacios en blanco o está vacío
            if not all([campo.strip() for campo in [titulo, pregunta, descripcion, link, fechaI, fechaF,respuesta_uno,respuesta_dos]]):
                messages.error(request, "Ninguno de los campos puede estar en blanco.")
                return redirect(reverse('CREA_ENC', args=[id]))
            else:
                # Convierte las cadenas de fecha en objetos de fecha de Python
                fecha_ini = datetime.strptime(fechaI, '%Y-%m-%d')
                fecha_fin = datetime.strptime(fechaF, '%Y-%m-%d')
                try:
                    connection = cx_Oracle.connect("SOCIALDUOC/SOCIALDUOC@//localhost:1521/xe")
                    cursor = connection.cursor()
                    # Llama al procedimiento PL/SQL
                    cursor.callproc("SP_AGREGAR_ENCUESTA", [titulo, pregunta, descripcion, fecha_ini, link, id, fecha_fin,respuesta_uno,respuesta_dos])
                    connection.commit()
                    messages.success(request, "EXITO")
                    return redirect(reverse('CREA_ENC', args=[id]))
                except Exception as e:
                    messages.error(request, "ERROR: ", ({'error': str(e)}))
                    return redirect(reverse('CREA_ENC', args=[id]))
    else:
        return redirect('404')
    return render(request, "crear_encuesta.html")

@login_required(login_url='/cerrar/')
def archivar_encuesta_inicio(request):
    try:
        encuesta_id = request.POST['encuesta_id'] 
        # Llamada al procedimiento almacenado para eliminar la publicación por su ID
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida = instancia.connection.cursor()
        proceso.callproc('SP_ADM_ARCHIVAR_ENCUESTA', [encuesta_id, v_salida])
        connection.commit()
        
        mensaje = "Publicación archivada con éxito"

        # Redirecciona de nuevo a la página de inicio
        contexto = {"mensaje": mensaje}
        return redirect(reverse('HOME'), contexto)

    except Exception as e:
        mensaje = "Error al archivar la publicación: " + str(e)

        # Redirecciona de nuevo a la página de inicio
        return render(request, 'Home.html', {"mensaje": mensaje})

@login_required(login_url='/cerrar/')
def eliminar_encuesta(request):
    try:
        encuesta_id = request.POST['encuesta_id'] 
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        proceso.callproc('SP_ELIMINAR_ENCUESTA', [encuesta_id])
        mensaje = "Publicación eliminada con éxito"
        contexto = { "mensaje": mensaje}
        return redirect(reverse('HOME'), contexto)
    except Exception as e:
        mensaje = "Error al eliminar la publicación: " + str(e)
        # Redirecciona de nuevo a la página de inicio
        return render(request, 'Home.html', {"mensaje": mensaje})

@login_required(login_url='/cerrar/')
def editar_encuesta(request, id):
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    proceso.callproc('SP_LISTAR_ENCUESTAS_USU', [id, v_salida])
    encuestas = []
    for row in v_salida:
        encuestas.append(row)
        if request.method == 'POST':
            titulo = request.POST.get('txtTitulo')
            pregunta = request.POST.get('txtPregunta')
            descripcion = request.POST.get('txtDesc')
            link = request.POST.get('txtlink')
            fechaI = request.POST.get('fechaI')
            fechaF = request.POST.get('fechaF')
            respuesta_uno = request.POST.get('respuesta_uno')
            respuesta_dos = request.POST.get('respuesta_dos')
            
            # Validar que no queden espacios en blanco en los campos (excepto descripcion y link)
            if not titulo.strip() or not pregunta.strip() or not fechaI.strip() or not fechaF.strip() or not respuesta_uno.strip() or not respuesta_dos.strip():
                messages.error(request, "Por favor, complete todos los campos, no puede enviar campos vacios.")
                return redirect(reverse('EDI_ENC', args=[id]))


            proceso.callproc('SP_MODIFICAR_ENCUESTA', [titulo, pregunta, descripcion, link, id, fechaI, fechaF, respuesta_uno, respuesta_dos])
            connection.commit()
            messages.success(request, "EXITO")
            return redirect(reverse('EDI_ENC', args=[id]))
            
    contexto ={"encuestas": encuestas}
    return render(request,"editar_encuesta.html", contexto)

@login_required(login_url='/cerrar/')
def agregar_respuesta_encuesta(request):
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta') # Elimina los espacios en blanco al principio y al final
        id_usuario = request.POST.get('id_usuario')
        id_encuesta = request.POST.get('id_encu')
        
        # Verificar si la respuesta está en blanco después de quitar espacios
        if not respuesta:
            # Mostrar un mensaje de error o realizar otra acción según tus necesidades
            mensaje = 'La respuesta no puede estar en blanco.'
            contexto = {"mensaje": mensaje}
            return render(request, 'Home.html', contexto)
        
        # Continúa con el procesamiento normal de la respuesta
        connection = cx_Oracle.connect("SOCIALDUOC/SOCIALDUOC@//localhost:1521/xe")
        cursor = connection.cursor()
        try:
            cursor.callproc("SP_AGREGAR_RESP_ENCUE", [respuesta, id_encuesta, id_usuario])
            connection.commit()
            instancia = connection.cursor()
            proceso = instancia.connection.cursor()
            v_salida = instancia.connection.cursor()
            # Llamada al procedimiento almacenado
            proceso.callproc('SP_LISTAR_RESP_ENCUE', [v_salida])

            respuestas = []
            for row in v_salida:
                respuestas.append(row)
            contexto = {"respuestas": respuestas}
            success = 'EXITO'
            return HttpResponse(success)
        except cx_Oracle.Error as error:
            print("Error al ejecutar el procedimiento almacenado:", error)
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    success = 'ERROR'
    return HttpResponse(success)

@login_required(login_url='/cerrar/')
def listar_resp_encu(request):
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    # Llamada al procedimiento almacenado
    proceso.callproc('SP_LISTAR_RESP_ENCUE', [v_salida])
    respuestas = []
    for row in v_salida:
        respuestas.append(row)
    
    v_salida2 = instancia.connection.cursor()
    # Llamada al procedimiento almacenado 
    proceso.callproc('SP_buscar_LISTAR_USUARIO', [v_salida2])
    usuarios = []
    for row in v_salida2:
        usuarios.append(row)

    contexto = {"respuestas": respuestas}

    return render(request, "Home.html", contexto)


################# SECCION EVENTO #################
@login_required(login_url='/cerrar/')
def crearEvento(request, id):
    mensaje = ''
    if request.user.is_staff == 1:
        if request.method == 'POST':
            # Obtén los datos del formulario
            titulo = request.POST.get('txtTitulo')
            descripcion = request.POST.get('txtDesc')
            fechaI = request.POST.get('fechaI')
            fechaF = request.POST.get('fechaF')

            # Verifica si alguno de los campos contiene solo espacios en blanco o está vacío
            if not all([campo.strip() for campo in [titulo, descripcion, fechaI, fechaF]]):
                messages.error(request, "Ninguno de los campos puede estar en blanco.")
                return redirect(reverse('CREA_EVE', args=[id]))
            else:
                # Convierte las cadenas de fecha en objetos de fecha de Python
                fecha_ini = datetime.strptime(fechaI, '%Y-%m-%d')
                fecha_fin = datetime.strptime(fechaF, '%Y-%m-%d')
                try:
                    connection = cx_Oracle.connect("SOCIALDUOC/SOCIALDUOC@//localhost:1521/xe")
                    cursor = connection.cursor()
                    # Llama al procedimiento PL/SQL para agregar un evento
                    cursor.callproc("SP_AGREGAR_EVENTO", [titulo, fecha_ini, descripcion, id, fecha_fin])
                    connection.commit()
                    messages.success(request, "EXITO")
                    return redirect(reverse('CREA_EVE', args=[id]))
                except Exception as e: 
                    messages.error(request, "ERROR: ", {'error': str(e)})
                    return redirect(reverse('CREA_EVE', args=[id]))
    else:
        return redirect('404')
    contexto = {"mensaje": mensaje}
    return render(request, "crear_evento.html", contexto)

@login_required(login_url='/cerrar/')
def archivar_evento_inicio(request):
    try:
        evento_id = request.POST['evento_id'] 
        # Llamada al procedimiento almacenado para eliminar la publicación por su ID
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida = instancia.connection.cursor()
        proceso.callproc('SP_ADM_ARCHIVAR_EVENTO', [evento_id, v_salida])
        connection.commit()
        
        mensaje = "Publicación archivada con éxito"

        # Redirecciona de nuevo a la página de inicio
        contexto = {"mensaje": mensaje}
        return redirect(reverse('HOME'), contexto)

    except Exception as e:
        mensaje = "Error al archivar la publicación: " + str(e)

        # Redirecciona de nuevo a la página de inicio
        return render(request, 'Home.html', {"mensaje": mensaje})

@login_required(login_url='/cerrar/')
def eliminar_evento(request):
    try:
        evento_id = request.POST['evento_id'] 
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        proceso.callproc('SP_ELIMINAR_EVENTO', [evento_id])
        mensaje = "Publicación eliminada con éxito"
        contexto = { "mensaje": mensaje}
        return redirect(reverse('HOME'), contexto)
    except Exception as e:
        mensaje = "Error al eliminar la publicación: " + str(e)
        # Redirecciona de nuevo a la página de inicio
        return render(request, 'Home.html', {"mensaje": mensaje})

@login_required(login_url='/cerrar/')
def editar_evento(request, id):
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    v_salida5 = instancia.connection.cursor()
    v_salida2 = instancia.connection.cursor()
    v_salida3 = instancia.connection.cursor()
    v_salida4 = instancia.connection.cursor()
    id = int(id)  
    
    # Llamar al procedimiento almacenado
    proceso.callproc("SP_ADM_BUSCAR_EVENTO_ID", [id, v_salida5])
    
    # Obtener los resultados
    evento = []
    for row in v_salida5:
        evento.append(row)
    
    proceso.callproc("SP_ADM_EVENTO_PARTICIPANTES", [id, v_salida2])
    # Cerrar los cursores
    participantes = []
    for row in v_salida2:
        participantes.append(row)
        
    proceso.callproc("SP_ADM_LISTAR_USUARIO", [v_salida3])
    # Cerrar los cursores
    usuarios = []
    for row in v_salida3:
        usuarios.append(row)

    participantes_ids = [participante[4] for participante in participantes]
    # Filtrar los usuarios para evitar repeticiones
    usuarios_filtrados = [user for user in usuarios if user[0] not in participantes_ids]

    proceso.callproc("SP_ADM_TIPO_USUARIO", [v_salida4])
    # Cerrar los cursores
    tipos_usuario = []
    for row in v_salida4:
        tipos_usuario.append(row)
        
    proceso.callproc('SP_LISTAR_EVENTOS_USU', [id, v_salida])
    eventos = []
    for row in v_salida:
        eventos.append(row)
        if request.method == 'POST':
            titulo = request.POST.get('txtTitulo')
            descripcion = request.POST.get('txtDesc')
            fechaI = request.POST.get('fechaI')
            fechaF = request.POST.get('fechaF')
            accion = request.POST.get('accion')
            proceso = instancia.connection.cursor()
            
            if accion == 'eliminar':
                participante_id = request.POST.get('participante_id')
                id_evento = request.POST.get('id')
                proceso.callproc('SP_ADM_ELIMINAR_PARTICIPANTE_EVENTO', [id_evento, participante_id])
                return HttpResponse("Participante eliminado exitosamente")
            
            # Validar que no queden espacios en blanco en los campos
            if not titulo.strip() or not descripcion.strip() or not fechaI.strip() or not fechaF.strip():
                messages.error(request, "Por favor, complete todos los campos, no puede enviar campos vacios.")
                contexto = {"eventos": eventos, 'participantes': participantes, 'usuarios': usuarios_filtrados, 'tipos_usuario': tipos_usuario}
                return render(request, "editar_evento.html", contexto)

            # Puedes agregar manejo de errores aquí si es necesario
            proceso.callproc('SP_MODIFICAR_EVENTO', [id, titulo, descripcion, fechaI, fechaF])
            connection.commit()

            if accion == 'agregar_tipo':
                id_tipo = request.POST.get('tipos')
                proceso.callproc('SP_ADM_INSERTAR_PARTICIPANTE', [id, id_tipo])
                messages.success(request, "EXITO")
                return redirect(reverse('EDI_EVE', args=[id]))
            
            if accion == 'agregar':
                id_participante = request.POST.get('usuarios')
                proceso.callproc('SP_ADM_AGREGAR_PARTICIPANTE_EVENTO', [id, id_participante])
                messages.success(request, "EXITO")
                return redirect(reverse('EDI_EVE', args=[id]))

            messages.success(request, "EXITO")
            return redirect(reverse('EDI_EVE', args=[id]))
    v_salida3.close()
    v_salida2.close()
    v_salida.close()
    proceso.close()
    instancia.close()
    contexto ={"eventos": eventos,  'participantes': participantes,  'usuarios': usuarios_filtrados, 'tipos_usuario':tipos_usuario}
    return render(request,"editar_evento.html", contexto)

@login_required(login_url='/cerrar/')
def agregar_parti_evento(request, id):
    mensaje=''
    connection = cx_Oracle.connect("SOCIALDUOC/SOCIALDUOC@//localhost:1521/xe")
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida2 = instancia.connection.cursor()
    v_salida3 = instancia.connection.cursor()
    v_salida4 = instancia.connection.cursor()
    proceso.callproc("SP_ADM_TIPO_USUARIO", [v_salida2])
    # Cerrar los cursores
    tipos_usuario = []
    for row in v_salida2:
        tipos_usuario.append(row)
    
    proceso.callproc("SP_ADM_LISTAR_USUARIO", [v_salida3])
    # Cerrar los cursores
    usuarios = []
    for row in v_salida3:
        usuarios.append(row)
    # Llamar al procedimiento almacenado

    proceso.callproc("SP_LISTAR_EVENTOS", [v_salida4])
    # Obtener los resultados
    evento = []
    for row in v_salida4:
        evento.append(row)
    
    participantes = []
    proceso.callproc("SP_ADM_TODO_EVENTO_PARTICIPANTES", [v_salida2])
    for row in v_salida2:
        participantes.append(row)
    if request.method == 'POST':
        proceso = instancia.connection.cursor()
        accion = request.POST.get('accion')
        if accion == 'agregar':
            id_participante = request.POST.get('usuarios')
            id_evento = request.POST.get('id')
            proceso.callproc('SP_AGREGAR_PARTICIPANTE_EVENTO', [id_evento, id_participante])
            return redirect(reverse('agregar_parti_evento', args=[id_evento]))
        
        if accion == 'agregar_tipo':
            id = request.POST.get('id')
            id_tipo = request.POST.get('tipos')
            proceso.callproc('SP_INSERTAR_PARTICIPANTE', [id, id_tipo])
            return redirect(reverse('agregar_parti_evento', args=[id]))
        
        if accion == 'modificar':
            id = request.POST.get('id')
            nombre = request.POST.get('nombre')
            descrip = request.POST.get('descrip')
            fechainicio = request.POST.get('inicio')
            fechafin = request.POST.get('fin')
            estado = request.POST.get('estado')
            proceso.callproc('SP_ADM_ACTUALIZAR_EVENTO', [id, nombre, descrip, fechainicio, fechafin, estado])
            return redirect(reverse('agregar_parti_evento', args=[id]))
        
    contexto = {"mensaje": mensaje, "tipos_usuario":tipos_usuario,"usuarios":usuarios, "participantes":participantes, "evento":evento}
    return render(request,"agregar_parti_evento.html", contexto)


################# SECCION PERFIL #################
@login_required(login_url='/cerrar/')
def perfil(request, id):
    # Llamada al procedimiento almacenado para eliminar la publicación por su ID.
    user = request.user
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    # Puedes agregar manejo de errores aquí si es necesario
    proceso.callproc('SP_PERFIL_USUARIO', [id, v_salida])
    usuario = []
    for row in v_salida:
        usuario.append(row)
        
    v_salida2 = instancia.connection.cursor()
    proceso.callproc('SP_LISTAR_PUBLICACION_TODO', [user.id, v_salida2])
    publicaciones = []
    for row in v_salida2:
        row_list = list(row)  # Convierte la tupla en una lista
        for i in [7]:  # Process images at indexes 8 and 9
            blob_data = row_list[i]
            if blob_data is not None:
                imagen_bytes = blob_data.read()
                imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                
                if len(imagen_base64) > 0:
                    row_list[i] = imagen_base64
                else:
                    # Handle the case when the image is empty (assign a default image or handle it as needed)
                    row_list[i] = '0'
        # Convierte la lista nuevamente en una tupla y agrégala a la lista de publicaciones
        publicaciones.append(tuple(row_list))
    v_salida3 = instancia.connection.cursor()
    # Llamada al procedimiento almacenado
    proceso.callproc('SP_LISTAR_EVENTOS_TODO', [user.id, v_salida3])
    eventos = []
    for row in v_salida3:
        eventos.append(row)
        
    v_salida4 = instancia.connection.cursor()
    # Llamada al procedimiento almacenado
    proceso.callproc('SP_LISTAR_ENCUESTAS_TODO', [user.id, v_salida4])
    encuestas = []
    for row in v_salida4:
        encuestas.append(row)

    try:
        v_salida5 = instancia.connection.cursor()
        proceso.callproc('SP_LISTAR_IMAGEN_USU', [id, v_salida5])

        # Obtener el resultado del procedimiento almacenado
        result = v_salida5.fetchall()
        proceso.close()

        # Convertir los datos BLOB en objetos bytes y pasarlos a la plantilla
        imagenes_usu = []

        if result:
            for row in result:
                id_usu, blob_data = row
                if blob_data is not None:
                    imagen_bytes = blob_data.read()
                    imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                    # Agregar una validación de tamaño mínimo aquí
                    if len(imagen_base64) > 0:
                        imagenes_usu.append({'id_usu': id_usu, 'imagen_base64': imagen_base64})
                    else:
                        # Si la imagen en base64 está vacía, puedes asignar una imagen predeterminada o manejarla de otra manera.
                        imagenes_usu.append({'id_usu': id_usu, 'imagen_base64': '0'})
        else:
            # Si no hay imágenes de usuario, asigna una imagen predeterminada o maneja la lógica necesaria.
            imagenes_usu.append({'id_usu': None, 'imagen_base64': '0'})

    except Exception as e:
        # Manejo de excepciones, puedes personalizar este bloque según tus necesidades
        return HttpResponse(f"Error: {str(e)}")

    mensaje = "Datos cargados con exito"
    # Redirecciona de nuevo a la página de inicio
    contexto ={"usuario": usuario, "mensaje": mensaje, "publicaciones":publicaciones, "eventos":eventos, "encuestas":encuestas, "imagenes_usu":imagenes_usu}
    return render(request, 'perfil.html' , contexto)

@login_required(login_url='/cerrar/')
def perfilUsuarios(request, id):
    # Conexión a la base de datos Oracle a través de Django 
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    # Puedes agregar manejo de errores aquí si es necesario
    proceso.callproc('SP_PERFIL_USUARIO', [id, v_salida])
    usuario = []
    for row in v_salida:
        usuario.append(row)
    
    v_salida2 = instancia.connection.cursor()
    proceso.callproc('SP_LISTAR_PUBLICACION_BUSQ_USU', [id, v_salida2])
    publicaciones = []
    for row in v_salida2:
        row_list = list(row)  # Convierte la tupla en una lista
        for i in [7]:  # Process images at indexes 8 and 9
            blob_data = row_list[i]
            if blob_data is not None:
                imagen_bytes = blob_data.read()
                imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                
                if len(imagen_base64) > 0:
                    row_list[i] = imagen_base64
                else:
                    # Handle the case when the image is empty (assign a default image or handle it as needed)
                    row_list[i] = '0'
        # Convierte la lista nuevamente en una tupla y agrégala a la lista de publicaciones
        publicaciones.append(tuple(row_list))
        
    v_salida3 = instancia.connection.cursor()
    # Llamada al procedimiento almacenado
    proceso.callproc('SP_LISTAR_EVENTOS_BUSQ_USU', [id, v_salida3])
    eventos = []
    for row in v_salida3:
        eventos.append(row)

    v_salida4 = instancia.connection.cursor()
    # Llamada al procedimiento almacenado
    proceso.callproc('SP_LISTAR_ENCUESTAS_BUSQ_USU', [id, v_salida4])
    encuestas = []
    for row in v_salida4:
        encuestas.append(row)
    try:
        proceso = instancia.connection.cursor()
        v_salida10 = instancia.connection.cursor()
        proceso.callproc('SP_LISTAR_IMAGEN_USU', [id, v_salida10])
        # Obtener el resultado del procedimiento almacenado
        result = v_salida10.fetchall()
        proceso.close()
        # Convertir los datos BLOB en objetos bytes y pasarlos a la plantilla
        imagenes_usu = []
        if result:
            for row in result:
                id_usu, blob_data = row
                if blob_data is not None:
                    imagen_bytes = blob_data.read()
                    imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                    # Agregar una validación de tamaño mínimo aquí
                    if len(imagen_base64) > 0:
                        imagenes_usu.append({'id_usu': id_usu, 'imagen_base64': imagen_base64})
                    else:
                        # Si la imagen en base64 está vacía, puedes asignar una imagen predeterminada o manejarla de otra manera.
                        imagenes_usu.append({'id_usu': id_usu, 'imagen_base64': '0'})
        else:
            # Si no hay imágenes de usuario, asigna una imagen predeterminada o maneja la lógica necesaria.
            imagenes_usu.append({'id_usu': None, 'imagen_base64': '0'})
    except Exception as e:
        # Manejo de excepciones, puedes personalizar este bloque según tus necesidades
        return HttpResponse(f"Error: {str(e)}")
    mensaje = "Datos cargados con exito"
    # Redirecciona de nuevo a la página de inicio
    contexto ={"usuario": usuario, "mensaje": mensaje, "publicaciones":publicaciones, "eventos":eventos, "encuestas":encuestas, "imagenes_usu":imagenes_usu}
    return render(request,"perfil_usuarios.html", contexto)

@login_required(login_url='/cerrar/')
def busqueda_usuarios(request):
    # Conexión a la base de datos Oracle a través de Django 
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    # Llamada al procedimiento almacenado 
    proceso.callproc('SP_buscar_LISTAR_USUARIO', [v_salida])
    usuarios = []

    for row in v_salida:
        row_list = list(row)  # Convierte la tupla en una lista
        blob_data = row_list[9] #ESPECIFICAS EN QUE PARTE DEL ARREGLO VIENE LA IMAGEN
        if blob_data is not None:
            imagen_bytes = blob_data.read()
            imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
            # Modifica la lista para agregar la representación en base64

            if len(imagen_base64) > 0:
                row_list[9] = imagen_base64
            else:
                # Si la imagen en base64 está vacía, puedes asignar una imagen predeterminada o manejarla de otra manera.
                row_list[9] = '0'
        # Convierte la lista nuevamente en una tupla y agrégala a la lista de usuarios
        usuarios.append(tuple(row_list))


    contexto = {"Usuarios": usuarios}
    return render(request, "busqueda_usuarios.html", contexto)

@login_required(login_url='/cerrar/')
def editarPerfil(request, id):
    try:
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida10 = instancia.connection.cursor()
        proceso.callproc('SP_LISTAR_IMAGEN_USU', [id, v_salida10])

        # Obtener el resultado del procedimiento almacenado
        result = v_salida10.fetchall()
        proceso.close()

        # Convertir los datos BLOB en objetos bytes y pasarlos a la plantilla
        imagenes_usu = []
        if result:
            for row in result:
                id_usu, blob_data = row
                if blob_data is not None:
                    imagen_bytes = blob_data.read()
                    imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                    # Agregar una validación de tamaño mínimo aquí
                    if len(imagen_base64) > 0:
                        imagenes_usu.append({'id_usu': id_usu, 'imagen_base64': imagen_base64})
                    else:
                        # Si la imagen en base64 está vacía, puedes asignar una imagen predeterminada o manejarla de otra manera.
                        imagenes_usu.append({'id_usu': id_usu, 'imagen_base64': '0'})
        else:
            # Si no hay imágenes de usuario, asigna una imagen predeterminada o maneja la lógica necesaria.
            imagenes_usu.append({'id_usu': None, 'imagen_base64': '0'})
    except Exception as e:
        # Manejo de excepciones, puedes personalizar este bloque según tus necesidades
        return HttpResponse(f"Error: {str(e)}")
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    proceso.callproc('SP_PERFIL_USUARIO', [id, v_salida])
    usuario = []
    for row in v_salida:
        usuario.append(row)
        if request.method == 'POST':
            imagen_base64 = request.FILES.get('txtImg', None)
            correo = request.POST.get('txtCorreo')
            telefono = request.POST.get('txtTelefono')
            if imagen_base64:
                try:
                    contenido_imagen = imagen_base64.read()
                    proceso = instancia.connection.cursor()
                    # Puedes agregar manejo de errores aquí si es necesario
                    proceso.callproc('SP_ACTUALIZAR_IMAGEN_USU', [id, contenido_imagen])
                    messages.success(request, "EXITO")
                    return redirect(reverse('EDI_PER', args=[id]))
                    connection.commit()
                except Exception as e: 
                    messages.error(request, "Error: ",  {'error': str(e)})
                    return redirect(reverse('EDI_PER', args=[id]))
            # Llamada al procedimiento almacenado para eliminar la publicación por su ID
            proceso = instancia.connection.cursor()
            # Puedes agregar manejo de errores aquí si es necesario
            try:
                telefono = int(telefono)
            except ValueError:
                messages.error(request, "El número de teléfono debe ser un valor numérico.")
                return redirect(reverse('EDI_PER', args=[id]))
            
            if not correo.strip():
                    messages.error(request, "Por favor, complete todos los campos, no puede enviar campos vacíos.")
                    return redirect(reverse('EDI_PER', args=[id]))
            
            proceso.callproc('SP_MODIFICAR_PERFIL_USUARIO', [id, correo, telefono])
            messages.success(request, "EXITO")
            return redirect(reverse('EDI_PER', args=[id]))

                # Llamada al procedimiento almacenado para eliminar la publicación por su ID
    contexto ={"usuario": usuario, "imagenes_usu":imagenes_usu}
    return render(request,"editar_perfil.html", contexto)



################# SECCION ADMIN #################
from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse
import csv

@login_required(login_url='/cerrar/')
def archivar_usuario(request):
    if request.user.is_superuser == 1:
        try:
            if request.method == 'POST':
                id_usuario = request.POST['id_usuario']
                accion = request.POST.get('accion')  # Obtiene el valor de "accion"
                instancia = connection.cursor()
                proceso = instancia.connection.cursor()
                if accion == 'modificar':
                    # Llamada al procedimiento almacenado para eliminar al usuario por su ID
                    proceso.callproc('sp_adm_eliminar_usuario', [id_usuario])
                    success = f'MODIFICADO'
                    return HttpResponse(success)
        except:
            success = f'El error'
            return HttpResponse(success)
    else:
        return redirect('404')
    
@login_required(login_url='/cerrar/')
def adminUsuarios(request):
    if request.user.is_superuser == 1:
        # Conexión a la base de datos Oracle a través de Django 
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida = instancia.connection.cursor()
        # Llamada al procedimiento almacenado 
        proceso.callproc('sp_adm_listar_usuario', [v_salida])
        usuarios = []
        for row in v_salida:
            row_list = list(row)  # Convierte la tupla en una lista
            blob_data = row_list[8] #ESPECIFICAS EN QUE PARTE DEL ARREGLO VIENE LA IMAGEN
            if blob_data is not None:
                imagen_bytes = blob_data.read()
                imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                # Modifica la lista para agregar la representación en base64

                if len(imagen_base64) > 0:
                    row_list[8]=(imagen_base64)
                else:
                    # Si la imagen en base64 está vacía, puedes asignar una imagen predeterminada o manejarla de otra manera.
                    row_list[8]=('0')
            # Convierte la lista nuevamente en una tupla y agrégala a la lista de usuarios
            usuarios.append(tuple(row_list))
            
        contexto = {"Usuarios": usuarios}
        return render(request, "admin_usuarios.html", contexto)
    else:
        return redirect('404')

@login_required(login_url='/cerrar/')
def archivar_publicacion(request):
    if request.user.is_superuser == 1:
        try:
            if request.method == 'POST':
                id_usuario = request.POST['id_usuario']
                accion = request.POST.get('accion')  # Obtiene el valor de "accion"
                instancia = connection.cursor()
                proceso = instancia.connection.cursor()
                v_salida = instancia.connection.cursor()
                if accion == 'modificar':
                    # Llamada al procedimiento almacenado para eliminar al usuario por su ID
                    proceso.callproc('SP_ADM_ARCHIVAR_PUBLICACION', [id_usuario, v_salida])
                    success = f'MODIFICADO'
                    estado = []
                    for row in v_salida:
                        estado.append(row)
                    if estado ==  ( [(1,)] ) :
                        thread = threading.Thread(target=enviar_notificacion)
                        thread.start()
                    return HttpResponse(success)
                if accion == 'eliminar':
                    # Llamada al procedimiento almacenado para eliminar al usuario por su ID
                    proceso.callproc('ELIMINAR_PUBLICACION', [id_usuario])
                    success = f'ELIMINADO'
                    return HttpResponse(success)
        except:
            success = f'El error'
            return HttpResponse(success)
    else:
        return redirect('404')

@login_required(login_url='/cerrar/')
def adminPublicaciones(request):
    if request.user.is_superuser == 1:
        # Conexión a la base de datos Oracle a través de Django 
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida = instancia.connection.cursor()
        v_salida2 = instancia.connection.cursor()
        # Llamada al procedimiento almacenado 
        proceso.callproc('SP_ADM_LISTAR_PUBLICACION', [v_salida])
        publicaciones = []
        for row in v_salida:
            row_list = list(row)  # Convierte la tupla en una lista
            blob_data = row_list[7] #ESPECIFICAS EN QUE PARTE DEL ARREGLO VIENE LA IMAGEN
            if blob_data is not None:
                imagen_bytes = blob_data.read()
                imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                # Modifica la lista para agregar la representación en base64

                if len(imagen_base64) > 0:
                    row_list[7]=(imagen_base64)
                else:
                    # Si la imagen en base64 está vacía, puedes asignar una imagen predeterminada o manejarla de otra manera.
                    row_list[7]=('0')
            # Convierte la lista nuevamente en una tupla y agrégala a la lista de usuarios
            publicaciones.append(tuple(row_list))

            
        proceso.callproc('SP_ADM_TODA_PUBLICACION_COMENTARIOS', [v_salida2])
        comentarios = []
        for row in v_salida2:
            row_list = list(row)  # Convierte la tupla en una lista
            blob_data = row_list[6] #ESPECIFICAS EN QUE PARTE DEL ARREGLO VIENE LA IMAGEN
            if blob_data is not None:
                imagen_bytes = blob_data.read()
                imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                # Modifica la lista para agregar la representación en base64

                if len(imagen_base64) > 0:
                    row_list[6]=(imagen_base64)
                else:
                    # Si la imagen en base64 está vacía, puedes asignar una imagen predeterminada o manejarla de otra manera.
                    row_list[6]=('0')
            # Convierte la lista nuevamente en una tupla y agrégala a la lista de usuarios
            comentarios.append(tuple(row_list))


        contexto = {"publicaciones": publicaciones, "comentarios":comentarios}
        return render(request,"admin_publicaciones.html", contexto)
    else:
        return redirect('404')

@login_required(login_url='/cerrar/')
def adminEventos(request):
    if request.user.is_superuser == 1:
        # Conexión a la base de datos Oracle a través de Django 
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida = instancia.connection.cursor()
        v_salida2 = instancia.connection.cursor()
        # Llamada al procedimiento almacenado 
        proceso.callproc('SP_ADM_LISTAR_EVENTO', [v_salida])
        eventos = []
        for row in v_salida:
            eventos.append(row)
            
        participantes = []
        proceso.callproc("SP_ADM_TODO_EVENTO_PARTICIPANTES", [v_salida2])
        for row in v_salida2:
            participantes.append(row)


        
        contexto = {"eventos": eventos, "participantes":participantes}
        return render(request,"admin_eventos.html", contexto)
    else:
        return redirect('404')

@login_required(login_url='/cerrar/')
def archivar_evento(request):
    if request.user.is_superuser == 1:
        try:
            if request.method == 'POST':
                id_evento = request.POST['id_evento']
                accion = request.POST.get('accion') 
                instancia = connection.cursor()
                proceso = instancia.connection.cursor()
                v_salida = instancia.connection.cursor()
                if accion == 'modificar':
                    # Llamada al procedimiento almacenado para eliminar al usuario por su ID
                    proceso.callproc('SP_ADM_ARCHIVAR_EVENTO', [id_evento , v_salida])
                    success = f'MODIFICADO'
                    estado = []
                    for row in v_salida:
                        estado.append(row)
                    print(estado)
                    if estado ==  ( [(1,)] ) :
                        thread = threading.Thread(target=enviar_notificacion)
                        thread.start()
                    return HttpResponse(success)
                if accion == 'eliminar':
                    # Llamada al procedimiento almacenado para eliminar al usuario por su ID
                    proceso.callproc('SP_ELIMINAR_EVENTO', [id_evento])
                    success = f'ELIMINADO'
                    return HttpResponse(success)  
        except:
            success = f'El error'
            return HttpResponse(success)
    else:
        return redirect('404')

@login_required(login_url='/cerrar/')
def adminEncuestas(request):
    if request.user.is_superuser == 1:
        # Conexión a la base de datos Oracle a través de Django 
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida = instancia.connection.cursor()
        v_salida2 = instancia.connection.cursor()
        # Llamada al procedimiento almacenado 
        proceso.callproc('SP_ADM_LISTAR_ENCUESTA', [v_salida])
        encuestas = []
        for row in v_salida:
            encuestas.append(row)
        
        respuestas = []
        proceso.callproc("SP_ADM_TODA_ENCUESTA_RESPUESTAS", [v_salida2])
        for row in v_salida2:
            row_list = list(row)  # Convierte la tupla en una lista
            blob_data = row_list[6] #ESPECIFICAS EN QUE PARTE DEL ARREGLO VIENE LA IMAGEN
            if blob_data is not None:
                imagen_bytes = blob_data.read()
                imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                # Modifica la lista para agregar la representación en base64

                if len(imagen_base64) > 0:
                    row_list[6]=(imagen_base64)
                else:
                    # Si la imagen en base64 está vacía, puedes asignar una imagen predeterminada o manejarla de otra manera.
                    row_list[6]=('0')
            # Convierte la lista nuevamente en una tupla y agrégala a la lista de usuarios
            respuestas.append(tuple(row_list))
        

        contexto = {"encuestas": encuestas, "respuestas":respuestas}
        return render(request,"admin_encuestas.html", contexto)
    else:
        return redirect('404')

@login_required(login_url='/cerrar/')
def archivar_encuesta(request):
    if request.user.is_superuser == 1:
        try:
            if request.method == 'POST':
                id_encuesta = request.POST['id_encuesta']
                accion = request.POST.get('accion') 
                instancia = connection.cursor()
                proceso = instancia.connection.cursor()
                v_salida = instancia.connection.cursor()
                if accion == 'modificar':
                    # Llamada al procedimiento almacenado para eliminar al usuario por su ID
                    proceso.callproc('SP_ADM_ARCHIVAR_ENCUESTA', [id_encuesta, v_salida])
                    success = f'MODIFICADO'
                    estado = []
                    for row in v_salida:
                        estado.append(row)
                    print(estado)
                    if estado ==  ( [(1,)] ) :
                        thread = threading.Thread(target=enviar_notificacion)
                        thread.start()
                    return HttpResponse(success)
                if accion == 'eliminar':
                    # Llamada al procedimiento almacenado para eliminar al usuario por su ID
                    proceso.callproc('SP_ELIMINAR_ENCUESTA', [id_encuesta])
                    success = f'ELIMINADO'
                    return HttpResponse(success)  
                if accion == 'grafico':
                    print('grafico')
                    v_salida = instancia.connection.cursor()
                    proceso.callproc('sp_grafico_encuesta', [id_encuesta, v_salida])
                    respuestas = []
                    for row in v_salida:
                        respuesta = {
                            'id_encu': row[0],
                            'resuesta_uno': row[1],
                            'resuesta_dos': row[2],
                            'respuestas_otras': row[3],
                        }
                        respuestas.append(respuesta)
                    success = f'ELIMINADO'
                    print(respuestas)
                    return HttpResponse(success)
                
        except:
            success = f'El error'
            return HttpResponse(success)
    else:
        return redirect('404')

@login_required(login_url='/cerrar/')
def mod_actualizar_usuario(request):
    if request.user.is_superuser == 1:
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        if request.method == 'POST':
            accion = request.POST.get('accion')
            if accion == 'modificar':
                id = request.POST.get('id')
                nombre = request.POST.get('nombre')
                ap_paterno = request.POST.get('ap_paterno')
                ap_materno = request.POST.get('ap_materno')
                correo_personal = request.POST.get('correo_personal')
                telefono = request.POST.get('telefono')
                comuna = request.POST.get('comuna')
                genero = request.POST.get('genero')
                estado = request.POST.get('estado', 2)
                tipo = request.POST.get('tipo')
                sede = request.POST.get('sede')
                
                try:
                    telefono = int(telefono)
                except ValueError:
                    # Handle the case where telefono is not a valid integer
                    messages.error(request, "El número de teléfono debe ser un valor numérico.")
                    return redirect(reverse('adm_modificar_usuario', args=[id]))
                
                if not all([
                    nombre and nombre.strip(),
                    ap_paterno and ap_paterno.strip(),
                    ap_materno and ap_materno.strip(),
                    correo_personal and correo_personal.strip(),
                    telefono and str(telefono).strip(),
                    comuna and comuna.strip(),
                    genero and genero.strip(),
                    tipo and tipo.strip(),
                    sede and sede.strip()
                ]):
                    messages.error(request, "Por favor, complete todos los campos, no puede enviar campos vacíos.")
                    return redirect(reverse('adm_modificar_usuario', args=[id]))

                proceso.callproc('SP_ADM_ACTUALIZAR_USUARIO', [nombre, ap_paterno, ap_materno, correo_personal, telefono, comuna, genero, estado, tipo, sede, id])
                messages.success(request, "EXITO")
                return redirect(reverse('adm_modificar_usuario', args=[id]))
            
            if accion == 'eliminar_foto':
                id = request.POST.get('id')
                proceso.callproc('SP_ADM_ELIMINAR_FOTO_USUARIO', [id])
                messages.success(request, "EXITO")
                return redirect(reverse('adm_modificar_usuario', args=[id]))
    else:
        return redirect('404')

@login_required(login_url='/cerrar/')    
def modUsuario(request, id):
    if request.user.is_superuser == 1:
        # Crear los cursores
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida = instancia.connection.cursor()
        v_salida2 = instancia.connection.cursor()
        v_salida3 = instancia.connection.cursor()
        v_salida4 = instancia.connection.cursor()
        v_salida5 = instancia.connection.cursor()
        id = int(id)    
        
        # Llamar al procedimiento almacenado
        proceso.callproc("SP_ADM_BUSCAR_USUARIO_ID", [id, v_salida])
        
        # Obtener los resultados
        usuarios = []
        for row in v_salida:
            row_list = list(row)  # Convierte la tupla en una lista
            blob_data = row_list[18] #ESPECIFICAS EN QUE PARTE DEL ARREGLO VIENE LA IMAGEN
            if blob_data is not None:
                imagen_bytes = blob_data.read()
                imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                # Modifica la lista para agregar la representación en base64

                if len(imagen_base64) > 0:
                    row_list[18]=(imagen_base64)
                else:
                    # Si la imagen en base64 está vacía, puedes asignar una imagen predeterminada o manejarla de otra manera.
                    row_list[18]=('0')
            # Convierte la lista nuevamente en una tupla y agrégala a la lista de usuarios
            usuarios.append(tuple(row_list))
        
        proceso.callproc("SP_ADM_TIPO_USUARIO", [v_salida2])
        # Cerrar los cursores
        tipos_usuario = []
        for row in v_salida2:
            tipos_usuario.append(row)
            
        proceso.callproc("SP_ADM_SEDE", [v_salida3])
        # Cerrar los cursores
        sedes = []
        for row in v_salida3:
            sedes.append(row)
            
        proceso.callproc("SP_ADM_GENERO", [v_salida4])
        # Cerrar los cursores
        generos = []
        for row in v_salida4:
            generos.append(row)
            
        proceso.callproc("SP_ADM_COMUNA", [v_salida5])
        # Cerrar los cursores
        comunas = []
        for row in v_salida5:
            comunas.append(row)

        proceso.close()
        instancia.close()
        
        # Renderizar la plantilla HTML con los datos de usuario
        return render(request, 'a_modificar_usuario.html', {'usuario': usuarios, 'tipos_usuario': tipos_usuario, 'sedes':sedes, 'generos':generos, 'comunas': comunas})
    else:
        return redirect('404')

@login_required(login_url='/cerrar/') 
def mod_actualizar_publicacion(request):
    if request.user.is_superuser == 1:
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        if request.method == 'POST':
            id = request.POST.get('id')
            descrip = request.POST.get('descrip')
            estado = request.POST.get('estado', 2)
            imagen_base64 = request.FILES.get('txtImg', None)
            nueva_sede = request.POST.get('cboSede', None)
            if imagen_base64:
                try:
                    contenido_imagen = imagen_base64.read()
                    proceso = instancia.connection.cursor()
                    proceso.callproc('SP_ACTUALIZAR_IMAGEN', [id, contenido_imagen])
                    connection.commit()
                except Exception as e:
                    messages.error(request, "ERROR AL PROCESAR LA FOTO")
                    return JsonResponse({'error': str(e)})
                   
            if not id or not descrip.strip():
                messages.error(request, "Por favor, complete todos los campos, no puede enviar campos vacios.")
                return redirect(reverse('adm_modificar_publicacion', args=[id]))
            try:
                instancia = connection.cursor()
                proceso = instancia.connection.cursor()
                proceso.callproc('SP_ADM_ACTUALIZAR_PUBLICACION', [id, descrip, estado, nueva_sede])
                connection.commit()
                messages.success(request, "EXITO")
            except Exception as e:
                return JsonResponse({'error': str(e)})
            return redirect(reverse('adm_modificar_publicacion', args=[id]))
    else:
        return redirect('404')
    
@login_required(login_url='/cerrar/')
def modPublicacion(request, id):
    if request.user.is_superuser == 1:
        # Crear los cursores
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida = instancia.connection.cursor()
        v_salida2 = instancia.connection.cursor()
        v_salida3 = instancia.connection.cursor()
        id = int(id)  
        
        # Llamar al procedimiento almacenado
        proceso.callproc("SP_ADM_BUSCAR_PUBLICACION_ID", [id, v_salida])
        
        # Obtener los resultados
        publicacion = []
        for row in v_salida:
            row_list = list(row)  # Convierte la tupla en una lista
            blob_data = row_list[8] #ESPECIFICAS EN QUE PARTE DEL ARREGLO VIENE LA IMAGEN
            if blob_data is not None:
                imagen_bytes = blob_data.read()
                imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                # Modifica la lista para agregar la representación en base64

                if len(imagen_base64) > 0:
                    row_list[8]=(imagen_base64)
                else:
                    # Si la imagen en base64 está vacía, puedes asignar una imagen predeterminada o manejarla de otra manera.
                    row_list[8]=('0')
            # Convierte la lista nuevamente en una tupla y agrégala a la lista de usuarios
            publicacion.append(tuple(row_list))
        
        proceso.callproc("SP_ADM_TIPO_USUARIO", [v_salida2])
        # Cerrar los cursores
        tipos_usuario = []
        for row in v_salida2:
            tipos_usuario.append(row)
            
        proceso.callproc("SP_ADM_SEDE", [v_salida3])
        # Cerrar los cursores
        sedes = []
        for row in v_salida3:
            sedes.append(row)

        v_salida2.close()
        v_salida.close()
        proceso.close()
        instancia.close()
        
        # Renderizar la plantilla HTML con los datos de usuario
        return render(request, 'a_modificar_publicacion.html', {'publicacion': publicacion,  'tipos_usuario': tipos_usuario, 'sedes':sedes})
    else:
        return redirect('404')

@login_required(login_url='/cerrar/')
def modEvento(request, id):
    if request.user.is_superuser == 1:
        # Crear los cursores
        # Crear los cursores
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida = instancia.connection.cursor()
        v_salida2 = instancia.connection.cursor()
        v_salida3 = instancia.connection.cursor()
        v_salida4 = instancia.connection.cursor()
        id = int(id)  
        
        # Llamar al procedimiento almacenado
        proceso.callproc("SP_ADM_BUSCAR_EVENTO_ID", [id, v_salida])
        
        # Obtener los resultados
        evento = []
        for row in v_salida:
            evento.append(row)
        
        proceso.callproc("SP_ADM_EVENTO_PARTICIPANTES", [id, v_salida2])
        # Cerrar los cursores
        participantes = []
        for row in v_salida2:
            participantes.append(row)
            
        proceso.callproc("SP_ADM_LISTAR_USUARIO", [v_salida3])
        # Cerrar los cursores
        usuarios = []
        for row in v_salida3:
            usuarios.append(row)

        participantes_ids = [participante[4] for participante in participantes]
        # Filtrar los usuarios para evitar repeticiones
        usuarios_filtrados = [user for user in usuarios if user[0] not in participantes_ids]

        proceso.callproc("SP_ADM_TIPO_USUARIO", [v_salida4])
        # Cerrar los cursores
        tipos_usuario = []
        for row in v_salida4:
            tipos_usuario.append(row)
            
        v_salida3.close()
        v_salida2.close()
        v_salida.close()
        proceso.close()
        instancia.close()
        
        # Renderizar la plantilla HTML con los datos de usuario
        return render(request, 'a_modificar_evento.html', {'evento': evento,  'participantes': participantes,  'usuarios': usuarios_filtrados, 'tipos_usuario':tipos_usuario})

    else:
        return redirect('404')

@login_required(login_url='/cerrar/')
def mod_actualizar_evento(request):
    if request.user.is_superuser == 1:
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        if request.method == 'POST':
            accion = request.POST.get('accion')
            if accion == 'agregar':
                id_participante = request.POST.get('usuarios')
                id_evento = request.POST.get('id')
                proceso.callproc('SP_ADM_AGREGAR_PARTICIPANTE_EVENTO', [id_evento, id_participante])
                messages.success(request, "EXITO")
                return redirect(reverse('adm_modificar_evento', args=[id_evento]))
            
            if accion == 'agregar_tipo':
                id = request.POST.get('id')
                id_tipo = request.POST.get('tipos')
                proceso.callproc('SP_ADM_INSERTAR_PARTICIPANTE', [id, id_tipo])
                messages.success(request, "EXITO")
                return redirect(reverse('adm_modificar_evento', args=[id]))
           
            
            if accion == 'modificar':
                id = request.POST.get('id')
                nombre = request.POST.get('nombre')
                descrip = request.POST.get('descrip')
                fechainicio = request.POST.get('inicio')
                fechafin = request.POST.get('fin')
                estado = request.POST.get('estado', 2)

                # Validar que no queden espacios en blanco en los campos obligatorios
                if not nombre.strip() or not descrip.strip() or not fechainicio or not fechafin:
                    messages.error(request, "Por favor, complete todos los campos, no puede enviar campos vacíos.")
                    return redirect(reverse('adm_modificar_evento', args=[id]))
                
               
                proceso.callproc('SP_ADM_ACTUALIZAR_EVENTO', [id, nombre, descrip, fechainicio, fechafin, estado])
                messages.success(request, "EXITO")
                return redirect(reverse('adm_modificar_evento', args=[id]))
            
            if accion == 'eliminar':
                participante_id = request.POST.get('participante_id')
                id_evento = request.POST.get('id')
                proceso.callproc('SP_ADM_ELIMINAR_PARTICIPANTE_EVENTO', [id_evento, participante_id])
                return HttpResponse("Participante eliminado exitosamente")
                
        return redirect('404')

@login_required(login_url='/cerrar/')
def modEncuesta(request, id):
    if request.user.is_superuser == 1:
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        v_salida = instancia.connection.cursor()
        v_salida2 = instancia.connection.cursor()
        id = int(id)  
        
        # Llamar al procedimiento almacenado
        proceso.callproc("SP_ADM_BUSCAR_ENCUESTA_ID", [id, v_salida])
        
        # Obtener los resultados
        encuesta = []
        for row in v_salida:
            encuesta.append(row)

        # Llamar al procedimiento almacenado
        proceso.callproc("SP_ADM_RESPUESTAS_POR_ID_ENCUESTA", [id, v_salida2])
        
        # Obtener los resultados
        respuestas = []
        for row in v_salida2:
            respuestas.append(row)
            
        v_salida.close()
        proceso.close()
        instancia.close()
        return render(request,"a_modificar_encuesta.html", {'encuesta': encuesta, 'respuestas': respuestas})
    else:
        return redirect('404')

@login_required(login_url='/cerrar/')
def mod_actualizar_encuesta(request):
    if request.user.is_superuser == 1:
        instancia = connection.cursor()
        proceso = instancia.connection.cursor()
        if request.method == 'POST':
            accion = request.POST.get('accion')
            if accion == 'modificar':
                id = request.POST.get('id')
                titulo = request.POST.get('titulo')
                descrip = request.POST.get('descrip')
                link = request.POST.get('link')
                fechainicio = request.POST.get('inicio')
                fechafin = request.POST.get('fin')
                estado = request.POST.get('estado', 2)
                pregunta = request.POST.get('pregunta')
                respuesta_uno = request.POST.get('respuesta_uno')
                respuesta_dos = request.POST.get('respuesta_dos')
                
                # Validar que no queden espacios en blanco en los campos excepto "link" y "descripcion"
                if not (titulo.strip() and fechainicio.strip() and fechafin.strip() and pregunta.strip() and descrip.strip() and respuesta_uno.strip()  and respuesta_dos.strip() ):
                    messages.error(request, "Por favor, complete todos los campos, no puede enviar campos vacíos.")
                    return redirect(reverse('adm_modificar_encuesta', args=[id]))
                
                proceso.callproc('SP_ADM_ACTUALIZAR_ENCUESTA', [id, titulo, descrip, link, fechainicio, fechafin, estado, pregunta, respuesta_uno,respuesta_dos])
                messages.success(request, "EXITO")
                return redirect(reverse('adm_modificar_encuesta', args=[id]))
    else:
        return redirect('404')

@login_required(login_url='/cerrar/')
def adminDashboard(request):
    if request.user.is_superuser == 1:
        instancia = connection.cursor()
        proceso_carreras = instancia.connection.cursor()
        proceso_publicaciones = instancia.connection.cursor()
        proceso_encuestas = instancia.connection.cursor()
        proceso_eventos = instancia.connection.cursor()
        v_salida_carreras = instancia.connection.cursor()
        v_salida_publicaciones = instancia.connection.cursor()
        v_salida_encuestas= instancia.connection.cursor()
        v_salida_eventos= instancia.connection.cursor()
        v_salida_ultimas_publicaciones = instancia.connection.cursor()
        v_salida_ultimas_encuestas = instancia.connection.cursor()
        v_salida_ultimas_eventos = instancia.connection.cursor()

        # Llamar al procedimiento almacenado para contar carreras de alumnos con el valor de salida
        proceso_carreras.callproc('SP_contar_carreras_alumnos', [v_salida_carreras])
        # Obtener los resultados del procedimiento almacenado para carreras de alumnos
        v_salida_carreras_result = v_salida_carreras.fetchall()
        # Crear una lista de resultados de carreras en formato JSON
        carreras_data = [{'count': row[0], 'nombre': row[1]} for row in v_salida_carreras_result]

        # Llamar al procedimiento almacenado para contar publicaciones en la semana con el valor de salida
        proceso_publicaciones.callproc('SP_contar_publicaciones_semana', [v_salida_publicaciones])
        # Obtener los resultados del procedimiento almacenado para publicaciones en la semana
        v_salida_publicaciones_result = v_salida_publicaciones.fetchall()
        # Crear una lista de resultados de publicaciones en la semana en formato JSON
        publicaciones_semana_data = [{'InicioSemana': row[0], 'FinSemana': row[1], 'NúmeroPublicaciones': row[2]} for row in v_salida_publicaciones_result]


        # Llamar al procedimiento almacenado para contar publicaciones en la semana con el valor de salida
        proceso_encuestas.callproc('SP_contar_encuestas_semana', [v_salida_encuestas])
        # Obtener los resultados del procedimiento almacenado para publicaciones en la semana
        v_salida_encuestas_result = v_salida_encuestas.fetchall()
        # Crear una lista de resultados de publicaciones en la semana en formato JSON
        encuestas_semana_data = [{'InicioSemana': row[0], 'FinSemana': row[1], 'NúmeroEncuestas': row[2]} for row in v_salida_encuestas_result]


        # Llamar al procedimiento almacenado para contar publicaciones en la semana con el valor de salida
        proceso_eventos.callproc('SP_contar_eventos_semana', [v_salida_eventos])
        # Obtener los resultados del procedimiento almacenado para publicaciones en la semana
        v_salida_eventos_result = v_salida_eventos.fetchall()
        # Crear una lista de resultados de publicaciones en la semana en formato JSON
        eventos_semana_data = [{'InicioSemana': row[0], 'FinSemana': row[1], 'NúmeroEventos': row[2]} for row in v_salida_eventos_result]


        # Llamar al procedimiento almacenado para contar publicaciones en la semana con el valor de salida
        proceso_publicaciones.callproc('SP_obtener_ultima_semana_y_dia', [v_salida_ultimas_publicaciones])
        # Obtener los resultados del procedimiento almacenado para publicaciones en la semana
        v_salida_ultimas_publicaciones_result = v_salida_ultimas_publicaciones.fetchall()
        # Crear una lista de resultados de publicaciones en la semana en formato JSON
        Ultimas_publicaciones_semana_data = [{'Fecha': row[0], 'Dia': row[1], 'NúmeroPublicaciones': row[2]} for row in v_salida_ultimas_publicaciones_result]



        # Llamar al procedimiento almacenado para contar publicaciones en la semana con el valor de salida
        proceso_encuestas.callproc('SP_obtener_ultima_semana_y_diaE', [v_salida_ultimas_encuestas])
        # Obtener los resultados del procedimiento almacenado para publicaciones en la semana
        v_salida_ultimas_encuestas_result = v_salida_ultimas_encuestas.fetchall()
        # Crear una lista de resultados de publicaciones en la semana en formato JSON
        Ultimas_encuestas_semana_data = [{'Fecha': row[0], 'Dia': row[1], 'NúmeroEncuestas': row[2]} for row in v_salida_ultimas_encuestas_result]



        # Llamar al procedimiento almacenado para contar publicaciones en la semana con el valor de salida
        proceso_eventos.callproc('SP_obtener_ultima_semana_y_diaEv', [v_salida_ultimas_eventos])
        # Obtener los resultados del procedimiento almacenado para publicaciones en la semana
        v_salida_ultimas_eventos_result = v_salida_ultimas_eventos.fetchall()
        # Crear una lista de resultados de publicaciones en la semana en formato JSON
        Ultimas_eventos_semana_data = [{'Fecha': row[0], 'Dia': row[1], 'NúmeroEventos': row[2]} for row in v_salida_ultimas_eventos_result]



        # Devolver los resultados de carreras y publicaciones en la semana como una respuesta JSON
        return render(request, "dashboard.html", {'carreras_data': carreras_data, 'publicaciones_semana_data': publicaciones_semana_data, "encuestas_semana_data":encuestas_semana_data, "eventos_semana_data":eventos_semana_data, 'Ultimas_publicaciones_semana_data': Ultimas_publicaciones_semana_data, "Ultimas_encuestas_semana_data":Ultimas_encuestas_semana_data, "Ultimas_eventos_semana_data":Ultimas_eventos_semana_data})
    else:
        return redirect('404')

def secciones(request):
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    v_salida2 = instancia.connection.cursor()
    v_salida3 = instancia.connection.cursor()
    
    proceso.callproc("SP_LISTAR_CARRERAS", [v_salida])
    carreras = []
    for row in v_salida:
        carrera = {
            'id_carrera': row[0],
            'nombre': row[1],
        }
        carreras.append(carrera)
        
    proceso.callproc("SP_LISTAR_SECCION", [v_salida2])
    secciones = []
    for row in v_salida2:
        seccion = {
            'id_seccion': row[0],
            'nombre': row[1],
            'id_ramo': row[2],
            'nombre_ramo': row[3],
            'id_carrera': row[4],
        }
        secciones.append(seccion)
        
    proceso.callproc("SP_LISTAR_RAMOS", [v_salida3])
    ramos = []
    for row in v_salida3:
        ramo = {
            'id_ramo': row[0],
            'nombre': row[1],
            'id_carrera': row[2]
        }
        ramos.append(ramo)
    
    return render(request, "secciones.html" , {'carreras': carreras, 'secciones': secciones, 'ramos':ramos})

def seccion_modificar(request, id):
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    v_salida2 = instancia.connection.cursor()
    v_salida3 = instancia.connection.cursor()
        
    proceso.callproc("SP_BUSCAR_SECCION_ID", [id, v_salida])
    secciones = []
    for row in v_salida:
        seccion = {
            'id_seccion': row[0],
            'nombre': row[1],
            'id_ramo': row[2],
            'nombre_ramo': row[3],
            'id_carrera': row[4],
        }
        secciones.append(seccion)
    
    proceso.callproc("SP_LISTAR_AGREGAR_SECCION", [id, v_salida2])
    usuarios = []
    for row in v_salida2:
        usuario = {
            'id_usuario': row[0],
            'Correo': row[1],
            'Nombre': row[2],
        }
        usuarios.append(usuario)
        
        
    proceso.callproc("SP_LISTAR_USUARIOS_SECCION_ID", [id, v_salida3])
    usuarios_registrados = []
    for row in v_salida3:
        usuario_registrado = {
            'id_usuario': row[0],
            'nombre': row[1],
            'foto': row[2],
            'correo': row[3],
            'seccion': row[4],
        }
        
        blob_data = row[2]  # ESPECIFICAS EN QUE PARTE DEL ARREGLO VIENE LA IMAGEN

        if blob_data is not None:
            imagen_bytes = blob_data.read()
            imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
            usuario_registrado['foto'] = imagen_base64 if len(imagen_base64) > 0 else '0'
        else:
            # Si blob_data es None, puedes asignar una imagen predeterminada o manejarla de otra manera.
            usuario_registrado['foto'] = '0'

        usuarios_registrados.append(usuario_registrado)
    
    return render(request, "seccion_modificar.html" , {'seccion': secciones, "usuarios": usuarios, "usuarios_registrados": usuarios_registrados})

def agregar_usuario_seccion(request):
    if request.method == 'POST':
        id_usuario = request.POST.get('id_usuario')
        id_seccion = request.POST.get('id_seccion')
        # Elimina espacios en blanco al inicio y al final del comentario
        try:
            instancia = connection.cursor()
            proceso = instancia.connection.cursor()
            v_salida = instancia.connection.cursor()
            # Ejecuta el procedimiento almacenado SP_AGREGAR_COMENTARIO
            proceso.callproc("SP_AGREGAR_USUARIO_SECCION", [id_seccion ,  id_usuario])
            #proceso.callproc("SP_AGREGAR_USUARIO_SECCION", [id_usuario ,  id_seccion]) error forzado para probar
            connection.commit()
            proceso.callproc('SP_LISTAR_USUARIOS_SECCION_ID', [id_seccion, v_salida])
            usuarios_registrados = []
            for row in v_salida:
                usuario_registrado = {
                    'id_usuario': row[0],
                    'nombre': row[1],
                    'foto': row[2],
                    'correo': row[3],
                    'seccion': row[4],
                }
                
                blob_data = row[2]  # ESPECIFICAS EN QUE PARTE DEL ARREGLO VIENE LA IMAGEN

                if blob_data is not None:
                    imagen_bytes = blob_data.read()
                    imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
                    usuario_registrado['foto'] = imagen_base64 if len(imagen_base64) > 0 else '0'
                else:
                    # Si blob_data es None, puedes asignar una imagen predeterminada o manejarla de otra manera.
                    usuario_registrado['foto'] = '0'

                usuarios_registrados.append(usuario_registrado)
            return JsonResponse({'success': 'EXITO','usuarios_registrados': usuarios_registrados})
            
        except cx_Oracle.Error as error:
                # Maneja el error de manera apropiada
                print("Error al ejecutar el procedimiento almacenado:", error)
                connection.rollback()
        success = ('ERROR')
    return JsonResponse(success)

def eliminar_usuario_seccion(request):
    if request.method == 'POST':
        id_usuario = request.POST.get('id_usuario')
        id_seccion = request.POST.get('id_seccion')
        try:
            instancia = connection.cursor()
            proceso = instancia.connection.cursor()
            #proceso.callproc('SP_ELIMINAR_USUARIO_SECCION', [id_usuario]) error forzado para probar
            proceso.callproc('SP_ELIMINAR_USUARIO_SECCION', [id_seccion, id_usuario])
            mensaje = "Usuario eliminado con exito"
            return JsonResponse({'success': 'EXITO', "mensaje": mensaje})
        except cx_Oracle.Error as error:
                # Maneja el error de manera apropiada
                print("Error al ejecutar el procedimiento almacenado:", error)
                connection.rollback()
        success = ('ERROR')
    return JsonResponse(success)

def seccion_crear(request):
    instancia = connection.cursor()
    proceso = instancia.connection.cursor()
    v_salida = instancia.connection.cursor()
    v_salida2 = instancia.connection.cursor()

    
    proceso.callproc("SP_LISTAR_CARRERAS", [v_salida])
    carreras = []
    for row in v_salida:
        carrera = {
            'id_carrera': row[0],
            'nombre': row[1],
        }
        carreras.append(carrera)
        
    proceso.callproc("SP_LISTAR_RAMOS", [v_salida2])
    ramos = []
    for row in v_salida2:
        ramo = {
            'id_ramo': row[0],
            'nombre': row[1],
            'id_carrera': row[2]
        }
        ramos.append(ramo)
    
    return render(request, "seccion_crear.html" , {'carreras': carreras, 'ramos':ramos})

def form_seccion_crear(request):
    if request.method == 'POST':
        id_ramo = request.POST.get('id_ramo')
        nombre = request.POST.get('nombre_seccion')
        # Elimina espacios en blanco al inicio y al final del comentario
        # Remove leading and trailing whitespaces from 'nombre'
        nombre_stripped = nombre.strip()

        # Check if 'nombre' is empty after stripping whitespaces
        if not nombre_stripped:
            return JsonResponse({'error': 'Nombre no válido'})
        
        try:
            instancia = connection.cursor()
            proceso = instancia.connection.cursor()
            proceso.callproc("SP_CREAR_SECCION", [nombre ,  id_ramo])
            connection.commit()
            return JsonResponse({'success': 'EXITO'})
            
        except cx_Oracle.Error as error:
                # Maneja el error de manera apropiada
                error=("Error al ejecutar el procedimiento almacenado:", error, id_ramo, nombre)
                connection.rollback()
        success = ('ERROR')
    return JsonResponse(success)



@csrf_exempt
def grafico_respuestas(request):
    try:
        if request.method == 'POST':
            id_encuesta = request.POST['id_encuesta']
            accion = request.POST.get('accion') 
            instancia = connection.cursor()
            proceso = instancia.connection.cursor()
            v_salida = instancia.connection.cursor()
            print('grafico')
            if accion == 'grafico':
                proceso.callproc('sp_grafico_encuesta', [id_encuesta, v_salida])
                respuestas = []
                for row in v_salida:
                    respuesta = {
                        'id_encu': row[0],
                        'resuesta_uno': row[1],
                        'resuesta_dos': row[2],
                        'respuestas_otras': row[3],
                    }
                    respuestas.append(respuesta)
                print(respuestas)
                return JsonResponse(respuestas, safe=False)
    except:
        success = f'El error'
        return HttpResponse(success)

