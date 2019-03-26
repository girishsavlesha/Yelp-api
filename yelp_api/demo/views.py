from django.shortcuts import render
from demo.models import *
from .helpers import *
from yelpapi import YelpAPI
from django.conf import settings
import requests
import json
yelp_api = YelpAPI(settings.YELP_API_KEY)
# Create your views here.


def search(request):

    template_name = 'demo.html'
    search_name = request.GET.get('search')
    location = "NEW YORK"
    template_name = 'details.html'
    search_name = request.GET.get('search')
    location = 'New York'
    query_set = yelp_to_db(search_name,location)
    context = {
         object_list : querys_set
     }

    return render(request,template_name,context)

# def search_result(request):
#     template_name = 'details.html'
#     search_name = request.GET.get('search')
#     location = 'New York'
#     query_set = yelp_to_db(search_name,location)
#     context = {
#          object_list : querys_set
#      }

    
#     return render(request,template_name, context)