from django.db import models

# Create your models here.

class Role(models.Model):
	id = models.AutoField(primary_key=True)
	label = models.CharField(max_length=50)
	class Meta:
		db_table = "roles"

	def __unicode__(self):
		return self.label
	

class Person(models.Model):
	id = models.AutoField(primary_key=True)
	email = models.CharField(max_length=100, unique = True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	role = models.ForeignKey('Role')

	def __unicode__(self):
		return self.first_name + self.last_name

	class Meta:
		db_table = "people"