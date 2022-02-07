from distutils.command.upload import upload
from pickle import NONE
from django.db import models
from django.utils import timezone

# Create your models here.
class modeloLoadImage (models.Model):
    name_img = models.CharField(max_length=255, null=True)
    url_img = models.ImageField(upload_to='img/', null=False)
    formato = models.CharField(max_length=255, null=False)
    created = models.DateTimeField(default=timezone.now)
    edit = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'images'

    
        
    # def delete (self, using=NONE, keep_parents=False):
    #     self.url_img.delete(self.i);
    #     super().delete()
   