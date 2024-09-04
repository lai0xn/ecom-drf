from django.urls import path

from products.views import get_emails

from . import views


urlpatterns = [
    path("users",views.all_users),
    path("customers",views.get_customers),
    path("stats",views.admin_stats),
    path("emails",get_emails),
]
