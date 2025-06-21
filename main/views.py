from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import ContactForm,ReviewForm
from .models import Reservation,MenuItem, DailySpecial,Review


def home(request):
    specials = DailySpecial.objects.all()
    return render(request, 'main/home.html', {'specials': specials })

def menu(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    items = MenuItem.objects.all()

    if category:
        items = items.filter(category=category)

    if query:
        items = items.filter(name__icontains=query)

    return render(request, 'main/menu.html', {'items': items})




def reservation_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        
        Reservation.objects.create(name=name,phone=phone, date=date, time=time, guests=guests)
        return render(request, 'main/thank_you.html')
    return render(request, 'main/reservation.html')
def thank_you(request):
    return render(request, 'main/thank_you.html')



# views.py
def customer_reviews(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReviewForm()

    reviews = Review.objects.all()
    return render(request, 'main/reviews.html', {'form': form, 'reviews': reviews})

 

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def services(request):
    return render(request, 'main/services.html')



