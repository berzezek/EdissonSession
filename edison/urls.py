from django.urls import path
from .views import home, app, start, user_stat, psychic_stat

urlpatterns = [
    path('', home, name='home'),
    path('start/', start, name='start'),
    path('app/', app, name='app'),
    path('userstat/', user_stat, name='user_stat'),
    path('psystat/', psychic_stat, name='psychic_stat'),
]
