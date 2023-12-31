from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse



class DishCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Dish Categories"
        ordering = ("position",)


class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    ingredients = models.CharField(max_length=250)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.PositiveIntegerField(blank=True)
    photo = models.ImageField(upload_to="dishes/", blank=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)

    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Dishes"
        ordering = (
            "category",
            "position",
        )


class Event(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    count = models.SmallIntegerField()  # number of people at the event
    event_name = models.CharField(max_length=50)
    maneg = models.CharField(max_length=50)  # manager responsible for the event
    venue = models.CharField(max_length=100)  # venue of the event
    description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to="event/% Y/% m/% d/", blank=True)

    def __str__(self):
        return f"{self.full_name} {self.date} {self.event_name}"

    class Meta:
        verbose_name_plural = "Events"
        ordering = ("date",)


class Gallery(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="gallery/", blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Gallery"
        ordering = ("name",)
        
    
class Contact(models.Model):
    location = models.CharField(max_length=100)
    open_day = models.CharField(max_length=100, blank=True)
    open_hours = models.CharField(max_length=100)
    email1 = models.EmailField()
    email2 = models.EmailField()
    number_phone1 = models.CharField(max_length=20)
    number_phone2 = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Contacts"

class Chef(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=30, unique=True)
    twitter = models.CharField(max_length=30, blank=True)
    facebook = models.CharField(max_length=30, blank=True)
    instagram = models.CharField(max_length=30, blank=True)
    telegram = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(upload_to="chefs/", blank=True)

    def __str__(self):
        return f"{self.position}"
    
    class Meta:
        verbose_name_plural = "Chefs"

class Booking(models.Model):
    ful_name = models.CharField(max_length=60)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r"^(\+38)?0[0-9]{9}$",
        message="Phone number must be entered in the format: +380xxxxxxxxx or 0xxxxxxxxx",
    )
    phone = models.CharField(validators=[phone_regex], max_length=20)
    date = models.DateField()
    time = models.TimeField()
    of_people = models.PositiveSmallIntegerField(default=1)
    message = models.TextField(max_length=200, blank=True)

    is_processed = models.BooleanField(default=False)
    date_in = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ful_name}: {self.phone} {self.date} {self.time}"
    
    class Meta:
        ordering = ("-date_in",)
        

class Client(models.Model):
    full_name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=50, blank=True)
    message = models.TextField(max_length=200, blank=True)
    date_in = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.full_name} {self.message}"
    
    class Meta:
        ordering = ("-date_in",)
        

class MainMenuItem(models.Model):
    title = models.CharField(max_length=50, verbose_name='menu item')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='url')
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}/{self.slug}'
    
    def get_absolute_url(self):
        return reverse('home') + f'#{self.slug}'


    class Meta:
        ordering = ("position",)
