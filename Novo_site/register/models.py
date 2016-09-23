from django.db import models

class Register(models.Model):
    title = models.CharField(max_length=10)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phoneNo = models.CharField(max_length=15)
    diet = models.CharField(max_length=10)
    medNo = models.CharField(max_length=10)
    practAd = models.CharField(max_length=50)

    # prof = models.FileField(null=True , blank=True)

    def __str__(self):
        return self.title

