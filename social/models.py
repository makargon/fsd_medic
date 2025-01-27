from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from fsd_medic.settings import AUTH_USER_MODEL
from api.models import News, Center
import uuid

User = AUTH_USER_MODEL
# Create your models here.
class Notification(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    pass 


class Chat(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    to_center = models.ForeignKey(Center, on_delete=models.CASCADE, null=True, blank=True)
    from_center = models.ForeignKey(Center, on_delete=models.CASCADE, null=True, blank=True, related_name="from_center")
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
       return f"Chat - {self.uuid}"

class Message(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.PROTECT,null=True, blank=True)
    text = models.TextField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    center = models.ForeignKey(Center, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Message {self.user} - {self.chat}'
