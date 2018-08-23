from django.db import models

from user.models import User


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=256)
    comment = models.TextField(max_length=256, null=True)
    message_at = models.DateTimeField(auto_now=True)
    thumbs = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
