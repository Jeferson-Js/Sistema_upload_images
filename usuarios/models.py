from django.db import models

# Create your models here.
class MyFile(models.Model):
    title = models.CharField(max_length=20)
    archive = models.FileField(upload_to="images")

    def __str__(self) -> str:
        return self.title