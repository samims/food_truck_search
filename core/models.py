from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# Base model will help to implement common fields
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ('-id',)


# CustomUser is implemented to use email based auth
# as it need to implemented before doing any migration 
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True, blank=False, null=True)
    objects = CustomUserManager
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self) -> str:
        return super().__str__()


# Profile model for user
class Profile(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.email