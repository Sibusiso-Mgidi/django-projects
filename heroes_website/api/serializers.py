"""
- Serialization - is the process of converting a model into a JSON file.
- Using a serializer, we can specify what fields should be presented inot a JSON representation of the file.
- The serializer will turn our heroes into a JSON representation so the API user can parse them.
"""
from .models import Hero
from rest_framework import serializers

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ("id","name", "nickname")
        

