from django.shortcuts import render

# Create your views here.
# inquiries/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SchoolPartnershipInquirySerializer
from .serializers import EnrollmentInquirySerializer

@api_view(['POST'])
def school_partnership_inquiry(request):
    serializer = SchoolPartnershipInquirySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"success": True, "message": "Inquiry submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(
        {"success": False, "errors": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
def enrollment_inquiry(request):
    serializer = EnrollmentInquirySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"success": True, "message": "Enrollment inquiry submitted"},
            status=status.HTTP_201_CREATED
        )

    return Response(
        {"success": False, "errors": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )