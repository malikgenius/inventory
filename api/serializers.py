from rest_framework import serializers
from .models import Item, Type, VendorType, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'no_of_items',
                  'item_details',
                  'is_active', 'is_staff', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        ### Create and return a new user ###

        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']

        )
        return user

    # def get(self, pk):
    #     pass


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorType
        fields = ['id', 'vendor_name']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']


class ItemSerializers(serializers.ModelSerializer):
    vendor = VendorSerializer(many=True)
    Type = TypeSerializer()
    user = UserSerializer()

    class Meta:
        model = Item
        fields = ['id', 'item_model', 'Type', 'vendor', 'user',
                  'purchased_date', 'condition', 'is_assigned', 'description']
