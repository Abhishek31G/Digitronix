from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="Index"),
    path('basic/', views.basic, name="Basic"),
    path('products/', views.product, name="Product"),
    path('toggle-wishlist/<int:product_id>/', views.toggle_wishlist, name='ToggleWishlist'),
    path('wishlist/', views.wishlist, name="Wishlist"),

    path('search/', views.search, name="Search"),
    path('products/<str:id>', views.product_details, name="ProductDetails"),
    path('contactus/', views.contactUs, name="ContactUs"),
    path('aboutus/', views.aboutUs, name="AboutUs"),
    path('account/', views.account, name="Account"),
    path('blog/', include('blog.urls')),

    path('register/', views.handleRegister, name="HandleRegister"),
    path('login/', views.handleLogin, name="HandleLogin"),
    path('logout/', views.handleLogout, name="HandleLogout"),


    # Cart Url's
    path('cart/add/<int:id>/', views.cart_add, name='CartAdd'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='ItemClear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='ItemIncrement'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='ItemDecrement'),
    path('cart/cart_clear/', views.cart_clear, name='CartClear'),
    path('cart/cart_detail/', views.cart_detail, name='CartDetail'),
    path('cart/checkout/', views.checkout, name='CheckOut'),
    path('cart/checkout/placeorder/', views.placeorder, name='PlaceOrder'),
    path('success/', views.success, name="Success"),
    path('yourorder/', views.yourorder, name="YourOrder"),
    path('user-order-track/<int:pid>/', views.user_order_track, name="UserOrderTrack"),

    # Forgot Password Url's
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='forgotpassword/reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='forgotpassword/reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='forgotpassword/reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='forgotpassword/reset_complete.html'), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
