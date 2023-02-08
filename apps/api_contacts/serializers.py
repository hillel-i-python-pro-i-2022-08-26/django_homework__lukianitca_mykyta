from rest_framework import serializers

from apps.contacts.models import Contact


class ContactsSerializer(serializers.HyperlinkedModelSerializer):
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
            "user_id",
        ]
        read_only_fields = ["pk", "created_at", "updated_at", "user_id"]
