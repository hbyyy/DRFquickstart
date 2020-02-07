from django.contrib.auth.models import User, Group
# Create your views here.
from rest_framework import viewsets

from quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    user 를 확인하거나 편집할 수 있는  API endpoint
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    Group을 확인하거나 편집할 수 있는 API endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer