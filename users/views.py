from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.

class SignupView(APIView):

    def post(self, request):
        name = request.data.get("name")
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects.create_user(
            first_name=name,
            username=username,
            email=email,
            password=password,
        )
        print(user)
        return Response("Signup success", status=HTTP_201_CREATED)


class UserDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {}
        data["name"] = user.first_name
        return Response(data, status=HTTP_200_OK)