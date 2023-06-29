from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    """
    A class to list contact messages.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
