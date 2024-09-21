from django.conf import settings
from django.db import models
from django.utils import timezone #importing timezone library

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ForeignKey used to define data or varaibles lniekd from another model
    title = models.CharField(max_length=200) # CharField is used to define a limited number of characters
    text = models.TextField()# TextField is suitable for large fields of characters instead of CharField (textfield essentially has no limit in characters input)
    created_date = models.DateTimeField(default=timezone.now) # DateTimeField used to input date and time variables 
    published_date = models.DateTimeField(blank=True, null=True)
 
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self): #dunder underscore
        return self.title