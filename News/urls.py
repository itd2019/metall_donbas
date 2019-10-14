from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.News, name="News"),
    # url(r'send_sms', views.send_sms, name="send_sms"),
]