"""my_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from my_app.views import contacts_list
from my_app.views import show_contact
from my_app.views import add_new_person
from my_app.views import delete_contact
from my_app.views import modify_contact
from my_app.views import groups_list
from my_app.views import group_users
from my_app.views import group_add_person
from my_app.views import add_group
from my_app.views import group_search


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', contacts_list),
    url(r'^show/(?P<my_id>(\d)+)$', show_contact),
    url(r'^new', add_new_person),
    url(r'^delete/(?P<my_id>(\d)+)$', delete_contact),
    url(r'^modify/(?P<my_id>(\d)+)$', modify_contact),
    url(r'^group-list/', groups_list),
    url(r'^group/(?P<group_id>(\d)+)$', group_users),
    url(r'^group/(?P<group_id>(\d)+)/add-person$', group_add_person),
    url(r'^group-add/', add_group),
    url(r'^group-search/', group_search),
]

