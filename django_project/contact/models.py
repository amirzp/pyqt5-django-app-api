from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    family = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    phone = models.CharField(max_length=50, verbose_name='تلفن')
    email = models.CharField(max_length=50, verbose_name='ایمیل')

    class Meta:
        verbose_name = 'مخاطب'
        verbose_name_plural = 'مخاطبین'

    def __str__(self):
        return self.name
