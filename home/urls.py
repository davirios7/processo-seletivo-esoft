from django.urls import path

from . import views

urlpatterns = [
  # rotas do main
  path('cadastrar/', views.principal),
  path('', views.tabelaUsuarios, name='tabela'),
  path('editarUsuario/<int:pk>', views.editUsuario, name='editProd')
]

