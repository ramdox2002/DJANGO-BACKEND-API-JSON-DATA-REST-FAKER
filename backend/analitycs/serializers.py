from rest_framework import serializers

from .models import ViewData


class ViewDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewData
        fields = "__all__"

class ViewDataPOSTSerializer(serializers.ModelSerializer):
    screen_resolution = serializers.CharField()
    time_on_site = serializers.DurationField()
    actions_taken = serializers.CharField()

    class Meta:
        model = ViewData
        fields = '__all__'