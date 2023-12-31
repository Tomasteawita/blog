from django.conf import settings
from django.urls import path
from .views import *
from django.conf.urls.static import static


url_crud_post = [
    path('delete/<pk>', DeletePostView.as_view(), name = "DeletePost"),
    path('detail/<pk>', DetailPostView.as_view(), name = "DetailPost"),
    path('edit/<pk>', EditPostView.as_view(), name = "EditPost"),
    path('transaction_completed/', transaction_completed_view, name = "TransactionCompleted"),
]

urlpatterns = [
    path('blog/', IndexView.as_view(), name = "BlogWeb"),
    path('', HomeView.as_view(), name = "Home"),
] + url_crud_post + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)