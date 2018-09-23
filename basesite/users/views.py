from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication


# Create your views here.
@api_view(['GET'])
def index(request):
    return Response({
        'info': "This is an authorization API. "
                "You can register new user or login to get a security token. "
                "Token is used to get protected resources.",
        'endpoints': {
            'users/register/': {
                'info': 'Used to register a new user. Use POST request.',
                'sample json request': {'username': 'some_user', 'password': 'his_password'},
                'sample json response': {
                    "token": "ff03abd808408d9b3d15ac803960b2da7fea7770",
                    "status": "success"
                }
            },
            'users/login/': {
                'info': 'Login with login/pass to get the token. Use POST request.',
                'sample json request': {'username': 'some_user', 'password': 'his_password'},
                'sample json response': {
                    "token": "ff03abd808408d9b3d15ac803960b2da7fea7770",
                    "status": "success"
                }
            },
            'users/protected/': 'To get the protected info you should set'
                                " 'Authorization: Token ~your_token~' in HEADERS of your GET request."
        }
    })


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
        'message': 'Congratulations: this is a protected information,'
                   ' that means you set your secure token correctly!',
        'username': request.user.username
    })
