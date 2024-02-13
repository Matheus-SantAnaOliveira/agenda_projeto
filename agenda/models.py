from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 100)
    created_date = models.DateTimeField(default = timezone.now)
    description = models.TextField(blank = True)
    # category = models.ForeignKey()
    # show = models.enums.Choices()
    # owner = models.ForeignKey()
    # picture = models.ImageField()
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    