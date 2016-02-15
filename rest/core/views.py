from django.shortcuts import render
from rest_framework import authentication, permissions, viewsets
from .models import Produto
from .forms import ProdutoFilter
from .serializers import ProdutoSerializer


def index(request):

    return render(request, 'base.html')


# modificado views
class ProdutoViewSet(viewsets.ModelViewSet):

    queryset = Produto.objects.order_by('preco')
    serializer_class = ProdutoSerializer
    filter_class = ProdutoFilter
    search_fields = ('nome', )
    ordering_fields = ('preco', )

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
        # permissions.IsAuthenticatedOrReadOnly,
    )
