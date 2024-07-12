from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
import uuid

# def pkgen(pk_length):
#     from base64 import b32encode
#     from hashlib import sha1
#     from random import random
#     rude = ('lol',)
#     bad_pk = True
#     while bad_pk:
#         pk = b32encode(sha1(str(random()).encode('utf-8')).digest()).lower()[:pk_length]
#         bad_pk = False
#         for rw in rude:
#             if pk.find(rw) >= 0: bad_pk = True
#     return pk


class Account(AbstractUser):
    class Meta:
        verbose_name = 'Account'
    class account_type_choices(models.TextChoices):
        attendant = 'at', 'attendant'
        support = 'sp', 'support'
        consumer = 'cn', 'consumer'
        manager = 'mn', 'manager'

    account_cpf = models.CharField(max_length=12, validators=[MinLengthValidator(12), MaxLengthValidator(12)])

    account_type = models.CharField(
        max_length=2,
        choices=account_type_choices.choices,
        default=account_type_choices.consumer
    )

    def save(self, *args, **kwargs):
        #if self.is_superuser and self.pk: # if updating existing on djangoadmin
        self.set_password(self.password)
        super(Account, self).save(*args, **kwargs)
        
class Luggage(models.Model):
    luggage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    luggage_consumer = models.ForeignKey(Account, null=False, on_delete=models.CASCADE)

class Luggage_Stage(models.Model):
    luggage_stage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class luggage_stage_choices(models.TextChoices):
        stage1 = 's1', 'stage1'
        stage2 = 's2', 'stage2'
        stage3 = 's3', 'stage3'
        stage4 = 's4', 'stage4'
    luggage_stage = models.CharField(
        max_length=2,
        choices=luggage_stage_choices.choices
    )

    luggage_stage_luggage = models.ForeignKey(Luggage, null=False, on_delete=models.CASCADE)
