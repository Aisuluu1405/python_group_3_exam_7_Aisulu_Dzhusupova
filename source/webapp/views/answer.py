from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from webapp.models import Poll, Answer, Choice


class AnswerView(View):

    def get(self, request, *args, **kwargs):
        poll = self.get_poll()
        return render(request, 'answer.html', {'poll': poll})

    def get_poll(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=poll_pk)

    def post(self, request, *args, **kwargs):
        poll_id = kwargs.get('pk')
        choice_id = int(request.POST.get('answer'))
        ans_pol = get_object_or_404(Poll, pk=poll_id)
        choice = get_object_or_404(Choice, pk=choice_id)
        answer = Answer()
        answer.poll = ans_pol
        answer.choice = choice
        answer.save()
        return redirect('index')



