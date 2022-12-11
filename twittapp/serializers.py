from rest_framework import serializers

from .models import Twitt

MAX_TWITT_LENGTH = 512
TWITT_ACTION_OPTIONS = ['like']

class TwittSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    timestamp = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Twitt
        fields = ['id', 'content', 'likes', 'timestamp']
    
    def get_likes(self, obj):
        return obj.likes
    
    def get_timestamp(self, obj):
        return obj.timestamp

    def validate_content(self, attrs):
        if len(attrs) > MAX_TWITT_LENGTH:
            raise serializers.ValidationError("Maximum content length exceeded.")
        return attrs

class TwittActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, attrs):
        attrs = attrs.lower().strip()
        if not attrs in TWITT_ACTION_OPTIONS:
            raise serializers.ValidationError("Invalid action.")
        return attrs