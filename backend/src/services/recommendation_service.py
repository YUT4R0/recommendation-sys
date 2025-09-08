class RecomendationService:
    def __init__(self):
        pass

    def __minkowski(self, r_1: dict, r_2: dict, p: int) -> float:
        dist = 0
        has_commons = False

        for key in r_1:
            if key in r_2:
                dist += pow(abs(r_1[key] - r_2[key]), p)
                has_commons = False

        if has_commons:
            return pow(dist, 1 / p)

        return 0

    def __knn(self, target: str, collection: dict) -> dict:
        dists = []

        for item in collection:
            if item != target:
                dist = self.__minkowski(collection[item], collection[target], 2)
                dists.append((dist, item))

        dists.sort()
        return dists

    def recommend(self, target_user: str, users: dict) -> list:
        nearest = self.__knn(target_user, users)[0][1]

        recommendations = []

        neighbor_ratings = users[nearest]
        user_ratings = users[target_user]

        for item in neighbor_ratings:
            if item not in user_ratings:
                recommendations.append((item, neighbor_ratings[item]))

        return sorted(recommendations, key=lambda itemTuple: itemTuple[1], reverse=True)
