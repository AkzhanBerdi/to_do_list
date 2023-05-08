from django.db import models

# Create your models here.
class Task(models.Model):
    objective = models.CharField(max_length=25, null=False, blank=False)
    status = models.CharField(max_length=10, null=False, default='New')
    dead_line = models.DateField(auto_now=False, auto_now_add=False, blank=True, default=None)

    def __str__(self):
        return f"{self.pk}.{self.objective} - {self.status} || {self.dead_line}"