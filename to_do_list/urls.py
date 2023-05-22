"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# import sys
# sys.path.append("..")
from django.contrib import admin
from django.urls import path
from display import views as display_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', display_views.index_view, name='main'),
    path('new_task/', display_views.new_task, name='new_task'),
    path('detail_task/<int:pk>', display_views.detail_task, name='detail_task'),
    path('update_task/<int:pk>', display_views.update_task, name='update_task'),
    path('delete_task/<int:pk>', display_views.delete_task, name='delete_task'),
    # path('delete_task/<int:pk>/confirm_delete/', display_views.confirm_delete, name='confirm_delete'),
]