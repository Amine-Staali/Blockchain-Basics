from django.urls import path
from . import views

urlpatterns = [
    path('get_chain/', views.get_chain, name = 'get_chain'),
    path('mine_block/',views.mine_block, name = 'mine_block'),
    path('is_chain_valid/',views.is_chain_valid, name = 'is_chain_valid'),
]
