from typing import Generic
from django.shortcuts import render
from .models import Link
from .serializers import LinkSerializer
from rest_framework import generics


# Create your views here.

class PostListApi(generics.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

    