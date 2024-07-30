from django.db.migrations import serializer
from rest_framework import serializers

from app.models import students


class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'