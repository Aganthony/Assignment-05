# orm.py

from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    notes = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

