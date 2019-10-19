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
