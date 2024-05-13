from django.db import models
from django.contrib.auth.models import User

# Create your model for social media site 

class Post(models.Model):
    text = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
    )

    def __str__(self):
        return self.text[0:100]

