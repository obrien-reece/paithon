from django.db import models
import uuid


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.png")
    demo_link = models.CharField(max_length=200, blank=True)
    source_link = models.CharField(max_length=200, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    # ManyToManyField
    tags = models.ManyToManyField(Tag, blank=True)

    # We put the Tag in speech marks when the class is after the parent class
    # tags = models.ManyToManyField("Tag", blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )

    # OneToMany
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.CharField(blank=True, null=True, max_length=200)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    def __str__(self):
        return self.value
