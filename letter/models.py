from django.db import models



class Subscribers(models.Model):
    class Meta:
        verbose_name_plural = "Subscribers"


    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

