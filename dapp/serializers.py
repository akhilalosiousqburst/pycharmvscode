from rest_framework import serializers
from dapp.models import Dapp


class DappSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dapp
        fields = ('id', 'name', 'email', 'phonenumber', 'description')
        