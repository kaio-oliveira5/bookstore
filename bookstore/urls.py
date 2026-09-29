
import debug_toolbar
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path, re_path
from rest_framework.authtoken.views import obtain_auth_token


def home(request):
    return render(request, "home.html")


urlpatterns = [
    path("", home, name="home"),
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    re_path(
        r"bookstore/(?P<version>(v1|v2))/",
        include("order.urls"),
    ),
    re_path(
        r"bookstore/(?P<version>(v1|v2))/",
        include("product.urls"),
    ),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]