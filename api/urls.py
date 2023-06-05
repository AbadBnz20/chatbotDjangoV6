from django.urls import path, include
from rest_framework import routers
from api import views

# router = routers.DefaultRouter()
# router.register(r'programmers', views.ProgrammerViewSet)
# router.querysql(r'querysql',views.post_string_view)

urlpatterns = [
    # path('', include(router.urls)),
      path('createquery/', views.generarConsulta),
      path('validatecontact/',views.validarContacto),
      path('validatequery/',views.validarConsulta),

      #  path('api/v1/mi-endpoint/',  views.mi_vista, name='mi_vista'),
]