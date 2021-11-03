from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
# Create your models here

from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
# Create your models here


class Kodagu_town(Model):
    def __str__(self):
        return self.__class__.__name__
        
    Town_name=models.CharField(max_length=150)
    use=models.BooleanField()
""" towns names """

class Napoklu(Model):
    def __str__(self):
        return self.__class__.__name__
    
   
    Middle_route=models.CharField(max_length=150)
    source=models.CharField(max_length=150)
    destination=models.CharField(max_length=150)
    arrive_t=models.TimeField(auto_now=False,auto_now_add=False)
    leave_t=models.TimeField(auto_now=False,auto_now_add=False)
    Busname=models.CharField(max_length=150)
    likes_count=models.IntegerField(default=0)    


class murnad(Model):
    def __str__(self):                   #Napoklu murnad virajpet Madikeri somarpet 
        return self.__class__.__name__

    Middle_route=models.CharField(max_length=150)
    source=models.CharField(max_length=150)
    destination=models.CharField(max_length=150)
    arrive_t=models.TimeField(auto_now=False,auto_now_add=False)
    leave_t=models.TimeField(auto_now=False,auto_now_add=False)
    Busname=models.CharField(max_length=150)
    likes_count=models.IntegerField(default=0)

class virajpet(Model):
    def __str__(self):
        return self.__class__.__name__

    Middle_route=models.CharField(max_length=150)
    source=models.CharField(max_length=150)
    destination=models.CharField(max_length=150)
    arrive_t=models.TimeField(auto_now=False,auto_now_add=False)
    leave_t=models.TimeField(auto_now=False,auto_now_add=False)
    Busname=models.CharField(max_length=150)
    likes_count=models.IntegerField(default=0)

class Madikeri(Model):
    def __str__(self):
        return self.__class__.__name__

    Middle_route=models.CharField(max_length=150)
    source=models.CharField(max_length=150)
    destination=models.CharField(max_length=150)
    arrive_t=models.TimeField(auto_now=False,auto_now_add=False)
    leave_t=models.TimeField(auto_now=False,auto_now_add=False)
    Busname=models.CharField(max_length=150)
    likes_count=models.IntegerField(default=0)


class madikeri2(Model):
    def __str__(self):
        return self.__class__.__name__

    Middle_route=models.CharField(max_length=150)
    source=models.CharField(max_length=150)
    destination=models.CharField(max_length=150)
    arrive_t=models.TimeField(auto_now=False,auto_now_add=False)
    leave_t=models.TimeField(auto_now=False,auto_now_add=False)
    Busname=models.CharField(max_length=150)
    likes_count=models.IntegerField(default=0)

class kutta(Model):
    def __str__(self):
        return self.__class__.__name__

    Middle_route=models.CharField(max_length=150)
    source=models.CharField(max_length=150)
    destination=models.CharField(max_length=150)
    arrive_t=models.TimeField(auto_now=False,auto_now_add=False)
    leave_t=models.TimeField(auto_now=False,auto_now_add=False)
    Busname=models.CharField(max_length=150)
    likes_count=models.IntegerField(default=0)
class ponnampet(Model):
    def __str__(self):
        return self.__class__.__name__

    Middle_route=models.CharField(max_length=150)
    source=models.CharField(max_length=150)
    destination=models.CharField(max_length=150)
    arrive_t=models.TimeField(auto_now=False,auto_now_add=False)
    leave_t=models.TimeField(auto_now=False,auto_now_add=False)
    Busname=models.CharField(max_length=150)
    likes_count=models.IntegerField(default=0)
    

class gonikoppal(Model):
    def __str__(self):
        return self.__class__.__name__

    Middle_route=models.CharField(max_length=150)
    source=models.CharField(max_length=150)
    destination=models.CharField(max_length=150)
    arrive_t=models.TimeField(auto_now=False,auto_now_add=False)
    leave_t=models.TimeField(auto_now=False,auto_now_add=False)
    Busname=models.CharField(max_length=150)
    likes_count=models.IntegerField(default=0)
class somarpet(Model):
    def __str__(self):
        return self.__class__.__name__

    Middle_route=models.CharField(max_length=150)
    source=models.CharField(max_length=150)
    destination=models.CharField(max_length=150)
    arrive_t=models.TimeField(auto_now=False,auto_now_add=False)
    leave_t=models.TimeField(auto_now=False,auto_now_add=False)
    Busname=models.CharField(max_length=150)
    likes_count=models.IntegerField(default=0)



""" likes and dislikes for traveling"""

class  Travel_exprience(Model):
    def __str__(self):
        return self.__class__.__name__

    Middle_route=models.CharField(max_length=150)
    source=models.CharField(max_length=150)
    destination=models.CharField(max_length=150)
    likes=models.IntegerField()
    Dislikes=models.IntegerField() 

class incorrect_data(Model):
    def __str__(self):
        return self.__class__.__name__
    town_tab_name=models.CharField(max_length=20) 
    post_id=models.IntegerField()
    complaint=models.CharField(max_length=20)

class detailquery(Model):
    def __str__(self):
        return self.__class__.__name__
    source=models.CharField(max_length=10)
    dest=models.CharField(max_length=10)
    time=models.CharField(max_length=6)
    Email= models.EmailField(max_length = 254)
    comments=models.TextField()
    user_name=models.CharField(max_length=30)
    
class corrected_data_by_user(Model):
    def __str__(self):
        return self.__class__.__name__

    town_tab_name=models.CharField(max_length=150)
    Middle_route=models.CharField(max_length=150)
    source=models.CharField(max_length=150)
    destination=models.CharField(max_length=150)
    arrive_t=models.TimeField(auto_now=False,auto_now_add=False)
    leave_t=models.TimeField(auto_now=False,auto_now_add=False)
    Busname=models.CharField(max_length=150)
    
class data_given_by_user(Model):
    def __str__(self):
        return self.__class__.__name__
    
    Middle_route=models.CharField(max_length=150)
    source=models.CharField(max_length=150)
    destination=models.CharField(max_length=150)
    arrive_t=models.TimeField(auto_now=False,auto_now_add=False)
    leave_t=models.TimeField(auto_now=False,auto_now_add=False)
    Busname=models.CharField(max_length=150)

class feeback_data(Model):
    def __str__(self):
        return self.__class__.__name__
    user_name=models.CharField(max_length=30)
    comments=models.TextField()
    Email= models.EmailField(max_length = 254)
   
"""class contact_us(Model):
    def __str__(self):
       return self.__class__.__name__
    comments=models.TextField()
    Email= models.EmailField(max_length = 254)"""

class save_contact_inf(Model):
    def __str__(self):
       return self.__class__.__name__
    user_name=models.CharField(max_length=30)#user_name,comments,Email
    comments=models.TextField()
    Email= models.EmailField(max_length = 254)

        
class replys(Model):
    def __str__(self):
        return self.__class__.__name__
    id_of_comenter=models.IntegerField()
    reply=models.TextField()



class liked_data(Model):
    def __str__(self):
        return self.__class__.__name__  
    post_id=models.IntegerField()
    user_id=models.IntegerField()
    
class images(Model):
    def __str__(self) -> str:
        return self.__class__.__name__ 
    images=models.ImageField(upload_to="pics")


