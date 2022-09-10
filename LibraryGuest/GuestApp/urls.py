from django.contrib import admin
from django.urls import path
from GuestApp.views import *

urlpatterns = [
    path("",home_page,name="home"),
    path('booksapi/', BookView.as_view(),name="view_books"),
    path('success/',success_res,name="reservation_success"),
    path('reserfail/',reservation_failure,name="reservation_fail"),
    path('cancellation/',cancelled_reservation,name="reservation_cancelled"),
    path('cancelfailed/',cancellation_failed,name="cancellation_failed"),
    # path('book/<int:pk>/',GetBookData.as_view(),name="view_book_by_id"),
    path("reserve/",ReservationView.as_view(),name="reserve_book"),
    path("viewreservations/",view_reservation,name="view_reservation"),
    path("cancelreservation/",cancellation_view,name="cancel_reservation"),
    path('viewbooks/',viewbooks_site,name="front_view"),
]
