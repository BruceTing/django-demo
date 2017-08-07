from django.db import models

# Create your models here.
class Users(models.Model):
    ''' use default database '''
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    # email = models.EmailField(max_length=50, null=True)
    type = models.SmallIntegerField(4, null=True)
    authorityid = models.IntegerField(11, null=True)

    def __str__(self):
        return self.username

class BigData(models.Model):
    ''' use fdms database '''
    source = models.CharField(max_length=25, null=True)
    content = models.CharField(max_length=250, null=True)
    by_who = models.CharField(max_length=50, null=True)
    collect_date = models.DateField()

    def __str__(self):
        return self.content