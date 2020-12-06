from django.contrib import admin

# Register your models here.
from gears.models import Gear, Like

from gears.models import Comment


class LikeInLine(admin.TabularInline):
    model = Like



class GearAdmin(admin.ModelAdmin):
    list_display = ('name','type','price','id',)
    list_filter = ('price',)
    inlines = (
        LikeInLine,
    )


admin.site.register(Gear, GearAdmin)
# admin.site.register(Like))
admin.site.register(Comment)
