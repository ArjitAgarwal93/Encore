from django.contrib import admin
from .models import Product ,Article,Tag,Profile,Vote
# Register your models here.
class VoteAdmin(admin.ModelAdmin):
    list_display = ('profile', 'product', 'comfort', 'performance', 'durability')
    search_fields = ('profile__user__username', 'product__name')

admin.site.register(Vote, VoteAdmin)

admin.site.register(Product)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Profile)
# admin.site.register(Vote)