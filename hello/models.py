from django.db import models
from django.utils import timezone


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name  # name to be shown when called


class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        return self.title  # name to be shown when called
