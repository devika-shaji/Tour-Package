from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class Custuser(AbstractUser):
    ROLE_CHOICES=(
        ('user','User'),
        ('vendor','Vendor'),
        ('admin','Admin'),
    )
    role=models.CharField(max_length=100,choices=ROLE_CHOICES,default='user')

    def __str__(self):
        return self.username


class Packages(models.Model):
    title=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    duration=models.PositiveIntegerField(help_text="Duration in days")
    image=models.ImageField(upload_to='packageimage/',blank=True,null=True)
    approved=models.BooleanField(default=False)
    vendor=models.ForeignKey(Custuser,on_delete=models.CASCADE,limit_choices_to={'role':'vendor'},related_name='packages')
    description=models.TextField(blank=True)
    expiry=models.DateTimeField(default=timezone.now)
    is_booked=models.BooleanField(default=False)
    
    @property
    def is_expired(self):
        return timezone.now()
    def __str__(self):
        return f"{self.title}- {self.destination}"


class Booking(models.Model):
    user=models.ForeignKey(Custuser,on_delete=models.CASCADE,related_name='bookings')
    package=models.ForeignKey(Packages,on_delete=models.CASCADE,related_name='bookings')
    booking_date=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=100,
                                    choices=[('pending','Pending'),('completed','Completed'),('failed','Failed')],
                                    default='pending')

    def __str__(self):
         return f"Booking by {self.user.username} for {self.package.title}"


