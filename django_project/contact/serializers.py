from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Contact


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
        )


# UserModel = get_user_model()


class CreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'is_staff', 'is_active')

    def create(self, validated_data):
        user = super(CreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
