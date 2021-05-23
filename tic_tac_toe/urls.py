
from django.contrib import admin
from django.urls import path
# from game.views import index
from game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="home"),
    path('play/<room_code>', views.game),
]
