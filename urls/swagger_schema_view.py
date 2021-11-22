schema_view = get_schema_view(
   openapi.Info(
      title="$title$",
      default_version="$version$",
      description="$description$",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
