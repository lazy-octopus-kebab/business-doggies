from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers

from ..models import User, ClientMore, SitterMore


class ClientMoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientMore
        fields = []


class SitterMoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitterMore
        fields = ['description']


class UserSerializer(serializers.ModelSerializer):
    """Serializer of the User model"""

    url = serializers.SerializerMethodField()
    more = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'url',
            'email',
            'phone_number',
            'first_name',
            'last_name',
            'image',
            'more',
        ]

    def get_url(self, obj):
        """Method field for User absolute url"""
        return obj.get_absolute_url()

    def get_more(self, obj):
        """
        Returns additional fields if user is Client and/or Sitter
        """
        try:
            serializer = dict()
            if obj.is_client:
                serializer = ClientMoreSerializer(obj.clientmore).data
            elif obj.is_sitter:
                serializer = SitterMoreSerializer(obj.sittermore).data
        except ObjectDoesNotExist:
            return None

        return serializer
