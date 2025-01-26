from rest_framework import serializers

from acconts.forms import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)
