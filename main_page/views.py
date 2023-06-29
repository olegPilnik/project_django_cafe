from django.shortcuts import render, redirect
from .models import DishCategory, Dish, Event, Gallery, Contact, Chef
from .forms import BookingForm, ClientForm

def main_page(request):
    if request.method == "POST":
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            return redirect('/')
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client_form.save()
            return redirect('/')

    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_special=True)
    events = Event.objects.all()
    gallery = Gallery.objects.all()
    contacts = Contact.objects.all()
    chefs = Chef.objects.all()
    booking_form = BookingForm()
    client_form =  ClientForm()
    return render(request,
                   "main.html",
                    context={
                        "categories": categories,
                        "dishes": dishes,
                        "special_dishes": special_dishes,
                        "contacts": contacts,
                        "chefs": chefs,
                        "events": events,
                        "galerry": gallery,
                        "booking_form": booking_form,
                        "client_form": client_form,
                        })
