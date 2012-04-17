from django.db import models

from django_model_tools.decorators import force_save_not_null_nor_blank

# Create your models here.
class SampleModel(models.Model):
    a_field = models.CharField(max_length=5) # this is by default blank=True, null= True

    @force_save_not_null_nor_blank('a_field')
    def save(self, force_insert=False, force_update=False, using=None):
        super(SampleModel, self).save(force_insert, force_update, using)