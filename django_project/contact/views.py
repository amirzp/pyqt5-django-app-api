from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializers


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
