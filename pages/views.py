from django.shortcuts import render
from .serializers import BlogSerializer
from rest_framework.generics import *
# Create your views here.
from .models import *
def Pageview(request):
    return render(request,'pages/index.html')

class Create(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

