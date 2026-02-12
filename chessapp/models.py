from django.db import models
from django.urls import reverse

# Create your models here.


class Player(models.Model):
    username: models.CharField = models.CharField(max_length=50, unique=True)
    email: models.EmailField = models.EmailField(unique=True)
    date_created: models.DateTimeField = models.DateTimeField()
    last_online: models.DateTimeField = models.DateTimeField()
    elo: models.ForeignKey = models.ForeignKey('Elo', on_delete=models.CASCADE, related_name="player_elo")

    # Check player stats via their username
    def get_absolute_url(self):
        return reverse('player', args=[str(self.username)])

    def __str__(self):
        return f"{self.username}"


class Elo(models.Model):
    elo_id: models.AutoField = models.AutoField(primary_key=True)
    time_control_id: models.ForeignKey = models.ForeignKey(
        'TimeControl', on_delete=models.CASCADE)
    player_id: models.ForeignKey = models.ForeignKey(
        'Player', on_delete=models.CASCADE, related_name="elo_player_id")
    rating: models.IntegerField = models.IntegerField(default=800)

    def __str__(self):
        return f"{self.player_id.username} - {self.rating} ({self.time_control_id.time} + {self.time_control_id.increment})"


class TimeControl(models.Model):
    player_id: models.ForeignKey = models.ForeignKey(
        'Player', on_delete=models.CASCADE)

    TIME_CONTROL = (
        (5, '5 minutes'),
        (10, '10 minutes'),
        (15, '15 minutes'),
        (30, '30 minutes'),
    )
    time: models.IntegerField = models.IntegerField(
        choices=TIME_CONTROL, 
        default=5, 
        help_text='Time Control in minutes'
    )

    def __str__(self):
        return f"{self.time}"


class GameInstance(models.Model):
    time_control: models.ForeignKey = models.ForeignKey(
        "TimeControl", on_delete=models.CASCADE)
    started: models.DateTimeField = models.DateTimeField()
    ended: models.DateTimeField = models.DateTimeField()
    black: models.ForeignKey = models.ForeignKey(
        "Player", on_delete=models.CASCADE, related_name="gameinstance_player_black")
    white: models.ForeignKey = models.ForeignKey(
        "Player", on_delete=models.CASCADE, related_name="gameinstance_player_white")
    result: models.ForeignKey = models.ForeignKey(
        "Result", on_delete=models.CASCADE)
    

    # Sort by started date by default
    class Meta:
        ordering: list[str] = ['started']

    def get_absolute_url(self):
        """Returns the URL to access a particular game instance."""
        return reverse('game', args=[str(self.id)])

    def __str__(self):
        return f"GameInstance(id={self.id}, time_control={self.time_control}, started={self.started}, ended={self.ended}, black={self.black}, white={self.white}, result={self.result})"


class Result(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    RESULT_STATUS = (
        ('w', 'Win'),
        ('l', 'Lose'),
        ('d', 'Draw'),
    )
    result: models.CharField = models.CharField(
        max_length=1,
        choices=RESULT_STATUS,
        blank=True,
        default='w',
        help_text='Game Result',
    )
    player_id: models.ForeignKey = models.ForeignKey(
        'Player', on_delete=models.CASCADE)

    def __str__(self):
        return f"Result(id={self.id}, player_id={self.player_id}, result={self.result})"


class Move(models.Model):
    timestamp: models.DateTimeField = models.DateTimeField()
    player_id: models.ForeignKey = models.ForeignKey(
        'Player', on_delete=models.CASCADE)
    game_instance: models.ForeignKey = models.ForeignKey(
        'GameInstance', on_delete=models.CASCADE)
    piece_id: models.ForeignKey = models.ForeignKey(
        'Piece', on_delete=models.CASCADE)
    source_location: models.CharField = models.CharField(max_length=2)
    destination_location: models.CharField = models.CharField(max_length=2, null=True, blank=True) # Allow null for initial piece positions

    def __str__(self):
        return f"Move(id={self.id}, player={self.player_id.username}, piece={self.piece_id.name}, from={self.source_location}, to={self.destination_location}, time={self.timestamp})"


class Piece(models.Model):
    name: models.CharField = models.CharField(max_length=20)
    color: models.CharField = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.color} {self.name}"
