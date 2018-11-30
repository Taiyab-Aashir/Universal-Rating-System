from django.contrib.syndication.views import Feed
from .models import *
from django.urls import reverse


class Feeed(Feed):
    title = "Best Rated Games"
    link = "/drcomments/"
    description = "The most competitive and zealous games."

    def items(self):
        l = GameItem.objects.all().order_by("-game_rating")[:5]
        return l

    def item_title(self, item):
        return item.game_name

    def item_description(self, item):
        return item.game_description

    def item_link(self, item):
        return reverse('comment')
