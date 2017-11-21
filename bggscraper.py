from boardgamegeek import BGGClient
from boardgamegeek import BGGApiError
import pandas as pd
gameframe = pd.DataFrame({"Name":[],
                              "Year":[],
                              "ID":[],
                              "BGGRank":[],
                              "Mechanics":[],
                              "Playtime":[],
                              "Min_Age":[],
                              "Median_Rating":[],
                              "Bays_Rating":[]})
for i in range(1,120000):
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
    except BGGApiError:
        pass
gameframe.to_csv("Game_Data.csv")
