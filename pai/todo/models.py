from django.db import models


class Day(models.Model):
    day_of_week = models.CharField(max_length=200)

    def __str__(self):
        return self.day_of_week


class Reminder(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    reminder_txt = models.CharField(max_length=200)
    reminder_date = models.DateTimeField('reminder_date')

    def __str__(self):
        return self.reminder_txt
