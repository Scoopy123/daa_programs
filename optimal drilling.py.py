import networkx as nx

def get_distance(num_nodes):
  distances = {}
  for i in range (1, num_nodes + 1):
    for j in range (i+1,num_nodes+1):
      distance=float(input(f"Enter the distance between node {i} and node {j}"))
      distances[(i,j)] = distance
      distances[(j,i)] = distance
  return distances

def optimal_drilling(distnaces):
  G = nx.Graph()
  G.add_weighted_edges_from((i,j,distance)for (i,j),distance in distance.items())
  optimal_order = nx.approximation.travelling_salesman_problem(G, cycle=True)
  return optimal_order

def calculate_optimal_cost(drill_order, distances):
  total_cost=sum(distance[(drill_order[i],drill_order[i+1])] for i in range(len(drill_order)-1))
  return total_cost

if __name__=="__main_":
  while True:
    num_nodes = int(input("Enter the number of the drill holes(nodes):"))
    distances = get_distance(num_nodes)

    optimal_order = optimal_drilling(distance)
    optimal_cost= cal_optimal_cost(optimal_order, distance)

    print("Optimal drilling order:",optimal_order)
    print("Total optimal cost:",optimal_cost)

    try_again = input("Do you want to try again with a different number of nodes? (Yes/No)")
    if try_again != "yes":
        break