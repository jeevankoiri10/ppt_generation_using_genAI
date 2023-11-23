from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView

from dash.forms import GenerationForm
from dash.models import GenerationHistory


class GenerationHistoryListView(LoginRequiredMixin, ListView):
    model = GenerationHistory
    template_name = "dash/history/list.html"
    context_object_name = "history"
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(
            author=self.request.user
        )


def new_generation_view(request):
    if request.method == 'POST':
        form = GenerationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()

            # Run in BG the processing script
            return redirect('dash:history-list')
    else:
        form = GenerationForm()
    return render(request, 'dash/generation/new.html', {'form': form})