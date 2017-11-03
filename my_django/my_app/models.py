from django.db import models

# Create your models here.\

class Person(models.Model):
	name = models.CharField(max_length=64)
	surname = models.CharField(max_length=64, null=True)
	description = models.TextField(null=True)



class Address(models.Model):
	ADDRESS_CHOICES = (
			(0, "permanent"),
			(1, "of_residence"),
			(2, "for_correspondence")
			)
	city = models.CharField(max_length=64, null=True)
	street = models.CharField(max_length=64, null=True)
	number = models.IntegerField(null=True)
	local_num = models.IntegerField(null=True)
	address_type = models.IntegerField(choices=ADDRESS_CHOICES, default=0)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)



class Phone(models.Model):
	PHONE_CHOICES = (
			(0, "home"),
			(1, "mobile"),
			(2, "business")
			)
	phone_number = models.CharField(max_length=16, null=True)
	phone_type = models.IntegerField(choices=PHONE_CHOICES, default=0)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)



class Email(models.Model):
	EMAIL_CHOICES = (
			(0, "private"),
			(1, "business")
			)
	email = models.EmailField(null=True)
	email_type = models.IntegerField(choices=EMAIL_CHOICES, default=0)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)



class Group(models.Model):
	name = models.CharField(max_length=32)
	description = models.TextField()
	person = models.ManyToManyField(Person)