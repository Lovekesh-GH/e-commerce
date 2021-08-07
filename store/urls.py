from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	#Leave as empty string for base url
    path('register/', views.registerpage, name="register"),
    path('login/', views.loginpage, name="login"), 

	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path(
        "manifest.json",
        TemplateView.as_view(
            template_name="pwa/manifest.json", content_type="text/plain"
        ),
        name='manifest',
    ),
    path(
        "serviceworker.js",
        TemplateView.as_view(
            template_name="pwa/serviceworker.js", content_type="text/javascript"
        ),
        name='serviceworker',
    ),
]