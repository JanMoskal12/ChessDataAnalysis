# ChessDataAnalysis

## `cleaned_data.csv`

### Data Dictionary

| variable                          | class     | description                                   |
|:-----------------------|:-----------------|:-----------------------------|
| id                                | character | Game id                                       |
| variant                           | factor    | Type of game variant                          |
| speed                             | factor    | Time format                                   |
| status                            | factor    | Game status (resign, draw, etc.)              |
| players_white_user_name           | character | White player's username                       |
| players_white_user_title          | factor    | White player's title                          |
| players_white_rating              | integer   | White player's rating                         |
| players_white_analysis_inaccuracy | integer   | White player's of inaccuracies in game        |
| players_white_analysis_mistake    | integer   | White player's analysis of mistakes in game   |
| players_white_analysis_blunder    | integer   | White player's analysis of blunders in game   |
| players_white_analysis_acpl       | integer   | White player's average centipawn loss         |
| players_white_provisional         | logical   | White player's provisional status             |
| players_black_user_name           | character | Black player's username                       |
| players_black_user_title          | factor    | Black player's title                          |
| players_black_rating              | integer   | Black player's rating                         |
| players_black_analysis_inaccuracy | integer   | Black player's number of inaccuracies in game |
| players_black_analysis_mistake    | integer   | Black player's number of mistakes in game     |
| players_black_analysis_blunder    | integer   | Black player's number of blunders in game     |
| players_black_analysis_acpl       | integer   | Black player's average centipawn loss         |
| players_black_provisional         | logical   | Black player's provisional status             |
| winner                            | factor    | Winner of the game                            |
| opening_eco                       | factor    | Opening ECO code                              |
| opening_name                      | character | Full opening name                             |
| moves                             | character | Moves in the game                             |
| analysis_eval                     | character | Analysis evaluation for every move (ACPL)     |
| duration_in_milliseconds          | integer   | Duration of game in milliseconds              |
