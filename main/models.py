from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
import uuid

class Account(AbstractUser):
    class Meta:
        verbose_name = 'Account'
    class account_type_choices(models.TextChoices):
        attendant = 'at', 'attendant'
        support = 'sp', 'support'
        consumer = 'cn', 'consumer'
        manager = 'mn', 'manager'

    account_cpf = models.CharField(max_length=12, validators=[MinLengthValidator(12), MaxLengthValidator(12)], unique=True)

    account_type = models.CharField(
        max_length=2,
        choices=account_type_choices.choices,
        default=account_type_choices.consumer
    )

    def save(self, *args, **kwargs):
        print(not self.is_superuser)
        if not self.is_superuser: # if not superuser
            self.set_password(self.password)
        super(Account, self).save(*args, **kwargs)

    def create_superuser(self, *args, **kwargs):
        super(Account, self).save(*args, **kwargs)
        
class Luggage(models.Model):
    luggage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    luggage_consumer = models.ForeignKey(Account, null=False, on_delete=models.CASCADE)

class Luggage_Stage(models.Model):
    luggage_stage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class luggage_stage_choices(models.TextChoices):
        stage1 = 's1', 'Check In'
        stage2 = 's2', 'Bag Room'
        stage3 = 's3', 'Aeronave'
        stage4 = 's4', 'Esteira de Desembarque'
        stage5 = 's5', 'Chegou ao Destino'
    luggage_stage = models.CharField(
        max_length=2,
        choices=luggage_stage_choices.choices,
        default=luggage_stage_choices.stage1
    )

    luggage_stage_luggage = models.OneToOneField(Luggage, null=False, on_delete=models.CASCADE, editable=False)