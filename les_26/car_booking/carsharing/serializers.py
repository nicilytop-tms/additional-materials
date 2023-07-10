from rest_framework import serializers

from carsharing.models import Auto, AutoModel, Brand


class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class AutoModelSerializer(serializers.Serializer):
    brand = BrandSerializer()
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return AutoModel.objects.create(**validated_data)


class AutoSerializer(serializers.Serializer):
    vin_code = serializers.CharField(max_length=10)
    status = serializers.ChoiceField(Auto.STATUSES, default=Auto.STATUSES[0])
    auto_model = AutoModelSerializer()
    user = serializers.CharField(max_length=255, required=False)

    def create(self, validated_data):
        return Auto.objects.create(**validated_data)
