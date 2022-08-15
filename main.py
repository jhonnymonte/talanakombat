import os
import json

from challenge import set_up_and_run_match

if __name__ == '__main__':
    filename = "game_stats.json"

    with open(filename) as json_match_data:
        match_data = json.load(json_match_data)
    
    set_up_and_run_match(match_data)