from django.db import models

class Profile(models.Model):
   GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
        ('not_specified', 'not_specified')  # デフォルトとして追加
    ]
   name = models.CharField(max_length=64, blank=False, null=False)
   checked = models.BooleanField(default=False)
   gender = models.CharField(max_length=64, choices=GENDER_CHOICES, default='not_specified', blank=True, null=True)
   comments = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        default='あなたのことをありったけ書いてください！'
    )
   items = models.IntegerField(default=0)
   age = models.IntegerField(default=0)
   place = models.TextField(
         max_length=1000, 
         blank=True, 
         null=True,
         default='日本'
    )
   image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # 新しいフィールド

   def __str__(self):
       return self.name
