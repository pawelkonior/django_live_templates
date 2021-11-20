class $name_upper$CreateView(CreateView):
    form_class = $name_upper$Form
    success_url = reverse_lazy("$url$")
    template_name = "$app$/$name_lower$.html"
