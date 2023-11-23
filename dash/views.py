from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from dash.models import GenerationHistory


class GenerationHistoryListView(LoginRequiredMixin, ListView):
    model = GenerationHistory
    template_name = "dash/history/list.html"
    context_object_name = "history"

    def get_queryset(self):
        return super().get_queryset().filter(
            author=self.request.user
        )


class NewGenerationView(LoginRequiredMixin, CreateView):
    model = GenerationHistory
    fields = ['title', 'document', 'author_override']
    template_name = "dash/generation/new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
