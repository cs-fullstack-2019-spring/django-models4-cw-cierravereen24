from django.db import models


# Create your models here.

class Mom(models.Model):
    mom_first_name = models.CharField(max_length=100)
    mom_last_name = models.CharField(max_length=100)
    mom_phone_number = models.IntegerField()

    def __str__(self):
        return self.mom_first_name


class Child(models.Model):
    child_first_name = models.CharField(max_length=100)
    child_last_name = models.CharField(max_length=100)
    child_mom = models.ForeignKey(Mom, on_delete=models.CASCADE)

    def __str__(self):
        return self.child_first_name
