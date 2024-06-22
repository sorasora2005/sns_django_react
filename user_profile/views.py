from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend]
    fileterset_fields = ('name','id')

    @action(detail=True, methods=['post'], url_path='update_image')
    def update_image(self, request, pk=None):
        """
        カスタムエンドポイントで画像を更新
        """
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render

def user_profile_list(request):
    Profiles = Profile.objects.all()
    return render(request, 'user_profile/user_profile_list.html', {'Profiles': Profiles})


