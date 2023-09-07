from django.conf import settings
from django.urls import path
from .views import *
from django.conf.urls.static import static


url_crud_post = [
    path('create/', CreatePostView.as_view(), name = "CreatePost"),
    path('delete/<pk>', DeletePostView.as_view(), name = "DeletePost"),
    path('detail/<pk>', DetailPostView.as_view(), name = "DetailPost"),
    path('edit/<pk>', EditPostView.as_view(), name = "EditPost"),
    path('transaction_completed/', transaction_completed_view, name = "TransactionCompleted"),
]

urlpatterns = [
    path('', IndexView.as_view(), name = "Index"),
] + url_crud_post + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)