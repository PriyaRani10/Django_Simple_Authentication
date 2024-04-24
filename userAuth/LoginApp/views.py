from rest_framework.views import APIView
import jwt, datetime
from rest_framework.generics import ListCreateAPIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .serializers import UserSerializers, UserDetailSerializer
from .models import LoginUser

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer=UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']

        user=LoginUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("user not found!")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")
        payload={
        'id':user.id,
        'expire': datetime.datetime.now().isoformat(),
        'iat':datetime.datetime.now()
    }
        token=jwt.encode(payload,'secret',algorithm='HS256')
        response=Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={
            'jwt':token,
            'message':"successful!"
        }
        return response
    

class LogoutView(APIView):
    '''
    This class is for implementing logout view
    '''
    def post(self,request):
        response=Response()
        response.delete_cookie('jwt')
        response.data={
            'message':"Successfully Logout!"
        }
        return response
   
class UserView(ListCreateAPIView):
    '''
    This class is for implementing logout view
    '''
    queryset = LoginUser.objects.all()
    serializer_class = UserDetailSerializer
            


