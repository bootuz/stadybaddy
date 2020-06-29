from django.db import models

# Create your models here.
LOCATION_CHOICES = (
    ('online', 'Online'),
    ('offline', 'Offline'),
)


class Announcement(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    image = models.ImageField(upload_to='images', blank=True)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, default='offline')
    place = models.CharField(max_length=500, blank=True)
    group_size = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title}'


