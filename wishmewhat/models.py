from django.db import models

from core.models import BaseModel

# Create your models here.
class Wishes(BaseModel):
    text = models.TextField()    
