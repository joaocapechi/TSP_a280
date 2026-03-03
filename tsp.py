from random import sample
from math import sqrt, inf

class node():
    def __init__(self, _x: int, _y: int, _ind: int):
        self.x = _x
        self.y = _y
        self.ind = _ind
        self.visited = False
    

    def distance(self, viz: "node"):
        return round(sqrt((self.x - viz.x) ** 2 + (self.y - viz.y) ** 2))
    
    
    def closest_neighbor(self, neighbors: list["node"]):
        best_candidate = neighbors[0]
        best_distance = self.distance(neighbors[0])
        for node in neighbors[1:]:
            tmp = self.distance(node)
            if tmp < best_distance:
                best_distance = tmp
                best_candidate = node
        
        return best_candidate
    
    
    def __str__(self):
        return f"{self.ind} - ({self.x}, {self.y})"
    

    def __repr__(self):
        return self.__str__()

def main():
    with open("a280.tsp", "r") as f:
        lines = [line.strip() for line in f.readlines()[6:-1]]
        nodes = [
            node(int(l.split()[1]), int(l.split()[2]), ind)
            for (ind, l) in enumerate(lines, 1)
        ]
    
    shortest_distance = inf
    desired_path = None
    for _ in range(300):
        dist = 0
        path = [sample(nodes, k=1)[0]]
        copy_nodes = nodes.copy()
        copy_nodes.remove(path[-1])
        
        while copy_nodes:
            tmp = path[-1]
            path.append(tmp.closest_neighbor(copy_nodes))
            dist += tmp.distance(path[-1])
            copy_nodes.remove(path[-1])
        
        if dist < shortest_distance:
            shortest_distance = dist
            desired_path = path.copy()
    
    print(f"{shortest_distance=}")
    for n in desired_path:
        print(f"{n.ind} -> ", end="")

    with open("a280.opt.tour", "r") as f:
        correct_path = [int(line.strip()) - 1 for line in f.readlines()[4:-1]]

    dist = 0
    start: node = nodes[correct_path[0]]
    for ind in correct_path[1:]:
        dist += start.distance(nodes[ind])
        start = nodes[ind]
    
    print(f"\nExpected distance={dist}")
    print(f"Error: {((shortest_distance - dist)/dist) * 100}")

if __name__ == '__main__':
    main()