
from django.db import models

class login(models.Model):
    user_name = models.CharField(max_length=64)
    pass_word = models.CharField(max_length=64)

class AddUser(models.Model): 
    first_name =models.CharField(max_length = 64)
    second_name = models.CharField(max_length = 64)
    pass_word = models.CharField(max_length = 64)
    pass_word2 = models.CharField(max_length = 64)
    user_name =models.CharField(max_length = 64)

    
class Like(models.Model):
    like_count = models.CharField(max_length=64)
