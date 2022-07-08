from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def help(request):
    my_dict = {'help_msg':"Help Page"}
    return render(request, 'Help/help.html', context=my_dict)