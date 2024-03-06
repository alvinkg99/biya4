"""
URL configuration for woods project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('furnitures.html',views.furni,name='furniture'),
    path('company.html',views.company,name='company'),
    path('contact.html',views.contact,name='contact'),
    path('about.html',views.about,name='about'),
    path('search',views.search,name='search'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('userr',views.userr,name='userr'),
    path('logout',views.logout,name='logout'),
    path('cart',views.cartt,name='cart'),
    path('product_list/addcart/<wal>',views.addtocart,name='addcart'),
    path('seemore',views.seemore,name='seemore'),
    path('product_list/<wal>',views.product_list,name='product_list'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('product_list/addwish/<wal>',views.addwish,name='addwish'),
    path('delwish/<de>',views.delwish,name='delwish'),
    # path('userprofile',views.userprofile,name='userprofile'),
    path('uedit',views.uedit,name='uedit'),
    path('uedit1',views.uedit1,name='uedit1'),
    path('ureset',views.ureset,name='ureset'),
    path('ureset1',views.ureset1,name='ureset1'),


    path('pluscart/<de>',views.pluscart,name='pluscart'),
    path('minuscart/<de>',views.minuscart,name='minuscart'),
    path('deletecart/<de>',views.deletecart,name='deletecart'),
    path('checkout',views.checkout,name='checkout'),
    

    path('place-order', views.placeorder, name='placeorder'),
    path('proceed-to-pay', views.razorpaycheck, name='proceed-to-pay'),
    path('myorder', views.orderss, name='myorder'),



    # forget password
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html'),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),


    # admin pages urls

    path('adminindex',views.adminindex,name='adminindex'),
    path('userdetails',views.userdetails,name='userdetails'),
    path('products',views.products,name='products'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('edit/<wal>',views.edit,name='edit'),
    path('edit/edit1/<wal1>',views.edit1,name='edit1'),
    path('admindelete/<int:id>',views.admindelete,name='admindelete'),
    path('complaint',views.comp,name='complaint'),
    path('reply/<em>',views.reply,name='reply'),
    path('reply/replymail/<em>',views.replymail,name='replymail'),
    path('delete/<wal>',views.comdelete,name='delete'),
    path('userbooking',views.userbooking,name='userbooking'),
    path('statusup/<wal>',views.statusup,name="statusup"),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
