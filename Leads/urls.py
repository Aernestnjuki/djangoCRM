from django.urls import path
from Leads import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('<pk>', views.lead_detail, name='lead-detail')
]
