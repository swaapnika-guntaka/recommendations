#!/usr/bin/env python3

def calculate_manhattan_distance(user_scores):
    score_dict = {}
    for xuser in user_scores:
        score_dict[xuser] = {}
        for yuser in user_scores:
            distance = 0
            if xuser != yuser:
                for movie in user_scores[xuser]:
                    if movie in user_scores[yuser]:
                        distance += abs(user_scores[xuser][movie] - user_scores[yuser][movie])
                score_dict[xuser][yuser] = distance
    return score_dict


def get_nearest_neighbor(user_scores):
    similar_users = {}
    score_dict = calculate_manhattan_distance(user_scores)
    for user in score_dict:
        nearest_neighbor = ''
        min = 1000
        for neighbor, score in score_dict[user].items():
            if score <= min :
                min = score
                nearest_neighbor = neighbor
        similar_users[user] = nearest_neighbor
    print(similar_users)
    return similar_users

def get_recommendations(user_scores):
    recommendations = {}
    similar_users = get_nearest_neighbor(user_scores)
    for user in similar_users:
        recommendations[user] = []
        for movie in user_scores[similar_users[user]]:
            if movie not in list(user_scores[user].keys()) :
                recommendations[user].append((movie, user_scores[similar_users[user]][movie]))
    return recommendations


def main():
    user_movie_ratings = {'Amy': {'Family Plot': 10, 'Rebecca': 5, 'Spellbound': 9, 'Star Trek': 6},
                          'Bill': {'Apocalypto': 8, 'Braveheart': 3, 'Rebecca': 10, 'Spellbound': 5, 'Star Trek': 7},
                          'Cathy': {'Spaceballs': 7, 'The Ice Storm': 4, 'Family Plot': 5, 'Rebecca': 9,
                                    'Spellbound': 1},
                          'Dave': {'Braveheart': 5, 'Rebecca': 7, 'Spellbound': 4},
                          'Ernie': {'Apocalypto': 3, 'Braveheart': 8, 'Rebecca': 1, 'Star Trek': 7},
                          'Fiona': {'The Ice Storm': 3, 'Family Plot': 10, 'Rebecca': 6, 'Spellbound': 10}}
    print(get_recommendations(user_movie_ratings))


if __name__ == "__main__":
    main()
