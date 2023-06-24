from django.db import models


# Create your models here.
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


# class Event(models.Model):
#     name = models.CharField(max_length=50)
#     suname = models.CharField(max_length=50)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     date = models.DateField()
#     time = models.TimeField()
#     count = models.SmallIntegerField()  # number of people at the event
#     message = models.TextField(max_length=500, blank=True)
#     photo = models.ImageField(upload_to="event/", blank=True)

#     def __str__(self):
#         return f"{self.name} {self.suname} {self.date} {self.time}"


# class Gallery(models.Model):
#     name = models.CharField(max_length=50)
#     photo = models.ImageField(upload_to="gallery/% Y/% m/% d/", blank=True)

#     def __str__(self):
#         return f"{self.name}"
