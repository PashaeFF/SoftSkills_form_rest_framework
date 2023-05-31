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
        return f'URL: {self.url} \nForm name: {self.form_name} \n'
