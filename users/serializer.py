from gettext import install
from pyexpat import model
from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        # Nu mai afisa parola
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Functie pentru criptarea parolei
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        insatance = self.Meta.model(**validated_data) # Salveaza datele fara parola
        # Salveaza parola criptata
        if password is not None:
            insatance.set_password(password)
        insatance.save()
        return insatance