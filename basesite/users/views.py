from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication


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
        return Response({
            'error': 'you need to provide a username and password fields in the request'
        }, status=400)

    # check that user does not exists
    try:
        User.objects.get_by_natural_key(username=username)
        return Response({'error': 'this username is already taken.'})
    except User.DoesNotExist:
        # create an user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        # return token
        return Response({'token': user.auth_token.key, 'status': 'success'})


@api_view(['POST'])
def login(request):
    try:
        username = request.data['username']
        password = request.data['password']
    except KeyError:
        Response({
            'error': 'you need to provide a username and password fields in the request'
        }, status=400)

    try:
        user = User.objects.get_by_natural_key(username=username)
    except User.DoesNotExist:
        return Response({'error': 'No such user'})

    if user.check_password(password):
        return Response({'token': user.auth_token.key, 'status': 'success'})
    return Response({'error': 'invalid credentials'})


@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated,))
def protected(request):
    return Response({
        'message': 'that is protected view',
        'username': request.user.username
    })
