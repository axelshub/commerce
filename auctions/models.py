from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    pass


class Listing(models.Model):
    category_type = models.TextChoices("category_type", "Fashion Electronics Decoration Other")
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.FloatField(default=0, max_length=10)
    category = models.CharField(blank=True, choices=category_type.choices, max_length=64)
    image = models.ImageField(default="default.png", blank=True)
    listed_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, blank=True, on_delete=models.CASCADE, related_name="listings")

    def __str__(self):
        return f"{self.id}: {self.title} in category {self.category} listed by {self.listed_by}"


class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    bid = models.FloatField(default=0, max_length=10)
    made_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, blank=True, on_delete=models.CASCADE, related_name="offers")


class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=128)
