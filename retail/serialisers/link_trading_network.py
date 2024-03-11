from rest_framework import serializers

from retail.models import Link_trading_network


class Link_trading_networkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link_trading_network
        fields = '__all__'
        extra_kwargs = {
            'debt': {'read_only': True},
        }
