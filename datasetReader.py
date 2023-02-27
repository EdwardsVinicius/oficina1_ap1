import csv

with open('data_set.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'])


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
            distance  = abs(rating1[key] - rating2[key])
            commonRatings = True
    if commonRatings:
        return distance
    else:
        return -1  #Indicates no ratings in common


def computeNearestNeighbor(username, users):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
    # sort based on distance -- closest first
    distances.sort()
    return distances


def recommend(username, users):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = computeNearestNeighbor(username, users)[0][1]

    recommendations = []
    # now find bands neighbor rated that user didn't
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations,
                  key=lambda artistTuple: artistTuple[1],
                  reverse=True)


print(recommend('Vivia Denisyev', reader))