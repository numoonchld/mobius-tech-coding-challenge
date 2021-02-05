import pprint

waiting_users = [{"username": "lyingOrange6", "skill": 62, "user_level": 2, "waiting_time": 4}, {"username": "betrayedSnipe6", "skill": 25, "user_level": 4, "waiting_time": 32}, {"username": "morbidDove1", "skill": 92, "user_level": 0, "waiting_time": 47}, {"username": "decimalCheese8", "skill": 94, "user_level": 4, "waiting_time": 82}, {"username": "lazySnail8", "skill": 29, "user_level": 2, "waiting_time": 47}, {"username": "shamefulBuzzard5", "skill": 72, "user_level": 2, "waiting_time": 51}, {"username": "giddyBuck3", "skill": 71, "user_level": 1, "waiting_time": 30}, {"username": "panickyToucan5", "skill": 23, "user_level": 2, "waiting_time": 62}, {"username": "cynicalCordial3", "skill": 26, "user_level": 2, "waiting_time": 15}, {"username": "zestyMagpie5", "skill": 26, "user_level": 2, "waiting_time": 46}, {"username": "dearEggs6", "skill": 47, "user_level": 2, "waiting_time": 88}, {"username": "grudgingPup3", "skill": 72, "user_level": 4, "waiting_time": 0}, {"username": "artisticMallard1", "skill": 75, "user_level": 3, "waiting_time": 42}, {"username": "solidSausage3", "skill": 9, "user_level": 1, "waiting_time": 24}, {"username": "awedAntelope0", "skill": 33, "user_level": 3, "waiting_time": 13}, {"username": "jealousBoars7", "skill": 28, "user_level": 2, "waiting_time": 84}, {"username": "pridefulBobolink8", "skill": 5, "user_level": 1, "waiting_time": 22}, {"username": "needyEagle6", "skill": 49, "user_level": 1, "waiting_time": 1}, {"username": "cockyBustard3", "skill": 88, "user_level": 4, "waiting_time": 15}, {"username": "pleasedBuck8", "skill": 64, "user_level": 4, "waiting_time": 63}, {"username": "hushedJaguar8", "skill": 77, "user_level": 1, "waiting_time": 47}, {"username": "pitifulCaribou6", "skill": 47, "user_level": 3, "waiting_time": 67}, {"username": "adoringSeafowl8", "skill": 53, "user_level": 3, "waiting_time": 74}, {"username": "peskyMandrill7", "skill": 53, "user_level": 4, "waiting_time": 21}, {"username": "kindSeafowl4", "skill": 44, "user_level": 4, "waiting_time": 72}, {"username": "shyCheetah0", "skill": 92, "user_level": 4, "waiting_time": 76}, {"username": "grizzledBoa6", "skill": 96, "user_level": 4, "waiting_time": 37}, {"username": "similarSeagull6", "skill": 51, "user_level": 3, "waiting_time": 48}, {"username": "obsessedMoth2", "skill": 10, "user_level": 1, "waiting_time": 79}, {"username": "sincereBoa1", "skill": 23, "user_level": 4, "waiting_time": 67}, {"username": "humorousHoopoe5", "skill": 4, "user_level": 0, "waiting_time": 33}, {"username": "thriftyLapwing1", "skill": 39, "user_level": 1, "waiting_time": 44}, {"username": "outlyingApricots1", "skill": 64, "user_level": 3, "waiting_time": 69}, {"username": "eagerCow2", "skill": 94, "user_level": 4, "waiting_time": 89}, {"username": "shyCockatoo9", "skill": 62, "user_level": 2, "waiting_time": 59}, {"username": "worriedChile9", "skill": 72, "user_level": 3, "waiting_time": 2}, {"username": "dopeyWhiting7", "skill": 37, "user_level": 2, "waiting_time": 5}, {"username": "cheerfulMoth9", "skill": 4, "user_level": 2, "waiting_time": 46}, {"username": "grudgingPorpoise3", "skill": 76, "user_level": 4, "waiting_time": 40}, {"username": "trustingOrange7", "skill": 80, "user_level": 4, "waiting_time": 72}, {"username": "dopeyChamois3", "skill": 80, "user_level": 0, "waiting_time": 50}, {"username": "peacefulGatorade4", "skill": 19, "user_level": 4, "waiting_time": 26}, {"username": "cruelEland7", "skill": 47, "user_level": 0, "waiting_time": 21}, {"username": "aboardWasp3", "skill": 12, "user_level": 4, "waiting_time": 34}, {"username": "grudgingGelding4", "skill": 75, "user_level": 1, "waiting_time": 36}, {"username": "cockyHare2", "skill": 41, "user_level": 0, "waiting_time": 56}, {"username": "guiltyPolenta9", "skill": 91, "user_level": 0, "waiting_time": 42}, {"username": "scornfulTacos5", "skill": 48, "user_level": 1, "waiting_time": 64}, {"username": "pluckyAntelope3", "skill": 93, "user_level": 0, "waiting_time": 88}, {"username": "holisticChough1", "skill": 25, "user_level": 3, "waiting_time": 78}]
match_config = {"s_weight": 5, "l_weight": 25, "t_weight": 2}

