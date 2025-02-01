class Graph:
    def __init__(self, n, lodging_costs):
        self.n = n
        self.lodging_costs = lodging_costs
        self.adjacency_list = [[] for _ in range(n + 1)]  # Adjacency list for the graph

    def add_edge(self, u, v, a, b):
        # Add bidirectional edges
        self.adjacency_list[u].append((v, a, b))
        self.adjacency_list[v].append((u, a, b))

    def dijkstra(self, start, is_alfur=True):
        import heapq

        costs = {node: float('inf') for node in range(1, self.n + 1)}  # Initialize costs for all nodes
        costs[start] = 0  # Cost to the start node is 0
        visited = set()  # Track visited nodes
        heap = [(0, start)]  # Priority queue: (cost, node)

        while heap:
            current_cost, current_node = heapq.heappop(heap)

            if current_node in visited:
                continue  # Skip if already visited
            visited.add(current_node)

            for neighbor, a, b in self.adjacency_list[current_node]:
                cost = a if is_alfur else b  # Use Álfur's cost or Benedikt's cost
                new_cost = current_cost + cost
                if new_cost < costs[neighbor]:  # Compare with the current cost of the neighbor
                    costs[neighbor] = new_cost  # Update the cost of the neighbor
                    heapq.heappush(heap, (new_cost, neighbor))  # Add to the priority queue

        return costs


# Read input
n, m = map(int, input().split())
lodging = list(map(int, input().split()))
travel_options = []
for _ in range(m):
    u, v, a, b = map(int, input().split())
    travel_options.append((u, v, a, b))

# Create graph
graph = Graph(n, lodging)
for u, v, a, b in travel_options:
    graph.add_edge(u, v, a, b)

# Compute shortest paths
alfur_costs = graph.dijkstra(1, is_alfur=True)  # Álfur's costs from location 1
benedikt_costs = graph.dijkstra(n, is_alfur=False)  # Benedikt's costs from location n

# Calculate the total cost for each location
min_total_cost = float('inf')
best_location = -1

for i in range(1, n + 1):
    total_cost = lodging[i - 1] + alfur_costs[i] + benedikt_costs[i]
    if total_cost < min_total_cost:
        min_total_cost = total_cost
        best_location = i

# Output the result
print(min_total_cost)