from django.urls import path
from adminapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard_admin', views.dashboard_admin, name='dashboard_admin'),

    path('admin_users/', views.admin_users, name='admin_users'),
    path('block_user/<int:user_id>/', views.block_user, name='block_user'),
    path('unblock_user/<int:user_id>/', views.unblock_user, name='unblock_user'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_category/', views.admin_category, name='admin_category'),
    #path('sample/', views.sample, name='sample'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('soft_delete_category/<int:category_id>/', views.soft_delete_category, name='soft_delete_category'),
    path('undo_soft_delete_category/<int:category_id>/', views.undo_soft_delete_category, name='undo_soft_delete_category'),
    #Products
    path('admin_products/', views.admin_products, name='admin_products'),
    path('add_product/',views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('soft_delete_product/<int:product_id>/', views.soft_delete_product, name='soft_delete_product'),
    path('undo_soft_delete_product/<int:product_id>/', views.undo_soft_delete_product, name='undo_soft_delete_product'),
    #order
    path('admin_orders/', views.admin_orders, name='admin_orders'),
    path('update_order_status/<int:order_id>/<str:new_status>/', views.update_order_status, name='update_order_status'),
    path('admin_order_details/<int:order_id>/', views.admin_order_details, name='admin_order_details'),
    path('admin_coupons/', views.admin_coupons, name='admin_coupons'),
    path('add_coupons/',views.add_coupons, name='add_coupons'),
    path('edit_coupons/<int:coupon_id>/', views.edit_coupons, name='edit_coupons'),
    path('delete_coupons/<int:coupon_id>/', views.delete_coupons, name='delete_coupons'),

    path('sales_report/', views.sales_report, name='sales_report'),
    path('cancel_report/', views.cancel_report, name='cancel_report'),
    path('stock_report/', views.stock_report, name='stock_report'),
]