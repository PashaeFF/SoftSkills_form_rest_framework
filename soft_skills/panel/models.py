from django.db import models
from django.utils.timezone import now
from auth2.models import User


class Form(models.Model):
    owner_id = models.ForeignKey(User, verbose_name="owner_id", on_delete=models.CASCADE)
    form_name = models.CharField(max_length=250, unique=True)
    values = models.JSONField(default=dict)
    created_at = models.DateTimeField(default=now)

    class Meta:
        db_table = "skill_forms"

    def __str__(self):
        return f'Form name: {self.form_name} \n'


class FilledForm(models.Model):
    owner_id = models.ForeignKey(User, verbose_name="owner_id", on_delete=models.CASCADE)
    form_id = models.ForeignKey(Form, default=1, verbose_name="own_forms", on_delete=models.CASCADE)
    question_list_1 = models.JSONField(default=dict)
    question_list_2 = models.JSONField(default=dict)
    question_list_3 = models.JSONField(default=dict)
    question_list_4 = models.JSONField(default=dict)
    question_list_5 = models.JSONField(default=dict)
    question_list_6 = models.JSONField(default=dict)
    question_list_7 = models.JSONField(default=dict)
    question_list_8 = models.JSONField(default=dict)
    question_list_9 = models.JSONField(default=dict)
    question_list_10 = models.JSONField(default=dict)

    class Meta:
        db_table = "filled_forms"

    def __str__(self):
        return f'Owner: {self.owner_id} \n'

