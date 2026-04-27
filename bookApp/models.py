from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserModel(AbstractUser):
    
    def __str__(self):
        return self.username
    
class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE,related_name='profile')
    full_name = models.CharField(max_length=100, null=True)
    occupation = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='media/profile', null=True)

    def __str__(self):
        return self.full_name
    
class BookModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
    total_pages = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name
    
class SellBookModel(models.Model):
    sell_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatic calculation logic
        self.total = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        # Fixed: Changed selled_by to sell_by to match the field name above
        return f"{self.book.book_name} sold by {self.sell_by.username}"