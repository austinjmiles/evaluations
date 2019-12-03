from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models





MY_CHOICES = (('item_key1', '1'),
              ('item_key2', '2'),
              ('item_key3', '3'),
              ('item_key4', '4'),
              ('item_key5', '5'))


MY_CHOICES2 = (('item_key1', 'less than 2'),
              ('item_key2', '2'),
              ('item_key3', '2.5'),
              ('item_key4', '3'),
              ('item_key5', 'more than 3'))


class Lab(models.Model):
	term = models.IntegerField(blank=True)
	class_number = models.IntegerField(blank=True)
	subject = models.CharField(max_length=100, blank=True)
	catalog = models.CharField(max_length=100, blank=True)
	title = models.CharField(max_length=400, blank=True)
	section = models.IntegerField(blank=True)
	instructor = models.CharField(max_length=150, blank=True)
	def __str__(self):
		return self.title

class Student(models.Model):
	name = models.CharField(max_length=100, blank=True)
	email = models.EmailField(max_length=70,blank=True,null=True)
	student_id = models.IntegerField(default=0)
	lab1 = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='lab1',null=True)
	l1 = models.BooleanField(default=False)
	lab2 = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='lab2',blank=True,null=True)
	l2 = models.BooleanField(default=False)
	lab3 = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='lab3',blank=True,null=True)
	l3 = models.BooleanField(default=False)
	lab4 = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='lab4',blank=True,null=True)
	l4 = models.BooleanField(default=False)
	lab5 = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='lab5',blank=True,null=True)
	l5 = models.BooleanField(default=False)
	def __str__ (self):
		return '%s' % (self.name)


#show form for each lab

class Survey(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	lab = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='lab',null=True)

	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student', null=True)
	q0= MultiSelectField(choices=MY_CHOICES, max_choices=1, default=[])
	q1= MultiSelectField(choices=MY_CHOICES, max_choices=1, default=[])
	q2= MultiSelectField(choices=MY_CHOICES, max_choices=1, default=[])
	q3= MultiSelectField(choices=MY_CHOICES, max_choices=1, default=[])
	q4= MultiSelectField(choices=MY_CHOICES, max_choices=1, default=[])
	q5= MultiSelectField(choices=MY_CHOICES, max_choices=1, default=[])
	q6= MultiSelectField(choices=MY_CHOICES, max_choices=1, default=[])
	q7= MultiSelectField(choices=MY_CHOICES, max_choices=1, default=[])
	q8= MultiSelectField(choices=MY_CHOICES, max_choices=1, default=[])
	q9= MultiSelectField(choices=MY_CHOICES, max_choices=1, default=[])
	q10= MultiSelectField(choices=MY_CHOICES, max_choices=1, default=[])
	q11= MultiSelectField(choices=MY_CHOICES, max_choices=1, default=[])
	q12= MultiSelectField(choices=MY_CHOICES2, max_choices=1, default=[])
	q13= MultiSelectField(choices=MY_CHOICES2, max_choices=1, default=[])
	q14= MultiSelectField(choices=MY_CHOICES2, max_choices=1, default=[])
	f1= models.TextField(blank=True,null=True)
	f2= models.TextField(blank=True,null=True)
	f3= models.TextField(blank=True,null=True)
	f4= models.TextField(blank=True,null=True)
	f5= models.TextField(blank=True,null=True)


# class UserManager(BaseUserManager):
# 	def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
# 		if not email:
# 			raise ValueError("Users must have a SCU email")
# 		if not password:
# 			raise ValueError("Users must have a password")
# 		user_obj = self.model(
# 			email = self.normalize_email(email)
# 		)

# 		user_obj.set_password(Password)
# 		user_obj.staff = is_staff
# 		user_obj.admin = is_admin
# 		user_obj.active = is_active
# 		user_obj.save(using=self._db)
# 		return user_obj

# 	def create_staffuser(self,email,password=None):
# 		user = self.create_user(
# 			email,
# 			password=password,
# 			is_staff=True,
			
# 			)

# 	def create_superuser(self,email,password=None):
# 		user = self.create_user(
# 			email,
# 			password=password,
# 			is_staff=True,
# 			is_admin=True
# 			)
 

# class User(AbstractBaseUser):
# 	email 		= models.EmailField(max_length=255, unique=True)
# 	active		= models.BooleanField(default=True) # can login
# 	staff	 	= models.BooleanField(default=False) 
# 	admin 		= models.BooleanField(default=False) # a superuser

# 	USERNAME_FIELD = 'email'	#username
# 	# email and password are required by default
# 	REQUIRED_FIELDS = []

# 	objects = UserManager()

# 	def __str__(self):
# 		return self.email

# 	def get_full_name(self):
# 		return self.email

# 	def get_short_name(self): 
# 		return self.email

# 	@property
# 	def is_staff(self):
# 		return self.staff

# 	@property
# 	def is_admin(self):
# 		return self.admin

# 	@property
# 	def is_active(self):
# 		return self.active


# class Profile(models.Model):
# 	user = models.OneToOneField(User,on_delete=models.CASCADE)














































