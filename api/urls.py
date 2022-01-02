from django.urls import path
from .views import CreateCardInfoView, ListCardInfoView, ListAllCardInfoView

urlpatterns = [
    path("verify/", CreateCardInfoView.as_view(), name="stored_card_number"),
    path("stats/", ListCardInfoView.as_view(), name="list_cart_number_unique"),
    path("all_stats/", ListAllCardInfoView.as_view(), name="list_cart_number_unique"),
]