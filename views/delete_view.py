class $name_upper$DeleteView(DeleteView):
    model = $name_upper$
    template_name = '$app$/delete_$name$.html'
    success_url = reverse_lazy('$app$:$name$_list')
