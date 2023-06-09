from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('backtests/', BacktestStrategyClassesView.as_view(), name='backtests'),
    path('backtests/<str:strategy_class>/', StrategyParametersView.as_view(), name='edit_backtest_strategy'),
    path('backtests/<str:strategy_class>/optimize/', StrategyOptimizationView.as_view(), name='optimize'),
    path('deploy/', DeployableStrategySelectView.as_view(), name='deploy'),
    path('deploy/<str:strategy_class>/', DeployableStrategyParametersView.as_view(), name='edit_deployable_strategy'),
]