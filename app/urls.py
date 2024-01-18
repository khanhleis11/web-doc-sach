
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('verify/', views.verify, name='verify'),
    path('login/', views.signIn, name='login'),
    path('logout/', views.signOut, name='logout'),
    path('account/', views.account, name='account'),
    path('cart/', views.cart, name='cart'),
    path('book/<str:slugName>/', views.book, name='book'),
    path('payment/', views.payment, name='payment'),
    path('update-item/', views.updateItem, name='update-item'),
    path('search/<str:query>/', views.search, name='search'),
    path('filter-category/', views.filter_category, name='filter-category'),
    path('api/products/', views.productsApi, name='products-api'),
    path('api/update-account/', views.updateAccount, name='update-account'),
    path('api/user-id/', views.getIdUser, name='user-id'),
    path('api/verify-change-email/', views.verifyChangeEmail, name='verify-change-email'),
    path('api/update-avatar/', views.updateAvatar, name='update-avatar'),
    path('api/change-password/', views.changePassword, name='change-password'),
    path('api/recover-password/', views.recoverPassword, name='recover-password'),
    path('api/verify-recover-password/', views.verifyRecoverPassword, name='verify-recover-password'),
    path('api/recover-success/', views.recoverSuccess, name='recover-success'),
    path('api/recover/', views.recover, name='recover'),
    path('api/recover-account/', views.recoverAccount, name='recover-account'),
    path('api/password/create/', views.createNewPassword, name='create-new-password'),
    path('notifications/', views.notifications, name='notifications'),
    path('order/', views.order, name='order'),
    path('create-order/', views.createOrder, name='create-order'),
    path('confirm-payment-order/', views.confirmPaymentOrder, name='confirm-payment-order'),
    path('update-cart-items/', views.updateCartItem, name='update-cart-items'),
    path('confirm-order-complete/', views.confirmOrderComplete, name='confirm-order-complete'),
    path('order/details/<int:order_id>', views.orderDetails, name='order-details'),
    path('order/payment-again/', views.paymentOrderAgain, name='payment-again'),
    path('feedback/', views.sendFeedback, name='feedback'),
]