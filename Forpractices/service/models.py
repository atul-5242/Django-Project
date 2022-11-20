from django.db import models
a=10
class Service(models.Model):

    passward=models.CharField(max_length=50)
    user_name=models.CharField(max_length=50)

    # class Meta:
    #     verbose_name = _("Service")
    #     verbose_name_plural = _("Services")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Service_detail", kwargs={"pk": self.pk})



# Create your models here.


"""
3 comands:===================

python manage.py startapp service

python manage.py makemigrations

python manage.py migrate

==============================
"""