from django.contrib import admin

# Register your models here.



from .models import menu, cat

class menu_view(admin.ModelAdmin):
	list_display = ["name", "price", "cat", "des"]
	class Meta:
		model = menu



class cat_view(admin.ModelAdmin):
	list_display = ["cat_name", "cat_type"]
	class Meta:
		model = cat


admin.site.register(cat, cat_view)

admin.site.register(menu, menu_view)