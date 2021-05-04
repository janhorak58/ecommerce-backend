from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only = True)
    _id = serializers.SerializerMethodField(read_only = True)
    isAdmin = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        fields = ["_id", "username", "email", "name", "isAdmin"]

    def get_name(self, o):
        name = str(o.first_name) + " " + str(o.last_name)
        if name == "":
            name = o.email
        return name

    def get__id(self, o):
        _id = o.id
        return _id

    def get_isAdmin(self, o):
        return o.is_staff

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = User
        fields = ["_id", "username", "email", "name", "isAdmin", "token"]
    
    def get_token(self, o):
        token = RefreshToken.for_user(o)
        return str(token.access_token)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

