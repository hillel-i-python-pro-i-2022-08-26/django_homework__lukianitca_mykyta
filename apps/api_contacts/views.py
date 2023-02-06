from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import ContactsSerializer


class ContactsViewSet(ModelViewSet):
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.contacts.all()
