from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ShopRegistration
from math import radians, cos, sin, sqrt, atan2
from .models import Shop

def register_shop(request):
    if request.method == 'POST':
        form = ShopRegistration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Shop Registered Sucessfully')
    else:
        form = ShopRegistration()
    return render(request, 'shops/register.html', {'form': form})

def haversine(lat1, lon1, lat2, lon2):
    # Haversine formula to calculate the distance
    R = 6371.0  # Radius of the Earth in km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def search_shops(request):
    if request.method == 'POST':
        user_lat = float(request.POST.get('latitude'))
        user_lon = float(request.POST.get('longitude'))
        shops = Shop.objects.all()

        shop_distances = []
        for shop in shops:
            distance = haversine(user_lat, user_lon, shop.latitude, shop.longitude)
            shop_distances.append((shop, distance))

        # Sort shops based on distance
        sorted_shops = sorted(shop_distances, key=lambda x: x[1])

        return render(request, 'shops/search_results.html', {'shops': sorted_shops})

    return render(request, 'shops/search.html')
