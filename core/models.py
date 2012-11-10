from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Visualization(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    javascript = models.TextField(blank=True)
    styles = models.TextField(blank=True)
    data = models.TextField(blank=True)
    tags = TaggableManager()
    def __unicode__(self):
        return u"%s" % (self.name)

