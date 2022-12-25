import debug_toolbar
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # inclue todos as rotas para uma rota principal exemplo "/principal"
    path('', include("home.urls")),
    path('__debug__/', include(debug_toolbar.urls))
]
