from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from funding.apps.user.serializers import UserSerializer
from .models import *
from drf_yasg.utils import swagger_serializer_method
from funding.apps.core.components.date import DateComponent


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class ShopPostSerializer(ModelSerializer):
    item = serializers.SerializerMethodField()
    poster = serializers.SerializerMethodField()
    participant_count = serializers.SerializerMethodField()
    all_funding_amount = serializers.SerializerMethodField()
    d_day = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'poster',
            'title',
            'content',
            'item',
            'poster_name',
            'status',
            'participant_count',
            'all_funding_amount',
            'd_day'
        ]

    @swagger_serializer_method(serializer_or_field=ItemSerializer)
    def get_item(self, obj):
        return ItemSerializer(obj.item).data
    
    @swagger_serializer_method(serializer_or_field=UserSerializer)
    def get_poster(self, obj):
        return UserSerializer(obj.poster).data
    
    def get_participant_count(self, obj):
        return obj.participants.count()

    def get_all_funding_amount(self, obj):
        return obj.item.price * obj.participants.count()
    
    def get_d_day(self, obj):
        final_date_comp = DateComponent(obj.final_date)
        return final_date_comp.get_d_day()


class ShopPostCreateSerializer(ModelSerializer):
    """
    ## validation 목록
    * final_date
    DateComponentValidationError
    """

    class Meta:
        model = Post
        fields = [
            'item',
            'poster', 
            'title', 
            'content', 
            'poster_name', 
            'final_date'
        ]


class ItemCreateSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = [
            'price', 'target_amount'
        ]


class PurchaseCreateSerializer(ModelSerializer):

    class Meta:
        model = Purchase
        fields = ['user_id', 'production']


class ParticipantCreateSerializer(ModelSerializer):

    class Meta:
        model = Participant
        fields = [
            'user',
            'post_id',
            'purchase',
        ]
