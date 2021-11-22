class $name_upper$UpdateView(UpdateView):
    model = $name_upper$
    fields = [$fields$]
    template_name = '$app$/update_$name$.html'
    context_object_name = '$name$'
    success_url = reverse_lazy('$app$:$name$_list')
