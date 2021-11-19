from django.views.generic import TemplateView

class $name1$View(TemplateView):
    template_name = '$name2$/$name1_lower$.html'

    # in edit variables    name1_lower -> decapitalize(name1)

