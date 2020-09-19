from flask_login import current_user
from nuts_and_bolts import db
from collections import defaultdict
import datetime


def get_cities(posts):
    cities = []
    for post in posts.items:
        city = post.site.city
        cities.append(city.title)
    return cities

def get_sites(posts):
    sites = []
    for post in posts.items:
        site = post.site
        sites.append(site.title)
    return sites    
    

def get_js_date(posts):
    posted = []
    updated = []
    for post in posts.items:
        posted.append(post.date_posted.isoformat())
        updated.append(post.date_updated.isoformat())
    return posted, updated