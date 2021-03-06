from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    # path('user/<usuario_latitud>/<usuario_longitud>/', views.encuentra_datos_usuario, name="info_usuario"),
    # si quieres revisar una info por coordenadas puedes pon la direccion asi:
    # 'user/latitud_longitud_son_coordenada'
    path("core/user/<direccion>/", views.encuentra_datos_usuario, name="info_usuario"),
]
