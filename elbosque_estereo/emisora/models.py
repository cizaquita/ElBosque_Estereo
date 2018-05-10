from django.db import models

# Create your models here.

	# """ Clase Rol """	
class Role(models.Model):
	rol_name = models.CharField(max_length=200)
	rol_description = models.CharField(max_length=200)
	# URL es para: ? TODO
	rol_url = models.CharField(max_length=200)
	rol_enabled = models.BooleanField(default=True)
	# """docstring for Role"""
	def __str__(self):
		return self.rol_name


	# """ Clase Modulo"""
class Module(models.Model):
	mdl_name = models.CharField(max_length=200)
	mdl_description = models.CharField(max_length=200)
	# URL es para: ? TODO
	mdl_url = models.CharField(max_length=200)
	mdl_enabled = models.BooleanField(default=True)

	# """docstring for Module"""
	def __str__(self):
		return self.mdl_name
	
	# """ Clase Rol y Modulo """
class Role_Module(models.Model):
	rol_id = models.ForeignKey(Role, on_delete=models.CASCADE)
	mdl_id = models.ForeignKey(Module, on_delete=models.CASCADE)

	# """docstring for Role_Module """
	def __str__(self):
		return 'Rol ' + self.rol_id.rol_name + ', Modulo ' + self.mdl_id.mdl_name


	# """ Clase Usuario"""	
class User(models.Model):
	usr_name = models.CharField(max_length=200)
	usr_lastname = models.CharField(max_length=200)
	usr_celphone = models.CharField(max_length=200)
	usr_password = models.CharField(max_length=200)
	# No editable no visible
	usr_created_by = models.CharField(max_length=200, editable=False, null=True)
	usr_modified_by = models.CharField(max_length=200, editable=False, null=True)
	usr_created_date = models.DateTimeField('Creado', editable=False, null=True)
	usr_modified_date = models.DateTimeField('Editado', editable=False, null=True)
	# rol_id guarda al llave foránea de la clase rol
	rol_id = models.ForeignKey(Role, on_delete=models.CASCADE)
	usr_enabled = models.BooleanField(default=True)
	"""docstring for User"""
	def __str__(self):
		return self.usr_name + ' ' + self.usr_lastname



class Category(models.Model):
	ctg_name = models.CharField(max_length=100)
	ctg_description = models.CharField(max_length=100)
	ctg_image_url = models.CharField(max_length=250)
	# No editable no visible
	ctg_modified_date = models.DateTimeField('Editado', editable=False, null=True)
	ctg_created_date = models.DateTimeField('Creado', editable=False, null=True)
	ctg_created_by = models.CharField(max_length=200, editable=False, null=True)
	ctg_modified_by = models.CharField(max_length=200, editable=False, null=True)
	ctg_enabled = models.BooleanField(default=True)
	"""docstring for Category"""
	def __str__(self):
		return self.ctg_name

class Subcategory(models.Model):
	# rol_id guarda al llave foránea de la clase rol
	ctg_id = models.ForeignKey(Category, on_delete=models.CASCADE)	
	sct_name = models.CharField(max_length=100)
	sct_description = models.CharField(max_length=100)
	sct_image_url = models.CharField(max_length=250)
	# No editable no visible
	sct_modified_date = models.DateTimeField('Editado', editable=False, null=True)
	sct_created_date = models.DateTimeField('Creado', editable=False, null=True)
	sct_created_by = models.CharField(max_length=200, editable=False, null=True)
	sct_modified_by = models.CharField(max_length=200, editable=False, null=True)
	sct_enabled = models.BooleanField(default=True)
	"""docstring for Category"""
	def __str__(self):
		return self.sct_name


class Program(models.Model):
	# rol_id guarda al llave foránea de la clase rol
	sct_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE)	
	prg_name = models.CharField(max_length=100)
	prg_description = models.CharField(max_length=100)
	prg_audio_url = models.CharField(max_length=250)
	prg_image_url = models.CharField(max_length=250)
	# No editable no visible
	prg_modified_date = models.DateTimeField('Editado', editable=False, null=True)
	prg_created_date = models.DateTimeField('Creado', editable=False, null=True)
	prg_created_by = models.CharField(max_length=200, editable=False, null=True)
	prg_modified_by = models.CharField(max_length=200, editable=False, null=True)
	prg_enabled = models.BooleanField(default=True)
	"""docstring for Category"""
	def __str__(self):
		return self.prg_name



class Schedule_program(models.Model):
	# rol_id guarda al llave foránea de la clase rol
	prg_id = models.ForeignKey(Program, on_delete=models.CASCADE)
	sp_start_time = models.DateTimeField('Inicio')
	sp_end_time = models.DateTimeField('Final')
	"""docstring for Category"""
	def __str__(self):
		return self.prg_name

