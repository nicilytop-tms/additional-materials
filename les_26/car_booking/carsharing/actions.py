def set_status_auto_free(admin_model, request, queryset):
    for instance in queryset:
        instance.status = '1'
        instance.save()


def set_status_auto_booked(admin_model, request, queryset):
    for instance in queryset:
        instance.status = '2'
        instance.save()
