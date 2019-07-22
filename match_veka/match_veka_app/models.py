from django.db import models


class Event:
    name = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True)


class Photo:
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    content = models.ImageField(upload_to=f"/{event.name}/")
    is_visible = models.BooleanField(default=True)


class Album:
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    order_prior = models.IntegerField(default=0)  # чем меньше, тем раньше альбом в выдаче
    name = models.CharField(max_length=200)
    photos = models.ManyToManyField(Photo)
    is_visible = models.BooleanField(default=True)


class Player:
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    faculty = models.CharField(max_length=100)
    age = models.IntegerField()
    graduation_year = models.IntegerField()
    extra_info = models.CharField(max_length=1000)
