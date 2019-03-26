from django.db import models
# from .types import State
from collections import Counter
# Create your models here.
class Constants:
    review_score_values = {'has_accessible_bathroom':3, 'has_parking':2, 'has_space':1, 'has_ramp':2, 'has_entrances':2}
    max_score = sum(review_score_values.values())
    review_boolean_fields = ['has_accessible_bathroom', 'has_parking', 'has_space', 'has_ramp', 'has_entrances']
    filter_fields = {'has_accessible_bathroom':'Accessible Bathrooms', 'has_parking':'Parking', 'has_ramp':'Ramps', 'has_entrances':'Wide Entrances', 'has_space':'Floor Space'}

class Category(models.Model):
    name = models.CharField(max_length=255, help_text="Name of Category")
    slug = models.CharField(max_length=255, help_text="Category slug")

class Restaurant(models.Model):
    yelp_id = models.CharField(max_length=255, help_text="Yelp ID")
    name = models.CharField(max_length=255, help_text="Name of Restaurant")
    is_closed = models.BooleanField(default=False, help_text="Whether business has been closed permanently.")
    

    image_url = models.URLField(help_text="Image URL from Yelp")
    phone = models.CharField(max_length=20, help_text="Formatted phone number for backend")
    display_phone = models.CharField(max_length = 30, help_text="Display phone number for HTML")
    url = models.URLField(help_text="Yelp URL for the page")

    review_count = models.IntegerField(help_text="Number of reviews.", null=True)
    categories = models.ManyToManyField(Category, help_text="Categories that the restaurant belongs to")
    rating = models.FloatField(help_text="Yelp Rating")
    

    display_address = models.TextField(help_text="Display Address for Restaurant")
    city = models.CharField(max_length=255, help_text="City")
   # state = models.CharField( max_length=2)
    zip_code = models.CharField(max_length=10, help_text="Zip code")

    latitude = models.FloatField(help_text="Latitude")
    longitude = models.FloatField(help_text="Longitude")

    def __unicode__(self):
        return self.name

