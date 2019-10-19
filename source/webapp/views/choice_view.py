from django.shortcuts import  get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DeleteView, UpdateView, CreateView
from webapp.forms import ChoiceForm
from webapp.models import Choice, Poll


class ChoiceForPollCreateView(CreateView):
    template_name = 'choice/create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll_pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=poll_pk)
        poll.choices.create(**form.cleaned_data)
        return redirect('poll_view', pk=poll_pk)


class ChoiceEditView(UpdateView):
    model = Choice
    template_name = 'choice/edit.html'
    form_class = ChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice/delete.html'
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})
