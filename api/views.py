from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
import json

from .models import Item, UserProfile, VendorType, Type
from api import permissions
from .serializers import ItemSerializers, UserSerializer, VendorSerializer, TypeSerializer

# Create your views here.
# Rest Framework viewset Class


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializers
    queryset = Item.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,
                          permissions.UpdateOwnItem,
                          )


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

    # below will bring all the Items which has our user in it.
    # http://127.0.0.1:8000/api/users/1/get_items/
    @action(detail=True, methods=['GET'])
    def get_items(self, request, pk=None):
        items = Item.objects.filter(user=pk)

        serializer = ItemSerializers(items, many=True)
        return Response({'response': serializer.data})
    # def get_items(self, request, pk=None):
    #     items = Item.objects.filter(user=1)
    #     user_items = []
    #     for item in items:
    #         user_items.append(item)
    #         print({'item': json.dumps(user_items)})

    #     return Response({"Items_Details": "user_items"})


class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    queryset = VendorType.objects.all()


# User Login API VIEW

class UserLoginApiView(ObtainAuthToken):
    ###Handle creating user authentication tokens###
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
