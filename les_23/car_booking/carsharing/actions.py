def set_status_auto_free(**kwargs):
    for instance in kwargs['queryset']:
        instance.status = '1'
        instance.save()
