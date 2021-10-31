from rest_framework.views import APIView
from rest_framework.response import Response


class Echo(APIView):
    def get(self, request):
        return Response({'msg': 'hello world 1'})

class Echo2(APIView):
    def get(self, request):
        return Response({'msg': 'hello world 2'})
