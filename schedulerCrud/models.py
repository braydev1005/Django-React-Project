# Create your models here.
from django.db import models

class ScheduleEvents(models.Model):
    Id = models.IntegerField(primary_key=True)
    Subject = models.CharField(max_length=200, null=True, blank=True)
    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()
    StartTimezone = models.CharField(max_length=200, null=True, blank=True)
    EndTimezone = models.CharField(max_length=200, null=True, blank=True)
    Location = models.CharField(max_length=200, null=True, blank=True)
    Description = models.CharField(max_length=200, null=True, blank=True)
    IsAllDay = models.BooleanField()
    RecurrenceID = models.IntegerField(null=True, blank=True)
    FollowingID = models.IntegerField(null=True, blank=True)
    RecurrenceRule = models.CharField(max_length=200, null=True, blank=True)
    RecurrenceException = models.CharField(max_length=200, null=True, blank=True)
    IsReadonly = models.BooleanField(null=True, blank=True)
    IsBlock = models.BooleanField(null=True, blank=True)
    RoomID = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'schedule_events'

class AuthUser(models.Model):
    Id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    username = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    date_joined = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'auth_user'