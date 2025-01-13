from django.db import models
from django.urls import reverse

DURATIONS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
)





# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # image = models.CharField(default=None, blank=True, null=True, max_length=2000)
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
    def __str__(self):
        return self.name
    
class Visit(models.Model):
    date = models.DateField()
    # B - breakfast, L - lunch, D - dinner
    duration = models.CharField(max_length=1, choices=DURATIONS, default=DURATIONS[0][0])
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE) #foreign key will always be in the many side (rule of thumb)

    def __str__(self):
        return f"{self.get_duration_display()} on {self.date} for {self.finch.name} "