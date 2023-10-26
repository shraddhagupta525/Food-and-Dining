from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('',views.homePage, name= "home" ),
    path('track-order',views.trackOrder, name= "track_order" ),
    # temp
    path('review',views.review, name= "review" ),
    path('menu',views.menu, name= "menu" ),
    path('recipe-sharing',views.recipeSharing, name= "recipeSharing" ),
    path('about',views.about, name= "about" ),
    # path('home',views.homePage, name= "home" ),
    
]