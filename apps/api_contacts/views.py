from rest_framework.viewsets import ModelViewSet

from apps.contacts.models import Contact
from .serializers import ContactsSerializer


class ContactsViewSet(ModelViewSet):
    serializer_class = ContactsSerializer
    queryset = Contact.objects.all()
