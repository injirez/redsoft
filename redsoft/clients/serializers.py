from rest_framework import  serializers
from .models import Client, Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer()

    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        photo_data = validated_data.pop('photo')
        photo = Photo.objects.create(**photo_data)
        client = Client.objects.create(photo=photo, **validated_data)

        return client

