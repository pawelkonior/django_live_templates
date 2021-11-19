from django.db import models


class $name1$(models.Model):
    $name2$ = models.$name3$Field()
    $name4$ = models.ForeignKey('$name5$', on_delete=models.CASCADE, related_name='$name6$')

    def __str__(self):
        return f'{self.$name2$}'
