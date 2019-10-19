from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=3000, verbose_name='Question')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')

    def __str__(self):
        return self.question


class Choice(models.Model):
    text = models.TextField(max_length=2000, verbose_name='Choice')
    poll = models.ForeignKey('webapp.Poll', related_name='choices',
                             on_delete=models.CASCADE, verbose_name='Poll')

    def __str__(self):
        return self.text


class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='answer_poll', on_delete=models.CASCADE, verbose_name='Poll')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    choice = models.ForeignKey('webapp.Choice', related_name='answer_choice', on_delete=models.CASCADE, verbose_name='Choice')

    def __str__(self):
        return self.poll