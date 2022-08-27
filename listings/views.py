from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import area_choices, developer_choices

from .models import Listing, Floor_Plan


def index(request):
   
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    floor_plan =Floor_Plan.objects.filter(listing=listing_id)
    # for b in floor_plan:
    #     print(b.listing)
   
    context = {
        'listing': listing,
        'floor_plan': floor_plan
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
   

    # KEYWORDS
    # if 'keywords' in request.GET:
    #     keywords = request.GET['keywords']
    #     if keywords:
    #         queryset_list = queryset_list.filter(description__icontains=keywords)

    # CITY
    # if 'city' in request.GET:
    #     city = request.GET['city']
    #     if city:
    #         queryset_list = queryset_list.filter(city__iexact=city)

    # STATE
    if 'area' in request.GET:
        area = request.GET['area']
        print(area)
        if area:
            queryset_list = queryset_list.filter(area__iexact=area)

    # BEDROOMS
    # if 'bedrooms' in request.GET:
    #     bedrooms = request.GET['bedrooms']
    #     if bedrooms:
    #         queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # PRICE
    if 'developer' in request.GET:
        developer = request.GET['developer']
        if developer:
            queryset_list = queryset_list.filter(developer__iexact=developer)

    context = {
        # 'state_choices': state_choices,
        'developer_choices': developer_choices,
        'area_choices': area_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)

def dropdown_menu_form(request):
    if request.method == "POST":
        selected_value = request.POST.get('dropdown_menu_option')
        # print(selected_value[])
  #do something
    else :
        template = 'app_name/dropdown_menu_form.html'
    return render(request, template)

def readyToMoveIn(request):
       
    listings = Listing.objects.order_by('-list_date').filter(property_status="READY")
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def mortgage(request):
       
    listings = Listing.objects.order_by('-list_date').filter(property_status="MORTGAGE")

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def handOver(request):
       
    listings = Listing.objects.order_by('-list_date').filter(is_handOver_in_12_months=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def villasMansions(request):
       
    listings = Listing.objects.order_by('-list_date').filter(is_villas_and_mansionettes=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
   

    context = {
        'listings': paged_listings,
       
    }

    return render(request, 'listings/listings.html', context)

def hottestInTown(request):
       
    listings = Listing.objects.order_by('-list_date').filter(is_hot=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    

    context = {
        'listings': paged_listings,
         "has_drop_down": True,
         "developer_choices": developer_choices,
         "area_choices": area_choices,
        
        
    }

    return render(request, 'listings/listings.html', context)
