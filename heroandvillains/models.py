from pyexpat import model
from xml.dom.minidom import CharacterData
from django.db import models

# Create your models here.

class heroandvillains(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField()
    secondary_ability = models.CharField()
    catchphrase = CharacterData()
    super_type = models.ForeignKey()
    