def get_matches(waiting_users, match_config):


    # TODO given match config, function to compute distance score between a user pair 

    def compute_distance_score(user_pair, match_config):
        user_a = user_pair[0]
        user_b = user_pair[1]
        distance_score = ( match_config["s_weight"] * abs(user_a["skill"] - user_b["skill"]) ) \
            + ( match_config["l_weight"] * abs(user_a["user_level"] - user_b["user_level"]) ) \
            + ( match_config["t_weight"] * abs(user_a["waiting_time"] - user_b["waiting_time"]) )
        return distance_score
          
    # TODO generate all combinations of user pairs
    pairs_list = []

    for base_index in range(len(waiting_users)):
        for floating_index in range(base_index+1,len(waiting_users)):
            pairs_list.append([waiting_users[base_index],waiting_users[floating_index]])

    # TODO compute distance score for each pair
    score_list = []

    score_list = [ 
                    {
                        "match_id": idx, \
                        "user_a": item[0]["username"], \
                        "user_b": item[1]["username"], \
                        "match_score": compute_distance_score([item[0],item[1]], match_config) \
                    }  for idx,item in enumerate(pairs_list)
                ]

    # TODO sort the pairs by descending order of distance score
    
    sorted_score_list = sorted(score_list, key=lambda item: item["match_score"])
    # pprint.pprint(sorted_score_list[0:5])

    # TODO select top 25 pairs combinations 

    ## TODO scroll through the sorted_score_list, 
    # this is in increasing order of distance - the lowest appers first, leverage this to 'null' the higher distance IDs
    # hold current ID and null the rest of the IDs either users occur in sorted_score_list 48*2 ID should be nulled for the 25 non-nulled IDs
    # go to next one; if ID is null, skip entry and go to next one and repeat 
    # at the end, sorted list will have have only 25 non-null IDs
    

    def is_repeat_match(match_a,match_b):

        if match_a['user_a'] == match_b['user_a'] or match_a['user_b'] == match_b['user_b'] or match_a['user_a'] == match_b['user_b'] or match_a['user_b'] == match_b['user_a']:
            return True
        else: return False


    for index, base_match in enumerate(sorted_score_list):
        if base_match['match_id'] != None:
            for test_match_index in range(index+1, len(sorted_score_list)):
                test_match = sorted_score_list[test_match_index]
                if is_repeat_match(base_match, test_match):
                    sorted_score_list[test_match_index]['match_id'] = None
                else: 
                    continue


    non_null_id_matches = [ match for match in sorted_score_list if match['match_id'] is not None ]

    # TODO output the combination in required format

    formatted_matches = { "matches": {}}

    for match in non_null_id_matches:
        # print(match["user_a"],match["user_b"])
        formatted_matches["matches"][match["user_a"]] = match["user_b"]

    return formatted_matches



if __name__ == '__main__':
    matches = get_matches(waiting_users, match_config)
    print(matches)