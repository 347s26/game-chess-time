from .models import Player, Ratings, GameInstance, Result, Move, Piece
from django.shortcuts import render

# Create your views here.
def index(request):

    # Home page view that shows some stats about the players, time controls, and elo ratings. We can alter this at any point.
    num_of_players = Player.objects.count()
    
    # Get all players with their highest elo rating
    players = Player.objects.all()
    players_blitz_5_data = []
    players_blitz_10_data = []
    players_rapid_15_data = []
    players_rapid_30_data = []
    
    for player in players:
        # Build Blitz (5 minutes) list
        try:
            ratings = player.ratings
            players_blitz_5_data.append({
                'player': player,
                'elo': ratings.rating_5_min
            })
        except Ratings.DoesNotExist:
            players_blitz_5_data.append({
                'player': player,
                'elo': 0
            })
        
        # Build Blitz (10 minutes) list
        try:
            ratings = player.ratings
            players_blitz_10_data.append({
                'player': player,
                'elo': ratings.rating_10_min
            })
        except Ratings.DoesNotExist:
            players_blitz_10_data.append({
                'player': player,
                'elo': 0
            })
        
        # Build Rapid (15 minutes) list
        try:
            ratings = player.ratings
            players_rapid_15_data.append({
                'player': player,
                'elo': ratings.rating_15_min
            })
        except Ratings.DoesNotExist:
            players_rapid_15_data.append({
                'player': player,
                'elo': 0
            })
        
        # Build Rapid (30 minutes) list
        try:
            ratings = player.ratings
            players_rapid_30_data.append({
                'player': player,
                'elo': ratings.rating_30_min
            })
        except Ratings.DoesNotExist:
            players_rapid_30_data.append({
                'player': player,
                'elo': 0
            })
    
    # Sort by highest elo rating in descending order
    players_blitz_5_data.sort(key=lambda x: x['elo'], reverse=True)
    players_blitz_10_data.sort(key=lambda x: x['elo'], reverse=True)
    players_rapid_15_data.sort(key=lambda x: x['elo'], reverse=True)
    players_rapid_30_data.sort(key=lambda x: x['elo'], reverse=True)
  
    context = {
        'num_of_players': num_of_players,
        'players_blitz_5': players_blitz_5_data,
        'players_blitz_10': players_blitz_10_data,
        'players_rapid_15': players_rapid_15_data,
        'players_rapid_30': players_rapid_30_data,
    }
    
    return render(request, 'index.html', context=context)