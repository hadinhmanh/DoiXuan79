from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path

app_name = "doixuan79"

urlpatterns = [
    

    path("", views.index, name="index"),
    path("gioithieu/",views.gioithieu, name="about"),
    path("sukien/",views.sukien, name="sukien"),
    path("booking/",views.booking, name="booking"),
    path("blog/",views.blog, name="blog"),
    path("lienhe/",views.lienhe, name="lienhe"),
    
    # load các trang dịch vụ
    path("buffet-lau-nuong/",views.lauNuong, name="launuong"),
    path("cafe/",views.cafe, name="cafe"),
    path("cheo-thuyen-Kayak/",views.cheothuyen, name="cheothuyen"),
    path("camping/",views.camping, name="camping"),
    path("khu-vui-choi-tre-em/",views.vuichoi, name="vuichoi"),
] 