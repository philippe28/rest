import django_filters
from django.contrib.auth import get_user_model
from .models import Produto
      
      
User = get_user_model()       

#modificado form
class ProdutoFilter(django_filters.FilterSet):
    
    data_min = django_filters.DateFilter(name='release', lookup_type='gte')
    data_max = django_filters.DateFilter(name='release', lookup_type='lte')
    
    class Meta:
        model = Produto
        fields = ('data_min', 'data_max', )

