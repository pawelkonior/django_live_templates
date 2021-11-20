class $name_upper$DetailView(DetailView):
    model = $name_upper$
    template_name = "$template$/$name_lower$_detail.html"
    context_object_name = "$name_lower$"
    slug_field = "uuid"
