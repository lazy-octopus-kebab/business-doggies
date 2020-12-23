from django.urls import path
from django.views.generic import TemplateView


app_name = 'core'
urlpatterns = [
    # ex: /
    path('', TemplateView.as_view(template_name='core/index.html'), name='index'),
    path('test_404', TemplateView.as_view(template_name='404.html'), name='404'),
]
