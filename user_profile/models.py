from django.db import models

class Profile(models.Model):
   GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
        ('not_specified', 'not_specified')  # デフォルトとして追加
    ]
   name = models.CharField(max_length=64, blank=False, null=False)
   checked = models.BooleanField(default=False, blank=True, null=True)
   gender = models.CharField(max_length=64, choices=GENDER_CHOICES, default='not_specified', blank=True, null=True)
   comments = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        default='あなたのことをありったけ書いてください！'
    )
   items = models.IntegerField(default=0, blank=True, null=True)
   age = models.IntegerField(default=0, blank=True, null=True)
   place = models.TextField(
         max_length=1000, 
         blank=True, 
         null=True,
         default='日本'
    )
   image = models.ImageField(upload_to='profile_images/', blank=True, null=True, default='profile_images/dfl.png')  # 新しいフィールド

   def __str__(self):
       return self.name
