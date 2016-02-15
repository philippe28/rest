from datetime import date
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Produto


User = get_user_model()


class ProdutoSerializer(serializers.ModelSerializer):
    
    nome = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, required=False, allow_null=True,
        queryset=User.objects.all())

    class Meta:
        model = Produto
        fields = ('id', 'nome' , 'cpu', 'memoria', 'disco', 'so' , 'preco', 'provedores' , 'release' )

    def create(self, validated_data):

        return nome.objects.create(**validated_data)

