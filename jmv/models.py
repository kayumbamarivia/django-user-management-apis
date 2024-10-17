from django.db import models

# class Users:
#     id : int
#     name: str
#     email: str
#     password: str
#     img: str
    
class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    

    
