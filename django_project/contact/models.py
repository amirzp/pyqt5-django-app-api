from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name='ﻧﺎﻡ')
    family = models.CharField(max_length=20, verbose_name='ﻧﺎﻡ ﺧﺎﻧﻮاﺩﮔﯽ')
    phone = models.CharField(max_length=20, verbose_name='ﺗﻠﻔﻦ')
    email = models.CharField(max_length=40, verbose_name='اﯾﻤﯿﻞ')

    class Meta:
        verbose_name = 'ﻣﺨﺎﻃﺐ'
        verbose_name_plural = 'ﻣﺨﺎﻃﺒﯿﻦ'

    def __str__(self):
        return self.name
