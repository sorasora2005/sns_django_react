from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    #image = serializers.ImageField(use_url=False)  # use_urlをFalseに設定→これだとファイル送られてきたときになんかエラーなる

    class Meta:
        model = Profile
        fields = ('id', 'name', 'checked', 'gender', 'comments', 'items', 'age', 'place', 'image')