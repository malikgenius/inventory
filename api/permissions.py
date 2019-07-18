from rest_framework import permissions
from rest_framework.response import Response


# Below Class is with SAFE_METHODS means users can create new posts / items and can see all the others posts but cant edit which they have not made it.
class UpdateOwnProfile(permissions.BasePermission):
    ### Allow user to edit their own profile ####

    def has_object_permission(self, request, view, obj):
        ## Check if user is trying to edit their own profile ###
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.id == obj.id or request.user.is_superuser:
            return True
        # return obj.id == request.user.id


### Only Admins and Users who are assinged to the Item can update it ###
class UpdateOwnItem(permissions.BasePermission):

    ### only Admins Can see all the Items and not others-- its not for single OBJ but for the whole set of Items ###

    def has_permission(self, request, view):
        # if request.user.is_superuser:
        if request.user.is_staff:
            return True

    # Below is only for single Ojb, but if has_permission is not allewed for normal users, means they cant reach to this point as well...

    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.user.id or request.user.is_staff:
            return True


# below is only for auth users has_permission function has to be in place ..
class OnlyAdminRoute(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.IsAdminUser:
            return True
