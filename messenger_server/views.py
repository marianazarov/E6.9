from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from .models import UserProfile, Room
from .serializers import RoomSerializer, UserProfileSerializer


def api_users(request):
    if request.method == 'GET':
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)


class ApiUsers(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ApiRooms(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
