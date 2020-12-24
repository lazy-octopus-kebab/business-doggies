from django.urls import path
from django.views.generic import TemplateView

from accounts.views import SitterListView

app_name = 'core'
urlpatterns = [
    # ex: /
    path('', TemplateView.as_view(template_name='core/index.html'), name='index'),
    path('test_btstrp', TemplateView.as_view(template_name='test_bootstrap.html'), name='bootstrap'),
    # ex: /sitters/
    path('sitters/', SitterListView.as_view(template_name='core/sitters.html'), name='sitters'),
]
