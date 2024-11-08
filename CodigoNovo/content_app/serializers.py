from rest_framework import serializers
from .models import Member,Convite,Cadastro,SistemaConvite

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class ConviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convite
        fields = '__all__'

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = '__all__'

class SistemaConviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SistemaConvite
        fields = '__all__'