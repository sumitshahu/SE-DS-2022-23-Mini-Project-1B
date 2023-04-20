from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    author = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    contribution_amount = models.IntegerField()
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos_uploaded',null=True, blank=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

    class Meta:
        ordering = ('-created_at',)


class Transaction(models.Model):
    payment_id = models.CharField(max_length=255)
    razorpay_order_id = models.CharField(max_length=255)
    razorpay_signature = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    post_id = models.TextField(null=True)
    donor = models.TextField() 

    # Other fields related to transaction data can be added here

    def __str__(self):
        return f"Transaction {self.id}"
    