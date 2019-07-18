from django.contrib import admin
from django.urls import path, include
# from . import views
# from .views import Another
from .views import ItemViewSet, UserViewSet, VendorViewSet, UserLoginApiView
# from .views import ItemSerializers
from rest_framework import routers

router = routers.DefaultRouter()
router.register('items', ItemViewSet)
router.register('users', UserViewSet)
router.register('vendor', VendorViewSet)
urlpatterns = [
    # path('', views.first),
    # path('items', views.second),
    # # Below is from the class
    path('', include(router.urls)),
    path('login/', UserLoginApiView.as_view()),

]
