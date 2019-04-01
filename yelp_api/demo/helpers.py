from yelpapi import YelpAPI
import json
from django.conf import settings
from demo.models import *

yelp_api = YelpAPI(settings.YELP_API_KEY)


def parse_yelp_obj(yelp_obj, db_obj):
    for k in yelp_obj:
        attr_list = [['yelp_id', 'id'], ['name', 'name'], ['is_closed', 'is_closed'], ['image_url', 'image_url'], ['phone', 'phone'], ['display_phone', 'display_phone'], ['url', 'url'], ['review_count', 'review_count'], ['rating', 'rating']]
        for attr in attr_list:
            setattr(db_obj, attr[0], k[attr[1]])
        db_obj.display_address = k['location']['display_address'][0]
        db_obj.city = k['location']['city']
  #     db_obj.state = k['location']['state_code']
        db_obj.zip_code = k['location']['zip_code']
        db_obj.latitude = float(k['coordinates']['latitude'])
        db_obj.longitude = float(k['coordinates']['longitude'])
    return db_obj

def yelp_to_db(search_name,location):
    name = search_name
    location = location
    if name == None:
        return None
    search_results = yelp_api.search_query(term = name, location = location, sort=0)
    yelp_restaurant_object = search_results['businesses']

    for fields in yelp_restaurant_object:
        yelp_id = fields['id']
        if Restaurant.objects.filter(yelp_id=yelp_id).exists():
            restaurant_object = Restaurant.objects.get(yelp_id=yelp_id)
        else:
            restaurant_object = Restaurant()
            restaurant_object = parse_yelp_obj(yelp_restaurant_object, restaurant_object)
            restaurant_object.save()
            for category in fields['categories']:
                category_obj, created = Category.objects.get_or_create(slug=category['alias'], name=category['title'])
                if created:
                     category_obj.save()
                restaurant_object.categories.add(category_obj)
    
    return restaurant_object