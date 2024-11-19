from django.urls import path

from .views import category_list, ticket_request

urlpatterns = [
    path('', category_list, name='category_list'),
    path('ticket/<int:pk>/', ticket_request, name='ticket'),
    # path('ticket_form/<int:category_id>/<int:pk>/', ticket_show, name='ticket_form'),
    # path('ticket_answer/<int:pk>/<int:chosen_num>/', ticket_answer, name='ticket_answer'),
]