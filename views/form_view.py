class $name_upper$FormView(FormView):
    template_name = "$app$/$name_lower$_form.html"
    form_class
    "name_upper$Form
    success_url = reverse_lazy("$url$")

    def form_valid(self, form):
        $END$
        return super().form_valid(form)
