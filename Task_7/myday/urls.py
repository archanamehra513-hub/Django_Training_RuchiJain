from django.urls import path

from . import views


app_name = 'myday'


urlpatterns = [

    path('',views.home,name='home'),

    path('signup/',views.signup,name='signup'),

    path('login/',views.login_view,name='login'),

    path('logout/', views.logout_view,name='logout'),

    path('test1/',views.test_page,{'test_number': 1},name='test1'),

    path('test2/',views.test_page,{'test_number': 2},name='test2'),

    path('test3/',views.test_page,{'test_number': 3},name='test3'),

    path('test-history/',views.test_history,name='test_history'),

]