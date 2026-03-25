from rest_framework import serializers
from django.utils.html import escape
from .models import Notes

class Noteserializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'title', 'content', 'created_at', 'updated_date']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError('Заголовок не может быть пустым')
        return escape(value.strip())
    
    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError('Не может быть пустым')
        return escape(value.strip())
    
class NoteCreate(Noteserializer):
    pass

class NoteupdateSerializer(Noteserializer):
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)