from rest_framework import serializers


def _time_check(qs, start_time, end_time):
    for schedule in qs:
        if schedule.start_time < end_time and schedule.end_time > start_time:
            raise serializers.ValidationError("User has conflicting schedules")


def schedule_check(gym, start_time, end_time, day, model, instance=None, trainer=None, member=None):
    target_member = trainer if trainer is not None else member
    if target_member not in gym.members.all():
        raise serializers.ValidationError("User is not a member of the gym")
    conflicting_schedules = model.objects.filter(
        day=day,
    ).exclude(pk=instance.pk if instance else None)
    if trainer:
        conflicting_schedules = conflicting_schedules.filter(trainer=trainer)
    if member:
        conflicting_schedules = conflicting_schedules.filter(members=member)
    _time_check(conflicting_schedules, start_time, end_time)
