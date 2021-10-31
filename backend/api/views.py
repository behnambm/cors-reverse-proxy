from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import redis

r = redis.Redis(host='127.0.0.1', port=6379)

# set initial value for `count`
r.set('count', 1)


class Echo(APIView):
    def get(self, request):
        return Response({'msg': 'hello world 1'})

class Echo2(APIView):
    def get(self, request):
        return Response({'msg': 'hello world 2'})


class AddOne(APIView):
    def post(self, request):
        # some key to determine that the request is authorized
        auth_key = '123456'

        key = request.headers.get('Authorization')

        if key and key == auth_key:
            count = int(r.get('count').decode()) + 1
            r.set('count', count)

            return Response({'count': count})

        return Response(
            {'message': 'you are not authorized'}, 
            status=status.HTTP_403_FORBIDDEN,
        )

