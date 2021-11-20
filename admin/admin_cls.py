from $name$s.models import $name_upper$


class $name_upper$Admin(admin.ModelAdmin):
    list_display = [$END$]


admin.site.register($name_upper$, $name_upper$Admin)
