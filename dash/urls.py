from django.urls import path

from dash.views import GenerationHistoryListView, NewGenerationView

app_name = 'dash'

urlpatterns = [
    path('history/', GenerationHistoryListView.as_view(), name='history-list'),
    path('new/', NewGenerationView.as_view(), name='generation-add'),
]
