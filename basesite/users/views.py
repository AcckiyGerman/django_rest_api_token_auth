from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User


# Create your views here.
@api_view(['GET'])
def index(request):
    return Response({'info': "this is an users auth app"})


@api_view(['POST'])
def register(request):
    # get user credentials
    try:
        username = request.data['username']
        password = request.data['password']
    except KeyError:
        Response({
            'error': 'you need to provide a username and password fields in the request'
        }, status=400)

    # check that user does not exists
    try:
        User.objects.get_by_natural_key(username=username)
        Response({'error': 'this username is already taken.'})
    except User.DoesNotExist:
        # create an user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        # return token
        return Response({'token': user.auth_token.key, 'status': 'success'})


@api_view(['POST'])
def login(request):
    return Response(request.data)


@api_view(['GET'])
def protected(request):
    return Response(request.data)
