from django.urls import path
from . import views

urlpatterns = [
   path('template/<str:template>/', views.template_view),
]
