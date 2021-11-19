from django.views.generic import ListView
from $name1$.models import $name2$


class $name2$ListView(ListView):
    model = $name2$
    context_object_name = '$name2_lower$_list'
    template_name = '$name1$/$name2_lower$_list.html'

    # in edit variable   name2_lower ->  decapitalize(name2)
