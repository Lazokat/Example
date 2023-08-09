from django.http import HttpResponse

def f(request):
    return HttpResponse('<b>salom</b>')