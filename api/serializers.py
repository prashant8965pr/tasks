from rest_framework import serializers
from .models import CardInfo


class CardInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardInfo
        fields = ["card_number"]


class CardInfoListSerializer(serializers.ModelSerializer):
    hits = serializers.IntegerField()

    class Meta:
        model = CardInfo
        fields = ["card_number", "hits"]


class AllCardInfoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardInfo
        fields = ["id", "card_number", "created_at", "updated_at"]