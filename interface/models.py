
from django.db import models

class AddUser(models.Model): 
    first_name =models.CharField(max_length = 64)
    last_name = models.CharField(max_length = 64)
    pass_word = models.CharField(max_length = 64)
    user_name =models.CharField(max_length = 64)
    Email = models.EmailField(max_length = 64, blank=True, null=True)
    class Meta:
        db_table ="adduser"

class User(models.Model):
    addUser = models.ForeignKey(AddUser, related_name='add', on_delete=models.CASCADE, blank=True, null=True)
        

    
class Like(models.Model):
    like_count = models.CharField(max_length=64)
