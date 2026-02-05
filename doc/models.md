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
- Black (Player ID)
- White (Player ID)
- Black timer (Derived)
- White timer (Derived)
- Moves (list of moves)
- Result ID

## Result
- ID
- Result (Win, Lose, or Draw)
- Player ID

## Move
- ID
- Timestamp (Relative to game start)
- Player ID
- Game Instance ID
- Piece ID
- Source Location
- Destination Location

## Piece
- ID
- Name