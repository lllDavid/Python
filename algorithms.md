# Most Important Algorithms in Python

## 1. Sorting Algorithms

- **Bubble Sort**: A simple comparison-based algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
  - **Time Complexity**: O(n²) in the worst case.
  
- **Selection Sort**: Another comparison-based algorithm, where the smallest element is selected from the unsorted part and swapped with the first unsorted element.
  - **Time Complexity**: O(n²) in all cases.
  
- **Insertion Sort**: Works by repeatedly picking the next element and inserting it into the sorted portion of the list.
  - **Time Complexity**: O(n²) in the worst case, but O(n) in the best case (when the list is already sorted).
  
- **Merge Sort**: A divide-and-conquer algorithm that splits the array in half, recursively sorts each half, and then merges the sorted halves.
  - **Time Complexity**: O(n log n)
  
- **Quick Sort**: Another divide-and-conquer algorithm, but it works by choosing a pivot element and partitioning the list around it. The process is recursively applied to the sublists.
  - **Time Complexity**: O(n log n) on average, but O(n²) in the worst case (can be improved with random pivot selection).

- **Heap Sort**: Uses a binary heap data structure and is based on the idea of constructing a max-heap and repeatedly extracting the maximum element.
  - **Time Complexity**: O(n log n)

- **Tim Sort**: A hybrid sorting algorithm derived from merge sort and insertion sort, used as the default sorting algorithm in Python (`sorted()` function).
  - **Time Complexity**: O(n log n) in the worst case.

## 2. Searching Algorithms

- **Linear Search**: A simple algorithm that checks every element in the list until it finds the target element.
  - **Time Complexity**: O(n)

- **Binary Search**: A much faster searching algorithm for sorted arrays. It works by repeatedly dividing the search interval in half.
  - **Time Complexity**: O(log n)

- **Breadth-First Search (BFS)**: Used in graph or tree traversal. It explores all nodes at the present depth level before moving on to nodes at the next depth level.
  - **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges in the graph.

- **Depth-First Search (DFS)**: Another graph traversal algorithm that explores as far as possible along each branch before backtracking.
  - **Time Complexity**: O(V + E)

## 3. Dynamic Programming

- **Fibonacci Sequence**: A classic example of dynamic programming where each term is the sum of the two preceding ones.
  - **Time Complexity**: O(n), with memoization or bottom-up approach.

- **Knapsack Problem**: Solving the problem of choosing the most valuable items without exceeding the weight limit using DP.
  - **Time Complexity**: O(nW), where n is the number of items and W is the capacity of the knapsack.

- **Longest Common Subsequence (LCS)**: The problem of finding the longest subsequence common to two sequences.
  - **Time Complexity**: O(m * n), where m and n are the lengths of the two sequences.

- **Edit Distance (Levenshtein Distance)**: Measures the difference between two strings by calculating the minimum number of operations required to convert one string into the other.
  - **Time Complexity**: O(m * n), where m and n are the lengths of the two strings.

## 4. Greedy Algorithms

- **Activity Selection Problem**: Given a set of activities with start and finish times, find the maximum number of activities that can be performed without overlapping.
  - **Time Complexity**: O(n log n), typically requires sorting the activities by finish time.
  
- **Huffman Coding**: A compression algorithm used for encoding data based on frequency of characters.
  - **Time Complexity**: O(n log n) for building the tree.

## 5. Graph Algorithms

- **Dijkstra’s Algorithm**: Finds the shortest path from a source node to all other nodes in a graph with non-negative edge weights.
  - **Time Complexity**: O((V + E) log V) with a priority queue.

- **Bellman-Ford Algorithm**: Similar to Dijkstra’s, but it works with negative edge weights and detects negative weight cycles.
  - **Time Complexity**: O(V * E)

- **Floyd-Warshall Algorithm**: Computes the shortest paths between all pairs of vertices in a weighted graph.
  - **Time Complexity**: O(V³)

- **Kruskal’s Algorithm**: An algorithm for finding the minimum spanning tree of a graph (i.e., the set of edges that connect all vertices with the minimum total edge weight).
  - **Time Complexity**: O(E log V)

- **Prim’s Algorithm**: Another algorithm for finding the minimum spanning tree, but it grows the tree one vertex at a time.
  - **Time Complexity**: O((V + E) log V)

## 6. Backtracking Algorithms

- **N-Queens Problem**: Place N queens on an N×N chessboard so that no two queens threaten each other.
  - **Time Complexity**: O(N!)

- **Sudoku Solver**: A typical backtracking problem that involves filling a 9x9 grid while satisfying Sudoku rules.
  - **Time Complexity**: O(9^(n²)) in the worst case.

## 7. Divide and Conquer

- **Merge Sort**: As discussed earlier, this is a divide-and-conquer sorting algorithm.
- **Quick Sort**: Also a divide-and-conquer sorting algorithm.
- **Binary Search**: A divide-and-conquer searching algorithm.

## 8. Mathematical Algorithms

- **Euclidean Algorithm**: Finds the greatest common divisor (GCD) of two numbers.
  - **Time Complexity**: O(log(min(a, b)))

- **Sieve of Eratosthenes**: An efficient algorithm to find all prime numbers up to a given limit.
  - **Time Complexity**: O(n log log n)

- **Fast Exponentiation (Exponentiation by Squaring)**: An algorithm for efficiently calculating large powers of numbers.
  - **Time Complexity**: O(log n)

## 9. String Matching Algorithms

- **Knuth-Morris-Pratt (KMP)**: A linear-time algorithm for finding all occurrences of a substring in a string.
  - **Time Complexity**: O(n + m), where n is the length of the text and m is the length of the pattern.

- **Rabin-Karp**: Uses hashing to search for patterns in a string.
  - **Time Complexity**: O(n + m), but worst case O(n * m).

---