from rest_framework import serializers

from retail.models import Trading_network


class Trading_networkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trading_network
        fields = '__all__'
        extra_kwargs = {
            'level_0': {'read_only': True},
            'level_1': {'read_only': True},
            'level_2': {'read_only': True},
        }
