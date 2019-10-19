from django.core.paginator import Paginator

# from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm, PollChoiceForm
from webapp.models import Poll


class PollIndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = ['-created']
    paginate_by = 5
    paginate_orphans = 1


class PollView(DetailView):
    template_name = 'poll/poll.html'
    model = Poll
    context_object_name = 'poll'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PollChoiceForm()
        choices = context['poll'].choices.all()
        self.paginate_choices_to_context(choices, context)
        return context

    def paginate_choices_to_context(self, choices, context):
        paginator = Paginator(choices, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['choices'] = page.object_list
        context['is_paginated'] = page.has_other_pages()


class PollCreateView(CreateView):
    model = Poll
    template_name = 'poll/create.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollEditView(UpdateView):
    model = Poll
    template_name = 'poll/edit.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'poll/delete.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('index')
