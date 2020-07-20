from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *

from .models import User, Listing, Bid, Comment


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all(),
    })

def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    bid_form = new_bid()
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "bid_form": bid_form

    })

def create(request):
    listing_form = new_listing()
    if request.method == "POST" and request.POST.get("id") == "listing_form":
        listing_form = new_listing(request.POST, request.FILES)
        bid_form = new_bid(request.POST, request.FILES)
        if listing_form.is_valid:
            listing = listing_form.save(commit=False)
            listing.listed_by = request.user
            listing.save()
            return HttpResponseRedirect(reverse("index"))

    if request.method == "POST" and request.POST.get("id") == "bid_form":
        if bid_form.is_valid:
            bid = bid_form.save(commit=False)
            bid.made_by = request.user
            bid.listing = request.listing
            return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/create.html", {
        "listing_form": listing_form,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
