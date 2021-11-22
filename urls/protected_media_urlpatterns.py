@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, protected_serve, document_root=settings.MEDIA_ROOT)
