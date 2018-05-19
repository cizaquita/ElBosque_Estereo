from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField(max_length=50,unique=True)
	descripcion = models.CharField(max_length=200)
	habilitado = models.BooleanField(default=True)
	# No editable no visible
	fecha_modificacion = models.DateTimeField('Editado', auto_now=True, editable=False, null=True)
	fecha_creacion = models.DateTimeField('Creado', auto_now_add=True, editable=False, null=True)
	#creado_por = models.ForeignKey(User, related_name='cat_creado_por', blank=True,  on_delete=models.CASCADE, editable=False)
	#modificado_por = models.ForeignKey(User, related_name='cat_modificado_por', blank=True,  on_delete=models.CASCADE, editable=False)
	"""docstring for Category"""
	def __str__(self):
		return self.nombre

class Subcategoria(models.Model):
	# rol_id guarda al llave foránea de la clase rol
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)	
	nombre = models.CharField(max_length=50,unique=True)
	descripcion = models.CharField(max_length=200)
	habilitado = models.BooleanField(default=True)
	# No editable no visible
	fecha_modificacion = models.DateTimeField('Editado', auto_now=True, editable=False, null=True)
	fecha_creacion = models.DateTimeField('Creado', auto_now_add=True, editable=False, null=True)
	#creado_por = models.ForeignKey(User, related_name='subcat_creado_por',blank=True, on_delete=models.CASCADE, editable=False)
	#modificado_por = models.ForeignKey(User, related_name='subcat_modificado_por', blank=True, on_delete=models.CASCADE, editable=False)
	"""docstring for Category"""
	def __str__(self):
		return self.nombre


class Programa(models.Model):
	TIPOS_PROGRAMA = (
        ('pregrabado', 'Pregrabado'),
        ('en_vivo', 'En Vivo'),
    )
	# rol_id guarda al llave foránea de la clase rol
	subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200)
	fecha_inicio = models.DateTimeField('Inicio', editable=False, null=True)
	fecha_final = models.DateTimeField('Fin', editable=False, null=True)
	imagen_banner = models.ImageField(upload_to="media/img/programas/", default="media/img/programas/sin-imagen.jpg", blank=True, null=True, max_length=100)
	tipo_programa = models.CharField(max_length=11, choices=TIPOS_PROGRAMA)
	url_pregrabado = models.CharField(max_length=200, blank=True, null=True)
	habilitado = models.BooleanField(default=True)
	# No editable no visible
	fecha_modificacion = models.DateTimeField('Editado', auto_now=True, editable=False, null=True)
	fecha_creacion = models.DateTimeField('Creado', auto_now_add=True, editable=False, null=True)
	#creado_por = models.ForeignKey(User, related_name='programa_creado_por',blank=True, on_delete=models.CASCADE, editable=False)
	#modificado_por = models.ForeignKey(User, related_name='programa_modificado_por', blank=True, on_delete=models.CASCADE, editable=False)
	"""docstring for Category"""
	def __str__(self):
		return self.nombre