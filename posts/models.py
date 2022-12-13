from django.db import models
from uuid import uuid4

# Create your models here.


class Posts(models.Model):
    id_post = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    link_post = models.CharField(max_length=500)
    image = models.CharField(max_length=500)