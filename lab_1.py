import random
import csv

class SimpleGraphGenerator:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = {v: [] for v in range(num_vertices)}
    
    def generate_random_graph(self, connectivity=0.5):
        self.adjacency_list = {v: [] for v in range(self.num_vertices)}
        
        max_possible_edges = self.num_vertices * (self.num_vertices - 1) // 2
        
        target_edges = int(max_possible_edges * connectivity)
        
        edges_added = 0
        while edges_added < target_edges:
            v1 = random.randint(0, self.num_vertices - 1)
            v2 = random.randint(0, self.num_vertices - 1)
            
            if v1 != v2 and v2 not in self.adjacency_list[v1]:
                self.adjacency_list[v1].append(v2)
                self.adjacency_list[v2].append(v1)
                edges_added += 1
    
    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
          
            
            for vertex in sorted(self.adjacency_list.keys()):
                writer.writerow([vertex] + sorted(self.adjacency_list[vertex]))
    
    def print_graph(self):
        print(f"Неориентированный невзвешенный граф ({self.num_vertices} вершин):")
        for vertex in sorted(self.adjacency_list.keys()):
            print(f"{vertex}: " + " ".join(map(str, sorted(self.adjacency_list[vertex]))))

def main():
    print("Генератор случайных неориентированных невзвешенных графов")
    print("--------------------------------------------------------")
    
    num_vertices = int(input("Введите количество вершин: "))
    connectivity = float(input("Введите уровень связности (0.0-1.0): "))
    
    generator = SimpleGraphGenerator(num_vertices)
    generator.generate_random_graph(connectivity)

    
    filename = input("\nВведите имя файла для сохранения (без расширения): ") + ".csv"
    generator.save_to_csv(filename)
    print(f"Граф сохранён в файл {filename}")

if __name__ == "__main__":
    main()
echo "# Kartofelnaya-Palochka-Karasika" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Fanatik-Karasik/Kartofelnaya-Palochka-Karasika.git
git push -u origin main
