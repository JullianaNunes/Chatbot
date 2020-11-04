from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
# from .models import *
# from .forms import *
# import email


def inicial(request):
    return render(request, 'drummond/site.html')