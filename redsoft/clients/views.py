from rest_framework import generics
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import ClientSerializer
from .models import Client, Photo
from rest_framework import statu
from django.http import Http404


class ClientViewSet(ViewSet):
    serializer_class = ClientSerializer

    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def post(self, request):
        """
        Creates a new Client object.
        Name, Surname, birth_date, gender, photo.
        Returns object.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        object = self.get_object(pk)
        object.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        queryset = Client.objects.all()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        object = self.get_object(pk)
        serializer = self.serializer_class(object, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)