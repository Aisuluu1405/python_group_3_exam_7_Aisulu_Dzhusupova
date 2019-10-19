# Generated by Django 2.2 on 2019-10-19 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=3000, verbose_name='Question')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000, verbose_name='Choice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='webapp.Poll', verbose_name='Poll')),
            ],
        ),
    ]
