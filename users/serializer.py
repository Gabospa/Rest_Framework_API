from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = [ 'id', 'first_name', 'last_name', 'username', 'email', 'password', 'birthdate']

    def create(self, validated_data):
        person = Persona.objects.create(**validated_data)
        return person

    def update(self, instance, validated_data):
        
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.save()
        
        return instance