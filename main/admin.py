from django.contrib import admin
from .models import Reservation, Contact,MenuItem, DailySpecial

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name',  'phone', 'date', 'time', 'guests')
    search_fields = ('name', 'email')
    list_filter = ('date', 'time')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name',)
    list_filter = ('category',)


@admin.register(DailySpecial)
class DailySpecialAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
