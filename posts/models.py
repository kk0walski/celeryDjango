from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta:
        unique_together = (('id', 'platform'),)
    PLATFORM_CHOICES = (
        ('T', 'Twitter'),
        ('R', 'Reddit'),
        ('G', 'Google'),
        ('Q', 'Quaora')
    )
    id = models.BigIntegerField(primary_key=True)
    platform = models.CharField(max_length=1, choices=PLATFORM_CHOICES)
    user = models.CharField(max_length=30)
    link = models.URLField()
    created_at = models.DateTimeField()
    text = models.TextField()
    title = models.CharField(max_length=200)
