from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Usuario, Setor, Polo, Endereco


UserModel = get_user_model()
class EnderecoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Endereco
        fields = ( "pk","endereco", "uf", "cidade","bairro", "numero", "complemento", "cep",)

class PoloSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = Polo
        fields = ( "pk","polo", "tipo", "endereco","subordinado",)

class SetorSerializer(serializers.ModelSerializer):
    polo = PoloSerializer()

    class Meta:
        model = Setor
        fields = ("pk","setor", "sigla", "polo","subordinado",)

class UserSerializer(serializers.ModelSerializer):
    #usuarios = serializers.StringRelatedField()

    class Meta:
        model = UserModel
        fields = ("pk","username", "first_name", "last_name",)

class UsuarioSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()
    setor = SetorSerializer()
    class Meta:
        model = Usuario
        fields = ("pk","usuario","setor",)

