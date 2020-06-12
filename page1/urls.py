from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home page"),
    path('search',views.search,name="search"),
    path('addcart',views.addcart,name="addcart"),
    path('about',views.about,name="about us"),
    path('contact',views.contact1,name="contact us"),
    path('gotouserdash',views.gotouserdash,name="for go to userdash"),
    path('productview',views.productview,name="productview"),
    path('checkout',views.checkout,name="checkout"),
    path('emovequantity',views.emovequantity,name="emovequantity"),
    path('ddquantity',views.ddquantity,name="ddquantity"),
    # for customer
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('userdash',views.userdash,name="userdash"),
    path('find',views.find,name="find"),
    path('update',views.update,name="update"),
    path('delete',views.delete,name="delete"),
    path('logout',views.logout,name="logout"),
    # for client
    path('signupc',views.signupc,name="signupc"),
    path('loginc',views.loginc,name="loginc"),
    path('userdashc',views.userdashc,name="userdashc"),
    path('findc',views.findc,name="findc"),
    path('updatec',views.updatec,name="updatec"),
    path('deletec',views.deletec,name="deletec"),
    path('logoutc',views.logoutc,name="logoutc"),
    # for product
    path('add',views.add,name="add"),
    path('remove',views.remove,name="removw"),
    path('editproduct',views.editproduct,name="editpro"),
]