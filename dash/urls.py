from django.urls import path

from dash.views import GenerationHistoryListView, new_generation_view

app_name = 'dash'

urlpatterns = [
    path('history/', GenerationHistoryListView.as_view(), name='history-list'),
    path('new/', new_generation_view, name='generation-add'),
]
