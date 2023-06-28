from django.shortcuts import render
from .models import DishCategory, Dish, Event, Gallery, Contact, Chef


def main_page(request):
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_special=True)
    events = Event.objects.all
    gallery = Gallery.objects.all
    contacts = Contact.objects.all
    chefs = Chef.objects.all



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
                        })
