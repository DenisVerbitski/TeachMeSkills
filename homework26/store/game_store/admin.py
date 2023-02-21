from django.contrib import admin
from django.http import HttpResponse
from django.db.models import Avg

from decimal import Decimal
import csv

from .models import Game, Category


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'price', 'category', 'image_tag')  
    date_hierarchy = 'release_date'                 
    prepopulated_fields = {"slug": ('name',)}        
    radio_fields = {"category":admin.HORIZONTAL}     
    actions = ['export_as_csv']                      

    @admin.action(description='Export to CSV')
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    def image_tag(self, obj):
        from django.utils.html import format_html
        return format_html('<img src="{}" width="150" height="150" />'.format(obj.game_image.url))

    image_tag.short_description = 'Image'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'games_amount', 'average_price_of_a_game_in_this_category')


    @admin.display(description='Средняя цена игр в категории')
    def average_price_of_a_game_in_this_category(self, obj):
        average_price = Game.objects.filter(category=obj).aggregate(Avg('price'))
        price = average_price['price__avg'].quantize(Decimal("1.0"))
        return f"{price} руб"