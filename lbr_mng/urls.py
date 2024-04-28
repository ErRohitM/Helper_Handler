from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from labour.views import index,add_helper,assign_helpers,save_selected_value,list_helpers,helper_assigned
from customer.views import list_customers,create_customer

urlpatterns = [
    path('', index, name='index'),
    path('add_helper/', add_helper, name='add_helper'),
    path('helper_assigned/', helper_assigned, name='helper_assigned'),
    path('create_customer/', create_customer, name='create_customer'),
    path('list_customers/', list_customers, name='list_customers'),
    path('list_helpers/', list_helpers, name='list_helpers'),
    path('assign_helpers/', assign_helpers, name='assign_helpers'),
    path('save_selected_value/', save_selected_value, name='save_selected_value'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
