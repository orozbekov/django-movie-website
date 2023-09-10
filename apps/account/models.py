from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from apps.account.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    username = None
    first_name = models.CharField(_('first name'), max_length=100, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    user_role = models.CharField('Тип пользователя', max_length=20)

    is_superuser = models.BooleanField(_('superuser status'), default=False,
        help_text='Указывает, следует ли рассматривать этого пользователя как Admin.')
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))

    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновлении', auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Возвращает first_name плюс last_name с пробелом между ними.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()