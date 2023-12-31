from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('',views.homePage, name= "home" ),
    path('track_order',views.trackOrder, name= "track_order" ),
    # temp
    path('review',views.review, name= "review" ),
    path('menu',views.menuPage, name= "menu" ),
    # path('additem',views.additem, name= "additem" ),
    path('recipe-sharing',views.recipeSharing, name= "recipeSharing" ),
    path('about',views.about, name= "about" ),
    path('cart',views.cart, name= "cart" ),
    path('login',views.loginPage, name= "login" ),
    path('logout/',views.logoutPage, name= "logout" ),
    path('register/',views.register, name= "register" ),
    # path('home',views.homePage, name= "home" ),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)