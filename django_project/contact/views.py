from rest_framework import viewsets, permissions
from .models import Contact
from .serializers import ContactSerializers


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
