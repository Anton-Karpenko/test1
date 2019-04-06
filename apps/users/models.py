from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from apps.base.utils import custom_uuid
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    id = models.CharField(
        max_length=11,
        primary_key=True,
        default=custom_uuid,
        editable=False,
    )
    email = models.EmailField(
        unique=True,
    )
    username = models.CharField(
        max_length=24,
        unique=True,
        help_text=_('Max length is 24 symbols. '),
        validators=[
            validators.MinLengthValidator(1),
            validators.MaxLengthValidator(24),
        ],
        error_messages={'unique': _("A user with this nickname already exists.")},
        default=custom_uuid,
    )
    name = models.CharField(
        _("Full name of User"),
        max_length=60,
        validators=[validators.MaxLengthValidator(60),
                    validators.MinLengthValidator(1)],
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Designates whether this user should be treated as active. '
                    'Unselect this instead of deleting accounts.'),
    )
    date_joined = models.DateTimeField(
        _('date joined'),
        default=timezone.now,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email
