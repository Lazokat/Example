from rest_framework.serializers import *
from rest_framework.generics import *
from .models import *

class BlogSerializer(ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'