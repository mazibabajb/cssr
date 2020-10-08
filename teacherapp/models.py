from django.db import models

# Create your models here.
courses = (
    ('select','Select a course'),
    ('Marketing','Marketing'),
    ('accounting','accounting'),
    ('hotel','hotel'),
    ('human','human'),
    ('tourism','Tourism And Hospitality'),
    ('human','Data Science'),
    ('Social','social Work'),
    ('public','Public Relations'),
    ('ecd','Ecd Teacher Training'),
    ('project','project Management'),
    ('health','Health and safety'),
    ('basic','Basic Computer Lessons'),
    ('graphic','Graphic Desinig'),
    ('Programing','Programing'),


    )


class Registration(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    next_of_kin = models.CharField(max_length=30)
    course = models.CharField(
        choices=courses,
        default='select',
        max_length=30)
    created_with = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.firstname} Registration'
  
class Blog(models.Model):
    title = models.CharField(max_length=30)
    auther = models.CharField(max_length=30)
    post = models.TextField(max_length=500)
    created_with = models.DateTimeField(auto_now=True)


class Courses(models.Model):
    title = models.CharField(max_length=30)
    tutor = models.CharField(max_length=30)
    course_outline = models.TextField(max_length=500)
    time_duration = models.CharField(max_length=500)
       
class Contact(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    created_with = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.firstname} Contact'
        
  
		

