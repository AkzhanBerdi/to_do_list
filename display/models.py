from django.db import models

# Create your models here.
class Task(models.Model):
    objective = models.CharField(max_length=50, null=True, blank=False)
    status = models.CharField(max_length=25, default='New')
    dead_line = models.DateField(auto_now=False, auto_now_add=False, blank=True, default=None)
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return f"{self.pk}. {self.objective} - {self.status} || {self.dead_line} || {self.description}"