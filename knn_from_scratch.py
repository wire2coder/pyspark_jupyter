""" 
    Importatnt Requirement
    Pythong 2.7, Pythong 3
    PySpark 2
    Java 8

    'k-nearest neigbors' 
    https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761
 """


from collections import Counter
import math
import math

def knn(data, query, k, distance_fn, choice_fn):
    neighbor_distances_and_indices = []
    
    # 3. For each example in the data
    for index, example in enumerate(data):

        # debug
        print("\n\n")
        print("query", query)
        print("example[:-1]", example[:-1])

        # 3.1 Calculate the distance between the query example and the current
        # example from the data.
        distance = distance_fn(example[:-1], query)

        # debug        
        print("distance", distance)
        print("index for distance", index)
        
        # 3.2 Add the distance and the index of the example to an ordered collection
        neighbor_distances_and_indices.append((distance, index))
    
    # 4. Sort the ordered collection of distances and indices from
    # smallest to largest (in ascending order) by the distances
    sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)

    # debug 
    print("\n\n")
    print("sorted_neighbor_distances_and_indices", sorted_neighbor_distances_and_indices)
    
    # 5. Pick the first K entries from the sorted collection
    k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]

    print("\n\n")
    print("k_nearest_distances_and_indices", k_nearest_distances_and_indices)
    
    # 6. Get the 'labels' of the selected K entries
    k_nearest_labels = [ data[i][1] for distance, i in k_nearest_distances_and_indices ]

    # debug
    print("\n\n") 
    print("data[i][0], k_nearest_labels", k_nearest_labels)

    # for distance, i in k_nearest_distances_and_indices:
    #     print("\n\n")
    #     print("distance", distance)
    #     print("i", i)


    # 7. If regression (choice_fn = mean), return the average of the K labels
    # 8. If classification (choice_fn = mode), return the mode of the K labels
    return k_nearest_distances_and_indices , choice_fn(k_nearest_labels)

# 'mean' calculating the average
def mean(labels):
    return sum(labels) / len(labels)

# 'mode' the 'most value'
def mode(labels):
        # [0], at index 0  [1], at index 1
        # of the value at .most_common(1)
    return Counter(labels).most_common(1)[0][0] 
    
def euclidean_distance(point1, point2):

    # debug
    # len(point1) >> 1
    # range(len(point1)) >> 0

    sum_squared_distance = 0
    for i in range(len(point1)):
        sum_squared_distance += math.pow(point1[i] - point2[i], 2)

    # debug
    print("sum_squared_distance", sum_squared_distance)    
    return math.sqrt(sum_squared_distance)

def main():
    '''
    # Regression Data
    # 
    # Column 0: height (inches)
    # Column 1: weight (pounds)
    '''
    reg_data = [
       [65.75, 112.99], # index 0
       [71.52, 136.49], # index 1
       [69.40, 153.03], # index 2
       [68.22, 142.34], # index 3
       [67.79, 144.30], # index 4
       [68.70, 123.30], # index 5
       [69.80, 141.49], # index 6
       [70.01, 136.46], # index 7
       [67.90, 112.37], # index 8
       [66.49, 127.45], # index 9
    ]
    
    # Question:
    # Given the data we have, what's the best-guess at someone's weight if they are 60 inches tall?
    reg_query = [60]
    reg_k_nearest_neighbors, reg_prediction = knn(
        reg_data, reg_query, k=3, distance_fn=euclidean_distance, choice_fn=mean
    )

    print("\n\n >>")
    print("reg_k_nearest_neighbors", reg_k_nearest_neighbors)
    print("reg_prediction", reg_prediction)
    print(">> \n\n")
    
    '''
    # Classification Data
    # 
    # Column 0: age
    # Column 1: likes pineapple
    #   Column 1, value 0
    #   Column 1, value 1
    '''
    clf_data = [
       [22, 1], # index 0  
       [23, 1], # index 1
       [21, 1], # index 2
       [18, 1], # index 3
       [19, 1], # index 4
       [25, 0], # index 5
       [27, 0], # index 6
       [29, 0], # index 7
       [31, 0], # index 8
       [45, 0], # index 9
    ]
    # Question:
    # Given the data we have, does a 33 year old like pineapples on their pizza?
    clf_query = [33]
    clf_k_nearest_neighbors, clf_prediction = knn(
        clf_data, clf_query, k=3, distance_fn=euclidean_distance, choice_fn=mode
    )

    print("\n\n >>")
    print("clf_k_nearest_neighbors", clf_k_nearest_neighbors)
    print("clf_prediction", clf_prediction)
    print(">> \n\n")

# run the 'main' function
if __name__ == '__main__':
    main()