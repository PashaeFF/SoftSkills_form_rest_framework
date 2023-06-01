# Generated by Django 4.2.1 on 2023-05-31 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilledForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_list_1', models.JSONField(default=dict)),
                ('question_list_2', models.JSONField(default=dict)),
                ('question_list_3', models.JSONField(default=dict)),
                ('question_list_4', models.JSONField(default=dict)),
                ('question_list_5', models.JSONField(default=dict)),
                ('question_list_6', models.JSONField(default=dict)),
                ('question_list_7', models.JSONField(default=dict)),
                ('question_list_8', models.JSONField(default=dict)),
                ('question_list_9', models.JSONField(default=dict)),
                ('question_list_10', models.JSONField(default=dict)),
                ('form_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='panel.form', verbose_name='own_forms')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner_id')),
            ],
            options={
                'db_table': 'filled_forms',
            },
        ),
    ]