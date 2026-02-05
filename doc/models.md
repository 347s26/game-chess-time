# Entities
## Player
- ID
- Username
- Email
- Date Created
- Last Online
- Elo ID

## Elo
- ID
- Player ID
- Time Control ID
- Rating

## Time Control
- ID
- Time
- Increment

## Game Instance
- ID
- Time Control ID
- Started Timestamp
- Ended Timestamp
- Black [Player ID]
- White [Player ID]
- Moves (list of moves)

## Move
- ID
- Timestamp (Relative to game start)
- Player ID
- Game Instance ID
- Piece
- Source Location
- Destination Location