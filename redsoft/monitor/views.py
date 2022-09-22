from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import os
import json


class MemoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cur_path = os.path.dirname(__file__)
        file_path = cur_path[:-7] + '/source/nohup.out'
        with open(file_path, 'r') as file:
            data = file.readlines()[-1]

        return Response(json.loads(data),
                        status=status.HTTP_200_OK,
                        )