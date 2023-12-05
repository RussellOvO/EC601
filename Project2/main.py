import googlemaps
import folium
import os

def find_nodes(api_key, lat, lng, r, t):
    # Find specific nodes
    gmaps_client = googlemaps.Client(api_key)
    nodes = gmaps_client.places_nearby(location = (lat, lng), radius = r, type = t)
    return nodes

def node_rank(nodes, weight):
    # Nodes should be a dictionary: {Name: [Distance, Cost, Value]}
    # The number of parameters in weight should equal to the number of dictionary value
    result = ""
    score = 0
    for i in nodes:
        tmp = nodes[i]
        cur = float(tmp[0] * weight[0] + tmp[1] * weight[1] + tmp[2] * weight[2])
        if cur > score:
            score = cur
            result = i
    return result

def main():
    api_key = input("You must include an API key for Google Map Service, please input: ")
    print("Please input your current location:")
    lat0 = float(input("latitude: "))
    lon0 = float(input("longitude: "))
    radius = input("Please input the radius to specify one area:")
    target = input("Please input the type of places you want to visit:")
    target = target.split()
    node_sets = []
    for t in target:
        node_sets.append(find_nodes(api_key, lat0, lon0, radius, t))
    weights = [[1, 0, 0], [0, 1, 0],[0, 0, 1]] # Find shortest, cheapest and best
    testcase1 = {"BBQ": [1.5, 0.5, 4.8], "McDonald": [1.2, 5.0, 3.8], "Restaurant": [5.0, 3.0, 2.0]}
    res = []
    for i in range(3):
        tmp = node_rank(testcase1, weights[i])
        res.append(tmp)
    print(res)
    return res

if __name__ == "__main__": 
    main()