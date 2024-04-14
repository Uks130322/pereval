from .models import User, PerevalAdded, Level, Coords, Image
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin
from rest_framework import serializers


class UserSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'fam', 'name', 'otc', 'phone']
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        user, created = User.objects.get_or_create(**validated_data)
        return user


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['id', 'winter', 'spring', 'summer', 'autumn']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['id', 'latitude', 'longitude', 'height']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'data', 'title']


class PerevalSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    level = LevelSerializer()
    coords = CoordsSerializer()
    images = ImageSerializer(many=True, allow_null=True)

    class Meta:
        model = PerevalAdded
        fields = ['id', 'status', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time',
                  'user', 'coords', 'level', 'images']
        extra_kwargs = {
            'id': {'read_only': True},
            'status': {'read_only': True},
        }
