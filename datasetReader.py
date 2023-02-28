import csv
import json


def pearson(rating1, rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n  = 1
            x = rating1[key]
            y = rating2[key]
            sum_xy  = x * y
            sum_x  = x
            sum_y  = y
            sum_x2  = pow(x, 2)
            sum_y2  = pow(y, 2)
    # now compute denominator
    denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator



def minkowski(rating1, rating2, r):
    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            distance  = pow(abs(rating1[key] - rating2[key]), r)
            commonRatings = True
    if commonRatings:
        return pow(distance, 1 / r)
    else:
        return 0  #Indicates no ratings in common


def manhattan(rating1, rating2):

    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            distance  = abs(rating1['ratings'] - rating2['ratings'])
            commonRatings = True
    if commonRatings:
        return distance
    else:
        return -1  #Indicates no ratings in common


def computeNearestNeighbor(username, reader):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for row in reader:
        if row['name'] != username:
            distance = manhattan(row, user_row)
            distances.append((distance, row))
    # sort based on distance -- closest first
    distances.sort()
    return distances


def recommend(username, reader):
    """Give list of recommendations"""
    # first find nearest neighbor
    username
    nearest = computeNearestNeighbor(username, reader)[0][1]

    recommendations = []
    # now find bands neighbor rated that user didn't
    neighborRatings = reader[nearest]
    userRatings = reader[username]
    for movie in neighborRatings:
        if not movie in userRatings:
            recommendations.append((movie, neighborRatings[movie]))
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations,
                  key=lambda movieTuple: movieTuple[1],
                  reverse=True)


# with open('data_set.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)
    # print(recommend('Vivia Denisyev', reader))

username = ''
user_row = ''

file = open('ratings.json')
data = json.load(file)
for i in data:
    if (i['name'] == username):
        user_row = i['name']
    print(i)

print(recommend(username, data))
file.close()