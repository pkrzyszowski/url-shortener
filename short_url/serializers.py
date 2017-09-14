import random

from rest_framework import serializers

from .models import Url, ShortUrl

class ShortUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortUrl
        fields = ('__all__')
        read_only_fields = ('id', )

    def to_representation(self, obj):
        self.fields['url'] = UrlSerializer()
        return super().to_representation(obj)

class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = ('__all__')
        read_only_fields = ('id', )

    def create(self, validated_data):
        url = super().create(validated_data)
        if 'rtest' in str(url.url):
            short = 'short.url/' + ''.join(random.choice('0123456789') for i in range(8)) + "R"
        else:
            short = 'short.url/' + ''.join(random.choice('0123456789') for i in range(8))
        ShortUrlSerializer().create(validated_data={'url': url, 'short_url':short})
        return url
