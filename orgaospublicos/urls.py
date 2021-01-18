"""orgaospublicos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from orgaopublicoapp.views import index, orgaospublicos, criar_orgaospublicos, editar_orgaospublicos, deletar_orgaospublicos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('orgaospublicos/', orgaospublicos, name='orgaospublicos'),
    path('criar_orgaospublicos/', criar_orgaospublicos),
    path('editar_orgaospublicos/<int:id>',editar_orgaospublicos, name='editar_orgaospublicos'),
    path('delatar_orgaospublicos/<int:id>',deletar_orgaospublicos, name='deletar_orgaospublicos'),
    url(r'^img/(?P<path>,*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
