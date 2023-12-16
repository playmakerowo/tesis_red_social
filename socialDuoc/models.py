# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alumno(models.Model):
    matricula = models.BigIntegerField()
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    
    class Meta:
        managed = False
        db_table = 'alumno'


class Amigo(models.Model):
    id_amistad = models.AutoField(primary_key=True)
    id_amigo = models.BigIntegerField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'amigo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nom_carrera = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'carrera'



class CarreraSede(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    id_sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='id_sede')

    class Meta:
        managed = False
        db_table = 'carrera_sede'


class Chat(models.Model):
    id_chat = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=150)
    archivo = models.BinaryField(blank=True, null=True)
    usu_recep = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'chat'


class Comentario(models.Model):
    id_coment = models.AutoField(primary_key=True)
    comentario = models.CharField(max_length=50)
    id_publi = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='id_publi')

    class Meta:
        managed = False
        db_table = 'comentario'


class Comuna(models.Model):
    id_comu = models.AutoField(primary_key=True)
    nom_comuna = models.CharField(max_length=20)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'comuna'



class Coordinador(models.Model):
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_carrera = models.ForeignKey(Carrera, models.DO_NOTHING, db_column='id_carrera')

    class Meta:
        managed = False
        db_table = 'coordinador'


class Director(models.Model):
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_carrera = models.ForeignKey(Carrera, models.DO_NOTHING, db_column='id_carrera')

    class Meta:
        managed = False
        db_table = 'director'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Docente(models.Model):
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)

    class Meta:
        managed = False
        db_table = 'docente'



class Encuesta(models.Model):
    titulo = models.CharField(max_length=100)
    pregunta = models.CharField(max_length=100)
    descrip = models.CharField(max_length=1500, blank=True, null=True)
    fecha = models.DateField()
    fechafin = models.DateField()
    estado = models.BigIntegerField()
    id_encu = models.AutoField(primary_key=True)
    link = models.CharField(max_length=150, blank=True, null=True)
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'encuesta'



class EstadoPerfil(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nom_est = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'estado_perfil'


class EventoAgendado(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nom_even = models.CharField(max_length=30)
    fecha = models.DateField()
    descrip = models.CharField(max_length=150)
    estado = models.BigIntegerField()
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    fechafin = models.DateField()

    class Meta:
        managed = False
        db_table = 'evento_agendado'


class Genero(models.Model):
    id_gen = models.AutoField(primary_key=True)
    nom_gen = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'genero'



class Institucion(models.Model):
    usuario_id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario', primary_key=True)
    id_sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='id_sede')

    class Meta:
        managed = False
        db_table = 'institucion'


class MeGusta(models.Model):
    id_me_gusta = models.AutoField(primary_key=True)
    id_publi = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='id_publi')
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'me_gusta'



class MyAdmin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    contrasenia = models.CharField(max_length=20, blank=True, null=True)
    usuario = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_admin'



class Participantes(models.Model):
    id_parti = models.AutoField(primary_key=True)
    id_evento = models.ForeignKey(EventoAgendado, models.DO_NOTHING, db_column='id_evento')

    class Meta:
        managed = False
        db_table = 'participantes'



class Publicacion(models.Model):
    id_publi = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descrip = models.CharField(max_length=150)
    estado = models.BigIntegerField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    fotos = models.ImageField(upload_to='publicaciones', null=True)

    class Meta:
        managed = False
        db_table = 'publicacion'


class Ramo(models.Model):
    id_ramo = models.AutoField(primary_key=True)
    nom_ramo = models.CharField(max_length=100)
    id_carrera = models.ForeignKey(Carrera, models.DO_NOTHING, db_column='id_carrera')

    class Meta:
        managed = False
        db_table = 'ramo'



class RamoDoc(models.Model):
    docente_id_usuario = models.OneToOneField(Docente, models.DO_NOTHING, db_column='docente_id_usuario', primary_key=True)
    ramo_id_ramo = models.ForeignKey(Ramo, models.DO_NOTHING, db_column='ramo_id_ramo')

    class Meta:
        managed = False
        db_table = 'ramo_doc'


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nom_region = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'region'



class Seccion(models.Model):
    id_secc = models.AutoField(primary_key=True)
    nom_seccion = models.CharField(max_length=15)
    id_ramo = models.ForeignKey(Ramo, models.DO_NOTHING, db_column='id_ramo')

    class Meta:
        managed = False
        db_table = 'seccion'



class SeccionAluDoc(models.Model):
    seccion_id_secc = models.OneToOneField(Seccion, models.DO_NOTHING, db_column='seccion_id_secc', primary_key=True)
    docente_usuario_id_usuario = models.ForeignKey(Docente, models.DO_NOTHING, db_column='docente_usuario_id_usuario')
    alumno_usuario_id_usuario = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='alumno_usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'seccion_alu_doc'



class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nom_sede = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sede'

    def __str__(self):
        return self.nom_sede


class TipoUsuario(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nom_tipo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'

    def __str__(self):
        return self.nom_tipo

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    rut = models.BigIntegerField()
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=30)
    ap_pater = models.CharField(max_length=30)
    ap_mater = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    foto = models.BinaryField(blank=True, null=True)
    correo = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    id_comu = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comu')
    id_gen = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_gen')
    id_estado = models.ForeignKey(EstadoPerfil, models.DO_NOTHING, db_column='id_estado')
    id_tipo = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipo')

    class Meta:
        managed = False
        db_table = 'usuario'


    def __str__(self):
        return self.correo


class UsuarioChat(models.Model):
    id_chat = models.OneToOneField(Chat, models.DO_NOTHING, db_column='id_chat', primary_key=True)
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'usuario_chat'


from django.db import models
from django.utils import timezone

class OneTimeToken(models.Model):
    token = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.token


class contenido(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=30)
    titulo = models.CharField(max_length=255)
    fecha = models.DateField()
    fecha_fin = models.DateField()
    nombre_usuario = models.CharField(max_length=30)
    descripcion = models.TextField()
    pregunta = models.TextField()
    link = models.URLField()
    respuesta_uno = models.TextField()
    respuesta_dos = models.TextField()
    like_count = models.IntegerField()
    id_usuario = models.IntegerField()
    foto_usuario = models.BinaryField(blank=True, null=True)
    foto_publicacion = models.BinaryField(blank=True, null=True)
    sede = models.TextField()
    usuario = models.TextField()

    def __str__(self):
        return f"contenido(id_publicacion={self.id_publicacion}, tipo={self.tipo}, titulo={self.titulo}, fecha={self.fecha}, fecha_fin={self.fecha_fin}, nombre_usuario={self.nombre_usuario}, descripcion={self.descripcion}, pregunta={self.pregunta}, link={self.link}, respuesta_uno={self.respuesta_uno}, respuesta_dos={self.respuesta_dos}, like_count={self.like_count}, id_usuario={self.id_usuario}, foto_usuario={self.foto_usuario}, foto_publicacion={self.foto_publicacion}, sede={self.sede}, ususario={self.usuario})"