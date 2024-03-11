from rest_framework import serializers

from retail.models import Debt


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = '__all__'
        extra_kwargs = {
            'debt': {'read_only': True},
            }
