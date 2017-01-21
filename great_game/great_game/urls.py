from django.conf.urls import include, url
from django.contrib import admin
from hunt_app import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'great_game.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index),
    url(r'^panel/', views.panel),

]