from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import WeatherSerializer
from rest_framework import status
import requests as req


class WeatherAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WeatherSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data['city'])
        url_yandex = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{request.data['city']}/{request.data['date']}?unitGroup=metric&include=alerts%2Cdays&key=BP8KPU35BEDZTTJCAMTNQVRX4&contentType=json"
        req.packages.urllib3.disable_warnings()
        resp = req.get(url_yandex, verify=False)
        data = resp.json()

        return Response(data,
            status=status.HTTP_200_OK,
        )

