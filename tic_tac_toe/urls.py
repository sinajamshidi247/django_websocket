
from django.contrib import admin
from django.urls import path
# from game.views import index
from django_websocket.game import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="home")
]
