from django.db import models

# Create your models here.
from django.db import models
import os

# Create your models here.

class Monument(models.Model):
    image=models.ImageField(upload_to="app/static/saved")

    def filename(self):
        return os.path.basename(self.image.name)