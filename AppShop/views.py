from django.shortcuts import render
from django.views import View
from .models import Product
from django.http import JsonResponse


class Pagehome(View):
    def get(swlf, request):
        return render(request, 'home.html')


class SearchProduct(View):
    def get(self, request):
        query = request.GET.get('q', '')
        
        search_products = Product.objects.filter(
            title__iregex = query
        ).values('title','price')
        print(search_products)
        
        return JsonResponse({
            'success': True,
            'query': query,
            'result': list(search_products),
            'count': len(search_products)
        }, status=200)
