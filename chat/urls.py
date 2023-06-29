from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_proposal_view, name='service_proposal'),
    path('product_ideas/',views.product_ideas_view, name='product_ideas'),
    path('business_composition/',views.business_composition_view, name='business_composition'),
    path('initial_hypothesis/',views.initial_hypothesis_view, name='initial_hypothesis'),
    path('market/',views.market_view,name='market')
]