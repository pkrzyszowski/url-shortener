# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_delete
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.dispatch import receiver

from .models import Url
from .serializers import UrlSerializer, ShortUrl, ShortUrlSerializer


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    @detail_route(methods=['head'])
    def search_url(self, request, pk=None):
        """ url do szukania w bazie"""
        url = self.get_object()
        if url in self.queryset:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ShortUrlViewSet(viewsets.ModelViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer

    @detail_route(methods=['get'])
    def redirect_url(self, request, pk=None):
        """ url do przekierowania"""
        url = self.get_object()
        url_pk = url.url.pk
        if url in self.queryset:
            data = {'URL': reverse('short_url:url-detail', kwargs={'pk': url_pk}, request=request)}
            return Response(data, status=status.HTTP_302_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @receiver(post_delete, sender='short_url.ShortUrl')
    def post_delete_url(sender, instance, *args, **kwargs):
        if instance.url:
            instance.url.delete()
