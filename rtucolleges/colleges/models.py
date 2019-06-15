from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class College(models.Model):
    title = models.CharField(
        _('College Title'), max_length=150)
    rank = models.PositiveIntegerField(
        _('College Rank'), default='')
    staff = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='college_staff')
    verified = models.BooleanField(
        _('College Verified'), default=False)
    verified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='verified_by',
        on_delete=models.SET_NULL, blank=True, null=True)
    location = models.CharField(
        _('Location'), max_length=50, null=True, blank=True)
    address = models.CharField(
        _('Address'), max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to='colleges_pics/')
    establishment_date = models.DateTimeField(
        _('Establishment Date'), blank=True, null=True)
