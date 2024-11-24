from rest_framework import serializers
from .models import *
from .permissions import *

class Account_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'date_joined', 'account_cpf', 'account_type', 'password', 'email']
        extra_kwargs = {'password':{'write_only': True}}
        read_only_fields  = ['account_type', 'id', 'date_joined']

class Luggage_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Luggage
        fields = '__all__'

    def validate_luggage_consumer(self, luggage_consumer):
        if luggage_consumer.account_type == 'cn':
            return luggage_consumer
        else:
            raise serializers.ValidationError('\'luggage_consumer\' must be a consumer (cn) Account).')
        
    def create(self, validated_data):
        luggage = Luggage(**validated_data)
        luggage.save()
        luggage_stage = Luggage_Stage(luggage_stage_luggage=luggage).save()
        return luggage

class Luggage_Stage_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Luggage_Stage
        fields = '__all__'
        
class Ticket_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'