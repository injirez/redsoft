from rest_framework import serializers
from .models import Client, Photo
from source.image_crop import crop


class PhotoSerializer(serializers.ModelSerializer):
    """ Serializer for photo model """
    class Meta:
        model = Photo
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    """ Serializer for Client model with OneToOne """
    photo = PhotoSerializer()
    left = serializers.IntegerField(allow_null=True, write_only=True)
    top = serializers.IntegerField(allow_null=True, write_only=True)
    right = serializers.IntegerField(allow_null=True, write_only=True)
    bottom = serializers.IntegerField(allow_null=True, write_only=True)

    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data, *args, **kwargs):
        photo_data = validated_data.pop('photo')
        photo = Photo.objects.create(**photo_data)
        left = validated_data.pop('left')
        top = validated_data.pop('top')
        right = validated_data.pop('right')
        bottom = validated_data.pop('bottom')
        crop(str(photo.file), left, top, right, bottom)
        client = Client.objects.create(photo=photo, **validated_data)

        return client

