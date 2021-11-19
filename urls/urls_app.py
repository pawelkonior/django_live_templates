from django.urls import path
from $name$ import views

app_name = '$name$'

urlpatterns = [
    path('$name$/', views.$name_upper$View.as_view(), name="$name$"),
]

# in edit variables   name_upper -> capitalize(name)