from django.contrib import admin
from django.http import HttpResponse
from django.db.models import Avg

from decimal import Decimal
import csv

from .models import Game, Category, Comment


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'price', 'category', 'average_grade_game', 'is_active')  
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

    @admin.display(description='Средняя оценка игры')
    def average_grade_game(self, obj):
        average_grade = Comment.objects.filter(game=obj).aggregate(Avg('grade'))
        return average_grade['grade__avg']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'games_amount', 'average_price_of_a_game_in_this_category', 'is_active')

    @admin.display(description='Средняя цена игр в категории')
    def average_price_of_a_game_in_this_category(self, obj):
        average_price = Game.objects.filter(category=obj).aggregate(Avg('price'))
        return average_price['price__avg'].quantize(Decimal("1.0"))   
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'game', 'pub_date', 'grade')
    list_filter = ('pub_date',)