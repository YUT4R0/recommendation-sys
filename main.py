# get nearest neighborhud
def computeNearestNeighbors(username: str, users: Lists):
    distances = []

    for user in users:
        if user != username:
            dist = minkowski(users[user], users[username], 2)
            distances.append((dist, user))

    distances.sort()
    return distances
    
    
# generate recommendation based on nearest neighbohuds
def recommend(username: str, users: Lists):
    nearest = computeNearestNeighbors(username, users)[0][i]
    recommendations = []

    neigRatings = users[nearest]
    userRatings = users[username]

    for artist in neigRatings:
        if artist not in userRatings:
            recommendations.append((artist, neigRatings[artist]))

    return sorted(recommendations, key=lambda artTuple: artTuple[1], reverse=True)


