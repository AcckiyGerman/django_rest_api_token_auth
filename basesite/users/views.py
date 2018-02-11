from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def index(request):
    return Response({'info': "this is an users auth app"})


@api_view(['POST'])
def register(request):
    return Response(request.data)


@api_view(['POST'])
def login(request):
    return Response(request.data)


@api_view(['GET'])
def protected(request):
    return Response(request.data)
