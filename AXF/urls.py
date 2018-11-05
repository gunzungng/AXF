from django.conf.urls import url

from AXF import views

urlpatterns =[
    url(r'^$',views.home,name='index'),
    url(r'^home/$',views.home,name='home'),
    url(r'^market/(\d+)/$',views.market,name='market'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^mine/$',views.mine,name='mine')

]