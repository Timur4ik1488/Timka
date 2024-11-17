from django.contrib import admin

#здесь будем регистрировать БД для отображения её в админ-панели

from goods.models import Categories, Products

# admin.site.register(Categories) #регистрировали категории изначально при помощи данного способа
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)  #теперь поле slug в БД будет транслитерироваться и заполняться автоматически, очень удобно, ОБЯЗАТЕЛЬНО СЕБЕ НА ЗАМЕТКУ НАДО ВЗЯТЬ!!!!!!
    }
                #здесь мы перепрописали категории при помощи более универсального способа, а именно классов
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',) 
    }