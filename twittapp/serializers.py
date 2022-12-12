from rest_framework import serializers

from profileapp.models import Profile

from .models import Twitt

MAX_TWITT_LENGTH = 512
TWITT_ACTION_OPTIONS = ['like']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'name', 'title', 'desc', 'profile_img']

class TwittReserializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model = Twitt
        fields = ['user', 'timestamp']

class TwittSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Twitt
        fields = ['id', 'content', 'likes', 'timestamp']

    def get_likes(self, obj):
        return obj.likes

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