# inquiries/serializers.py
from rest_framework import serializers
from .models import SchoolPartnershipInquiry
from .models import EnrollmentInquiry

class SchoolPartnershipInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolPartnershipInquiry
        fields = '__all__'


class EnrollmentInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollmentInquiry
        fields = "__all__"