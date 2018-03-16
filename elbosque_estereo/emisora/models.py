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
	usr_created_by = models.CharField(max_length=200)
	usr_modified_by = models.CharField(max_length=200)
	usr_created_date = models.DateTimeField('Creado')
	usr_modified_date = models.DateTimeField('Editado')
	# rol_id guarda al llave foránea de la clase rol
	rol_id = models.ForeignKey(Role, on_delete=models.CASCADE)
	usr_enabled = models.BooleanField(default=True)
	"""docstring for User"""
	def __str__(self):
		return self.usr_name + ' ' + self.usr_lastname