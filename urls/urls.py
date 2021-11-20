from django.urls import path, include

from $name$ import views


app_name = '$name$'

urlpatterns = [
	path('$name$/', views.$name_upper$View.as_view(), name="$name$"),
]
