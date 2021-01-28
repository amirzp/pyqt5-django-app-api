from rest_framework import viewsets, permissions, mixins
from django.contrib.auth.models import User
from .models import Contact, UserModel
from .serializers import ContactSerializers, UserSerializers, CreateSerializer


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class CreateUserView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = UserModel.objects.all()
    serializer_class = CreateSerializer
    # permission_classes = [permissions.AllowAny]
