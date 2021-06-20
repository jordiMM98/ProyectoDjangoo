from django.contrib import admin
from .models import  Page

#configuracion extra
class PageAdmin(admin.ModelAdmin):
	readonly_fields =('created_at', 'updated_at')
	#buscador search
	search_fields = ('title','content')
	#se le pone la coma para que identifique que es una tupla
	list_filter = ('visible',)
	#columnas visibles
	list_display = ('title','visible','created_at')
	#se le pone , porqu ee sun atupla
	ordering = ('created_at',)

# Register your models here.
admin.site.register(Page,PageAdmin)
#configuracion del panel 
title = "Proyecto con Django"
subtitle = "Panel de gestion"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
