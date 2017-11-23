from boardgamegeek import BoardGameGeek 
from boardgamegeek import BoardGameGeekAPIError
import pandas as pd
bgg = BoardGameGeek()
gameframe = pd.DataFrame({"Name":[],
                              "Year":[],
                              "ID":[],
                              "BGGRank":[],
                              "Mechanics":[],
                              "Playtime":[],
                              "Min_Age":[],
                              "Median_Rating":[],
                              "Bays_Rating":[]})
for i in range(1,12):
    try:
        g = bgg.game(game_id=i)
        gamedat = pd.DataFrame({"Name":[g.name],
                                "ID":[g.id],
                                "Year":[g.year],
                                "BGGRank":[g.boardgame_rank],
                                "Mechanics":[g.mechanics],
                                "Playtime":[g.playing_time],
                                "Min_Age":[g.min_age],
                                "Median_Rating":[g.rating_median],
                                "Bays_Rating":[g.rating_bayes_average]})

        gameframe = pd.concat([gameframe,gamedat])
    except BoardGameGeekAPIError:
        pass
gameframe.to_csv("Game_Data.csv")
