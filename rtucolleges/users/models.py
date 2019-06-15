from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class User(AbstractUser):
    pass
    name = models.CharField(_("User's name"), blank=True, max_length=255)
    picture = models.ImageField(
        _('Profile picture'), upload_to='profile_pics/', null=True, blank=True)
    location = models.CharField(
        _('Location'), max_length=50, null=True, blank=True)
    job_title = models.CharField(
        _('Job title'), max_length=50, null=True, blank=True)
    personal_url = models.URLField(
        _('Personal URL'), max_length=555, blank=True, null=True)
    facebook_account = models.URLField(
        _('Facebook profile'), max_length=255, blank=True, null=True)
    twitter_account = models.URLField(
        _('Twitter account'), max_length=255, blank=True, null=True)
    github_account = models.URLField(
        _('GitHub profile'), max_length=255, blank=True, null=True)
    stack_overflow = models.URLField(
        _('Stackoverflow profile'), max_length=255, blank=True, null=True)
    linkedin_account = models.URLField(
        _('LinkedIn profile'), max_length=255, blank=True, null=True)
    short_bio = models.CharField(
        _('Describe yourself'), max_length=60, blank=True, null=True)
    bio = models.CharField(
        _('Short bio'), max_length=280, blank=True, null=True)
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    email_public = models.BooleanField(default=True)
    reputation = models.IntegerField(default='1')

    # Is_student
    #     Student Rank
    #     Branch
    #     Experience
    # Is_teacher
    #     Techer Rank
    #     Job title
    #     Work Experience

    # College name
    # Badge(ex: Autobiographer - for completing profile details, First like, etc)
    # Skills
    # Accomplishments
