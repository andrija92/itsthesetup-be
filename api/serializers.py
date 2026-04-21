from api.models import Car, Game, Setup, SetupData, Track, User
from rest_framework import serializers

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class SetupDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetupData
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class SetupDetailSerializer(serializers.ModelSerializer):
    setup_data = SetupDataSerializer()
    user = PublicUserSerializer()
    track = TrackSerializer()
    car = CarSerializer()
    game = GameSerializer()
    
    class Meta:
        model = Setup
        fields = '__all__'


class SetupListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    track = serializers.StringRelatedField()
    car = serializers.StringRelatedField()
    game = serializers.StringRelatedField()

    class Meta:
        model = Setup
        fields = ['id', 'title', 'user', 'created_at', 'rating', 'rating_count', 'track', 'car', 'game', 'downloads_count']
