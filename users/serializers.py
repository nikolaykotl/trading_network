from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
     #   password = validated_data.pop('password')
     #   user = User(**validated_data)
     #   user.set_password(password)
     #   user.save()
     #   return user
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'password')
        extra_kwargs = {'password': {'write_only': True}}
