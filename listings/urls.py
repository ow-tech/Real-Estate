from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('ready-to-move-in', views.readyToMoveIn, name='readyToMoveIn'),
    path('mortgage', views.mortgage, name='mortgage'),
    path('hand-over-in-12-months', views.handOver, name='handOver'),
    path('hot-properties', views.hottestInTown, name='hottestInTown'),
    path('villas-and-mansionettes', views.villasMansions, name='villasMansions'),
]
