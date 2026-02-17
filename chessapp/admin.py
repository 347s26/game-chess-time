from django.contrib import admin
from .models import Player, Ratings, GameInstance, Move, Piece, Result

# Register your models here.
admin.site.register(Player)
admin.site.register(Ratings)
admin.site.register(GameInstance)
admin.site.register(Move)
admin.site.register(Piece)
admin.site.register(Result)
