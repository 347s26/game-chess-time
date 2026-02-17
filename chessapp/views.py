from .models import Player, Ratings, GameInstance, Result, Move, Piece
from django.shortcuts import render

# Create your views here.
def index(request):

    # Home page view that shows some stats about the players, time controls, and elo ratings. We can alter this at any point.
    num_of_players = Player.objects.count()
    
    # Get all players with their highest elo rating
    players = Player.objects.all()
    players_data = []
    
    for player in players:
        try:
            ratings = player.ratings
            highest_elo = max(ratings.rating_5_min, ratings.rating_10_min, ratings.rating_15_min, ratings.rating_30_min)
        except Ratings.DoesNotExist:
            highest_elo = 0
        
        players_data.append({
            'player': player,
            'highest_elo': highest_elo
        })
    
    # Sort by highest elo rating in descending order
    players_data.sort(key=lambda x: x['highest_elo'], reverse=True)
  
    context = {
        'num_of_players': num_of_players,
        'players': players_data,
    }
    
    return render(request, 'index.html', context=context)