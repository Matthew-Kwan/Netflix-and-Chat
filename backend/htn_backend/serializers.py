from rest_framework import serializers
from .models import Message, Show

class ShowSerializer(serializers.ModelSerializer):
  class Meta:
    model = Show
    fields = ['unique_id', 'description']

  def create(self, validated_data):

    return Show.objects.create(**validated_data)

class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    fields = ['id', 'content', 'time', 'username', 'show']

  def create(self, validated_data):
    return Message.objects.create(**validated_data)
