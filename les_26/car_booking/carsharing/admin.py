from django.contrib import admin
from django.utils.safestring import mark_safe

from carsharing.models import Brand, Auto, AutoModel, Image
from carsharing.actions import set_status_auto_free, set_status_auto_booked


class AutoModelTabular(admin.TabularInline):
    model = AutoModel


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('url_image', 'title')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')

    inlines = (AutoModelTabular, )

    def logo(self, instance):
        if not instance.image:
            return mark_safe('<b>No Logo</b>')
        return mark_safe(f'<image src="/images/{instance.image.url_image}" style="max-width: 25px">')


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('vin_code', 'status', 'get_brand')
    list_filter = ('auto_model__brand', 'status')
    search_fields = ('vin_code', 'status')
    ordering = ('status', )

    actions = (set_status_auto_free, set_status_auto_booked)

    def get_brand(self, instance):
        return instance.auto_model.brand

    get_brand.short_description = 'Brand'


@admin.register(AutoModel)
class AutoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_of_autos')

    def count_of_autos(self, instance):
        count = Auto.objects.filter(auto_model__name=instance.name).count()
        return count

    count_of_autos.short_description = 'Auto'
