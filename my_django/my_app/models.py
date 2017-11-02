from django.db import models

# Create your models here.\

class Person(models.Model):
	name = models.CharField(max_length=64)
	surname = models.CharField(max_length=64)
	description = models.TextField()



class Address(models.Model):
	ADDRESS_CHOICES = (
			(0, "permanent"),
			(1, "of_residence"),
			(2, "for_correspondence")
			)
	city = models.CharField(max_length=64)
	street = models.CharField(max_length=64)
	number = models.IntegerField()
	local_num = models.IntegerField()
	address_type = models.IntegerField(choices=ADDRESS_CHOICES)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)



class Phone(models.Model):
	PHONE_CHOICES = (
			(0, "home"),
			(1, "mobile"),
			(2, "business")
			)
	phone_number = models.CharField(max_length=16)
	phone_type = models.IntegerField(choices=PHONE_CHOICES)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)



class Email(models.Model):
	EMAIL_CHOICES = (
			(0, "private"),
			(1, "business")
			)
	email = models.EmailField()
	email_type = models.IntegerField(choices=EMAIL_CHOICES)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)



class Group(models.Model):
	name = models.CharField(max_length=32)
	description = models.TextField()
	person = models.ManyToManyField(Person)