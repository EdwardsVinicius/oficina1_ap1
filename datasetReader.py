from math import sqrt

users = {
    "Vinicius": {
        "Dark Souls":2.5,
        "God of War":0.7,
        "The Legend of Zelda: Breath of the Wild":3.2,
        "Minecraft":1.7,
        "The Last of Us":4.7,
        "Terraria":4.8,
        "Hollow Knight":0.0,
        "Persona 5 Royal":1.2,
        "Super Mario Odyssey":2.4,
        "Call of Duty: Black Ops II":3.3,
        "Super Mario 64":4.0,      
    },
    "Evandro": {
        "Portal 2":4.7,
        "Super Mario Galaxy":3.6,
        "The Elder Scrolls V: Skyrim":1.1,
        "Red Dead Redemption 2":1.4,
        "Minecraft":2.7,
        "Left 4 Dead 2":2.9,
        "Uncharted 4: A Thief's End":3.8,
        "Call of Duty: Modern Warfare 2":3.5,
        "The Last of Us Part II":4.6,
        "Super Smash Bros. Ultimate":4.5,
        "Grand Theft Auto V":3.4,
        "The Legend of Zelda: Breath of the Wild":3.3,
        "Left 4 Dead 2":0.9,
        "Team Fortress 2":2.7,
        "Persona 5 Royal":4.6,
    },
    "Marvin": {
        "Grand Theft Auto: San Andreas":4.7,
        "Grand Theft Auto V":4.5,
        "The Legend of Zelda: Ocarina of Time":2.0,
        "Red Dead Redemption 2":0.8,
        "The Legend of Zelda: Breath of the Wild":0.3,
        "Super Mario Galaxy":4.6,
        "Halo 3":2.3,
        "Stardew Valley":2.2,
    },
    "Caio": {
        "Super Mario Odyssey":0.2,
        "Hollow Knight":2.0,
        "Persona 5 Royal":1.1,
        "Team Fortress 2":4.5,
        "Grand Theft Auto: San Andreas":0.1,
        "Super Smash Bros. Ultimate":2.5,
        "The Last of Us Part II":4.9,
        "Grand Theft Auto V":3.6,
        "Portal 2":1.3,
        "Halo 3":4.1,
        "Cuphead":3.8,
        "Red Dead Redemption":0.5,
        "The Witcher 3: Wild Hunt":1.6,
    },
    "Hugo": {
        "Undertale":0.9,
        "Persona 5 Royal":0.0,
        "Halo 3":4.8,
        "Portal 2":1.8,
        "Super Mario Galaxy":1.6,
        "Call of Duty: Black Ops II":3.9,
        "The Last of Us":2.9,
        "Grand Theft Auto: San Andreas":1.0,
        "The Elder Scrolls V: Skyrim":4.6,
        "Call of Duty: Black Ops II":4.4,
        "God of War":0.4,
        "Red Dead Redemption":1.8,
    },
    "Pique": {
        "Super Mario Galaxy":3.3,
        "Halo 3":1.7,
        "The Elder Scrolls V: Skyrim":1.1,
        "Super Mario 64":0.5,
        "Red Dead Redemption":3.1,
        "The Witcher 3: Wild Hunt":3.8,
        "Undertale":3.7,
        "Uncharted 4: A Thief's End":1.6,
        "Cuphead":1.0,
        "Team Fortress 2":0.1,
        "The Last of Us Part II":0.8,
    },
    "Shakira": {
        "Left 4 Dead 2":3.1,
        "Red Dead Redemption 2":0.6,
        "The Witcher 3: Wild Hunt":3.2,
        "Super Mario Galaxy":1.9,
        "Halo 3":4.6,
        "God of War":2.6,
        "Grand Theft Auto V":2.5,
        "Cuphead":4.6,
        "Call of Duty: Modern Warfare 2":2.2,
        "The Legend of Zelda: Ocarina of Time":0.3,
        "Persona 5 Royal":4.5,
    },
    "John": {
        "Halo 3":4.3,
        "Stardew Valley":3.5,
        "The Last of Us":4.5,
        "Red Dead Redemption 2":0.6,
        "Left 4 Dead 2":4.7,
        "The Witcher 3: Wild Hunt":2.5,
        "Undertale":0.1,
        "Minecraft":4.1,
        "Dark Souls":1.8,
        "The Legend of Zelda: Breath of the Wild":4.0,
        "The Legend of Zelda: Ocarina of Time":4.0,
    }
}

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
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
    # sort based on distance -- closest first
    distances.sort()
    return distances


def recommend(username, users=users):
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


# examples - uncomment to run

# print(users["Veronica"])
# print(manhattan(users["Hailey"], users["Veronica"]))

# print(computeNearestNeighbor("Dan", users))
# print(recommend("Vinicius", users))
