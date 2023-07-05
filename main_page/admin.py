from django.contrib import admin
from .models import DishCategory, Dish, Event, Gallery, Contact, Chef, Booking, Client
from .models import MainMenuItem

admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Chef)
admin.site.register(Booking)
admin.site.register(Client)

@admin.register(MainMenuItem)
class MainMenuItemsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}