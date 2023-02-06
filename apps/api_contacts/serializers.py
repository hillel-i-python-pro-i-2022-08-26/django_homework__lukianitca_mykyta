from rest_framework.serializers import HyperlinkedModelSerializer

from apps.contacts.models import Contact


class ContactsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "url",
            "pk",
            "contact_name",
            "phone_number",
            "contact_photo",
            "birth_date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["pk", "created_at", "updated_at"]
