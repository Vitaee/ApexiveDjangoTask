# Third Party
from core.serializers import UserAuthSerializer, UserDetailSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.core import serializers

# Django Stuff
from django.db import models
from django.db.models import F, Value
from django.db.models.functions import Concat
from django.http import HttpResponse

# Rest Framework
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Local Folder
from .models import User

"""
Basic Authentication
"""


class UserRegistrationView(CreateAPIView):
    serializer_class = UserAuthSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        user = User.objects.filter(username=request.data["username"])
        if user.exists():
            user = authenticate(
                username=request.data["username"], password=request.data["password"]
            )
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
            else:
                return Response(
                    {"error": "Invalid credentials"}, status=status.HTTP_403_FORBIDDEN
                )
        else:
            user = User.objects.create(
                username=request.data["username"],
                password=make_password(request.data["password"]),
            )
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})


class UserLoginView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        user = authenticate(
            username=request.data["username"], password=request.data["password"]
        )
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class UserView(RetrieveAPIView, APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            data={
                "data": {"results": [serializer.data]},
                "error_message": None,
                "error_type": None,
            },
            status=status.HTTP_200_OK,
        )

    def get_object(self):
        return self.request.user


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def UserFilter(request):
    search_term = request.GET.get("q")

    data = (
        User.objects.annotate(
            full_name_address=Concat(
                F("first_name"),
                Value(" "),
                F("last_name"),
                Value(" "),
                F("address"),
                output_field=models.TextField(),
            )
        )
        .annotate(search=SearchVector("first_name", "last_name", "address"))
        .annotate(rank=SearchRank("search", SearchQuery(search_term)))
        .filter(search=SearchQuery(search_term))
        .order_by("-rank", "date_of_birth")
    )

    data = serializers.serialize(
        "json", data, fields=("first_name", "last_name", "address")
    )

    return HttpResponse(data, content_type="application/json")
