from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import BookingInfo, Listing, Reservation

class BookingInfoSerializer(serializers.ModelSerializer):
    
    listing_type = SerializerMethodField()
    title = SerializerMethodField()
    country = SerializerMethodField()
    city = SerializerMethodField()

    class Meta:

        model = BookingInfo
        fields = ["listing_type", "title", "country", "city", "price"]

    def get_listing_type(self, booking_info):
        try:
            return booking_info.listing.listing_type
        except:
            return ""

    def get_title(self, booking_info):
        try:
            return booking_info.listing.title
        except:
            return ""

    def get_country(self, booking_info):
        try:
            return booking_info.listing.country
        except:
            return ""

    def get_city(self, booking_info):
        try:
            return booking_info.listing.city
        except:
            return ""
