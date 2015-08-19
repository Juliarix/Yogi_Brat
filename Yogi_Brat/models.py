from django.db import models
from members.views import User
 
class Blog(models.Model):
	title = models.CharField(max_length= 100) 
	text = models.TextField()

# class Quiz(models.Model):
# 	limbs = models.IntegerField()
# 	yamas = models.IntegerField()
# 	niyamas = models.IntegerField()
# 	asana = models.TextField()
# 	dhyana = models.TextField()
# 	pratyahara = models.TextField()  
# 	dharana = models.TextField() me!
# 	ayamas = models.TextField()
# 	aniyamas = models.TextField()
# 	samadhi = models.Boolean ***************Finish me!

class Contact(models.Model):
	name = models.TextField()
	question = models.TextField()
	email = models.TextField()

# class Members(models.Model):
# 	first_name = models.TextField()
# 	last_name = models.TextField() 
# 	username = models.TextField()
# 	email = models.TextField()
# 	password = models.TextField()


# class Appointment(models.Model):
# 	date = models.DateField()
# 	name = models.TextField()

