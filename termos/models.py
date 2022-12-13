from django.db import models
from uuid import uuid4
# Create your models here.


class Termos(models.Model):
    id_post = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    link_termos = models.CharField(max_length=500)