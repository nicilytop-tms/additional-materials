from django.urls import path

from carsharing.views import get_main_page, create_user, create_car, book_or_take

urlpatterns = [
    path('', get_main_page),
    path('user/', create_user),
    path('car/', create_car),
    path('book-or-take/', book_or_take),
]
