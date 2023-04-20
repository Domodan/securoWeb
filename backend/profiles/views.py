from django.contrib.auth import get_user_model
#Import all the models
from .models import UsersModel
from rest_framework import views, permissions, status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponseForbidden

from .serializers import ObtainTokenSerializer,UserSerializer
from .authentication import JWTAuthentication

User = get_user_model()

class ObtainTokenView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email_or_phone_number = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        user = UsersModel.objects.filter(email=email_or_phone_number).first()
        if user is None:
            user = UsersModel.objects.filter(phone_number=email_or_phone_number).first()

        if user is None or not user.check_password(password):
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate the JWT token
        jwt_token = JWTAuthentication.create_jwt(user)

        return Response({'token': jwt_token})

#Class to Manage Transaction Types
class ProfilesApi(views.APIView):
    authentication_class = JSONWebTokenAuthentication
    permission_classes = (IsAdminUser,)
    #authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        user=request.user
        item=UserSerializer(data=request.data)
        if item.is_valid():
            new_item=item.save()
            if new_item:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'message': 'Record Created successfully',
                }
                return Response(response,status=status_code)
        return Response(item.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        queryset = UsersModel.objects.all().order_by('date_joined')
        serializer_class = UserSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status_code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
# #Class List Specific 
# class TransactionTypesDetailApi(APIView):
#     permission_classes = (AllowAny,)
#     #authentication_class = JSONWebTokenAuthentication
#     def get(self,request,id):
#         try:
#             queryset = TransactionTypeModel.objects.filter(transaction_type_id=id)
#             serializer_class = UpdateTransactionTypeSerializer(queryset, many=True)
            
#             status_code = status.HTTP_200_OK
#             response = {
#                 'success' : 'True',
#                 'status_code' : status_code,
#                 'data': serializer_class.data,
#             }
#             return Response(response,status=status_code)
#         except queryset.DoesNotExist:
#             status_code = status.HTTP_404_NOT_FOUND
#             response = {
#                     'success' : 'False',
#                     'status_code' : status_code,
#                     'Message': "Data Not Found",
                    
#             }
#             return Response(response,status=status_code)
#     #Update the Data
#     def put(self,request,id):
#         queryset = TransactionTypeModel.objects.filter(transaction_type_id=id).first()
#         serializer_class = UpdateTransactionTypeSerializer(queryset, data=request.data)
#         if serializer_class.is_valid(raise_exception=True):
#             update=serializer_class.save()
#             if update:
#                 status_code = status.HTTP_200_OK
#                 response = {
#                     'success' : 'True',
#                     'status_code' : status_code,
#                     'Message': "Data Updated",
#                     'data': serializer_class.data,
#                 }
#             return Response(response,status=status_code)
#         return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)