from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200,default="Title")
    # type = models.CharField(max_length=40)
    isbn = models.CharField(max_length=35,default="ISBN0000")
    author = models.CharField(max_length=100,default="Author")
    av_count = models.IntegerField(default=0)

    def __str__ (self):
        return f"{self.isbn} : {self.title}"

class User(models.Model):
    isbn = models.CharField(max_length=35,default="ISBN0000")
    name = models.CharField(max_length=200,default="User name")
    mail_id = models.CharField(max_length=50,default="example@example.com")
    phno = models.BigIntegerField(default=0000000000)
    resver_id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)

    def __str__ (self):
        return f"{self.name} : {self.phno}"


# @receiver(pre_save, sender=User)
# def decrement_book(sender, instance, **kwargs):
#     if User.objects.filter(pk=instance.resver_id).exists():
#         print("Hello World!")
#         curr_book = Book.objects.get(isbn=User.objects.get(pk=instance.resver_id).isbn)
#         curr_book.av_count -= 1 
#         curr_book.save()
#         return