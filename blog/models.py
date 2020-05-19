from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateField(null=True)

    def __str__(self):
        return self.title
