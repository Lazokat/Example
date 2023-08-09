from django.db import models

# Create your models here.
class Blog(models.Model):
    body=models.TextField()
    title=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
