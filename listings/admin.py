from django.contrib import admin

from .models import Listing, Floor_Plan

class ListingAdmin(admin.ModelAdmin):
    # fields =["realtor","title","developer","area","description", "price","photo_main",("photo_1", "photo_2", "photo_3","photo_4","photo_5", "photo_6", "photo_7","photo_8","photo_9","photo_10","photo_11","photo_12"), "is_published","property_status", "is_handOver_in_12_months", "is_hot","is_villas_and_mansionettes","list_date" ]
    fieldsets = (
        ('Listing Details', {'fields':("realtor","title","developer","area","description", "price","is_published","property_status", "is_handOver_in_12_months", "is_hot","is_villas_and_mansionettes",)}),
        
        ('Listing Main Photo', {'fields':('photo_main',)}),
        ('Listing Other Photos',{'fields':("photo_1", "photo_2", "photo_3","photo_4","photo_5", "photo_6", "photo_7","photo_8","photo_9","photo_10","photo_11","photo_12",)}),
                
        ('Listing Date',{"fields": ('list_date',)})
        
    )
    list_display = ('id', 'title', 'is_published', 'property_status','price', 'is_hot','list_date','is_handOver_in_12_months', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published','property_status','is_handOver_in_12_months','is_hot')
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25
    
class Floor_PlanAdmin(admin.ModelAdmin):
    list_display=('listing',)
    list_display_links = ('listing',)

admin.site.register(Listing, ListingAdmin)
admin.site.register(Floor_Plan, Floor_PlanAdmin)
