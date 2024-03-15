from django.db import models


# Create your models here.
class Pupil(models.Model):
    name = models.CharField(max_length=50, verbose_name='Pupil name', unique=True,null=True)
    month_1 = models.IntegerField(verbose_name='First month', null=True)
    month_2 = models.IntegerField(verbose_name='Second month', null=True)
    month_3 = models.IntegerField(verbose_name='Third month', null=True)
    all_points = models.IntegerField(verbose_name='All points', null=True)
    image = models.ImageField(upload_to='logos',default='logos/pupil_logo.jpg', verbose_name='Pupil_image')


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'children'
        verbose_name = 'Children_list'
        ordering = ('id',)
