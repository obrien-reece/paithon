from django.db import models


class Day(models.Model):
    DAYS_OF_WEEK = (
        ("monday", "Monday"),
        ("tuesday", "Tuesday"),
        ("wednesday", "Wednesday"),
        ("thursday", "Thursday"),
        ("friday", "Friday"),
        ("sartuday", "Sartuday"),
        ("sunday", "Sunday"),
    )
    day = models.CharField(max_length=200, choices=DAYS_OF_WEEK, unique=True)

    def __str__(self):
        return self.day


class Todo(models.Model):
    # a note belongs to a day. A day has many notes
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name="todo")
    todo = models.CharField(max_length=200, blank=False)
    created = models.TimeField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return self.todo
