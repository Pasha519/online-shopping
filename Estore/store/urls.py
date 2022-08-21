from django.urls import path
from store import views

urlpatterns = [
    path("store/",views.store_home,name="store"),
    path("<int:id>/details",views.store_product_details,name="product_details"),
    path("<int:id>/category",views.store_product_category_view,name="category"),
    path("cart_create/",views.store_cart_create_view,name="cart_create"),
    #cart/address
    path("cart/",views.store_cart_view,name="cart"),
    path("cart_checkout/", views.store_cart_checkout_view, name="cart_checkout"),
    path("cart_update/", views.store_cart_items_update, name="cart_update"),
    #item Order
    path("order_create/",views.store_order_create_view,name="order_create"),
    path("order_save/",views.store_order_save_view,name="order_save"),
    path("order_item/",views.store_order_item_view,name="order"),
    path("ordered_track/",views.store_ordered_items_track,name="ordered_track"),
    #profile registration
    path("profile/",views.store_user_profile,name="profile"),
    path("orders/",views.store_user_profile_orders,name="orders"),
    path("address/",views.store_user_profile_address,name='address'),
    path("address_update/",views.store_user_profile_update,name="address_update"),
    path("update_picture/",views.Order_user_profile_update,name="picture"),
    path("password_change/",views.customer_password_change,name="password_change"),
    #authenticate
    path("logout/",views.customer_logout_view,name="logout"),
    path("login/",views.customer_login_view,name="login"),
    path("register/",views.customer_register_view,name="register")
]
