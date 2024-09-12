# Create your models here.
from django.db import models
from django_tenants.models import DomainMixin, TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField(null=True, blank=True)
    on_trial = models.BooleanField(
        help_text="Make this false will create charge-over subscription."
    )
    trial_expiration_date = models.DateField(null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    owner_first_name = models.CharField(max_length=512, null=True, blank=True)
    owner_last_name = models.CharField(max_length=512, null=True, blank=True)
    owner_email = models.EmailField()
    owner_password = models.CharField(max_length=100)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    def __str__(self):
        return f"{self.schema_name} - {self.name}"


class Domain(DomainMixin):
    pass
