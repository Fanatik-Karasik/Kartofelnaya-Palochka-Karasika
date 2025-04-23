import csv
from collections import defaultdict, deque

def read_graph_from_csv(filename):
    graph = defaultdict(list)
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row: 
                vertex = int(row[0])
                neighbors = list(map(int, row[1:]))
                graph[vertex] = neighbors
    return graph

def find_connected_components(graph):
    visited = set()
    components = []
    
    for vertex in graph:
        if vertex not in visited:
            queue = deque([vertex])
            visited.add(vertex)
            component = []
            
            while queue:
                current = queue.popleft()
                component.append(current)
                
                for neighbor in graph.get(current, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            components.append(component)
    
    return components

def find_largest_component(graph):
    components = find_connected_components(graph)
    if not components:
        return {}
    
    largest_component = max(components, key=len)
    subgraph = {vertex: graph[vertex] for vertex in largest_component}
    return subgraph

def write_graph_to_csv(graph, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for vertex in sorted(graph.keys()):
            writer.writerow([vertex] + graph[vertex])

def main():
    input_filename = input("Введите имя входного CSV-файла: ")
    output_filename = input("Введите имя выходного CSV-файла: ")
    
    try:
        graph = read_graph_from_csv(input_filename)
        largest_component = find_largest_component(graph)
        write_graph_to_csv(largest_component, output_filename)
        print(f"Максимальная связная компонента записана в файл {output_filename}")
    except FileNotFoundError:
        print("Ошибка: входной файл не найден")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()
