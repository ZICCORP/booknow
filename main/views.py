from django.shortcuts import render

def testing(request):
    print(request)
    raise Exception
