from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_created=True, auto_now=True)
    text = models.TextField(help_text="Write here")
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title