from django.conf.urls import url
from account import views

urlpatterns = [
    # url(r'test/.+/$',views.test,name="ssss")
    url(r'^test/$',views.test,name='test'),
]
