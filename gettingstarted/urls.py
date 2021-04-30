from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("base/", hello.views.base, name="base"),
    path("bulb/", hello.views.bulb, name="bulb"),
    path("google_map_location/", hello.views.google_map_location, name="google_map_location"),
    path("osm_leaf_map/", hello.views.osm_leaf_map, name="osm_leaf_map"),
    path("simple_todo/", hello.views.simple_todo, name="simple_todo"),
]
