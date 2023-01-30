from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author',)
    # para buscar algun dato y que el buscador se active
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    # para que en la parte superior aparezca la fecha
    date_hierarchy = 'published'
    # crea los filtros
    list_filter = ('title', 'author__username', 'categories__name')

    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorias'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
