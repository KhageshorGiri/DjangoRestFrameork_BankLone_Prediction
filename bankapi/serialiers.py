
from rest_framework import serializers
from bankapi.models import BankLone

class BankLoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankLone
        fields = "__all__"
