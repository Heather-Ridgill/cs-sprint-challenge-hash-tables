# Merging Two Packages

# Given a package with a weight limit `limit` and a list `weights` of item
# weights, implement a function `get_indices_of_item_weights` that finds
# two items whose sum of weights equals the weight limit `limit`.

cache = {}

def get_indices_of_item_weights(weights, length, limit):
    for i in range(len(weights)):
        cache[weights[i]] = i
    for j in range(len(weights)):
        a = limit - weights[j]
        if a in cache:
            return (max(j, cache[a]), min(j, cache[a]))

    return None

#print just in make sure the numbers go through...
if __name__ == "__main__":
    print(get_indices_of_item_weights([4, 6, 10, 15, 16], length = 5, limit = 21))
