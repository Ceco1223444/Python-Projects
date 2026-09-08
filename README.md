
# Python Algorithms & Data Structures Portfolio

Tsvetelin Simeonov — Data Science & AI, Leiden University

Selected assignments from university coursework in Python, algorithms, and
data structures — recursion, backtracking, dynamic programming, graphs,
object-oriented design, and a small applied-ML piece. Organized by topic below.

Note: A couple of demo
blocks (e.g. `image_processor.py`) reference local test files, such as an
image, that aren't included here.

## Object-Oriented Design (`oop/`)
- **combat_simulator.py** — turn-based Enemy/Player duel simulator using class-level shared state.
- **image_processor.py** — image-processing class (NumPy + Pillow): RGB ↔ indexed-color conversion with color quantization, channel rotation, mean-filter blur, region pixelation, load/save for PNG and pickled indexed images.

## Recursion & Backtracking (`recursion_backtracking/`)
- **maze_pathfinding.py** — recursive DFS route-finding through a maze, with a text-based visualizer.
- **maze_reachability.py** — backtracking reachability check from top-left to bottom-right of a grid maze.
- **unique_value_filler.py** — backtracking fill of missing slots in a list to form a valid set of unique values.
- **n_bit_arrays.py** — generates every binary string of length n.
- **n_queens.py** — N-Queens solver returning all valid board configurations.
- **lock_combination_solver.py** (+ **lock_helper.py**) — exhaustive backtracking solver for a multi-ring combination lock.
- **traveling_salesman.py** — TSP solved by backtracking over a weighted adjacency list, returns the minimal-cost round trip.

## Dynamic Programming (`dynamic_programming/`)
- **knapsack_0_1.py** — 0/1 knapsack, bottom-up with a rolling 1D array.
- **longest_common_subsequence.py** — classic LCS, bottom-up tabulation.
- **edit_distance_top_down.py** — Levenshtein distance, top-down with memoization (`functools.cache`).
- **edit_distance_bottom_up.py** — Levenshtein distance, bottom-up tabulation with NumPy.
- **cut_rod.py** — rod-cutting problem, bottom-up.
- **collatz_longest_sequence.py** — longest Collatz sequence length over a range, bottom-up with reuse of prior results.
- **bus_schedule_shortest_path.py** — minimum-cost path through a sequence of stops, bottom-up.
- **floor_is_lava_probability.py** — probability of reaching a target cell in exactly n random-walk steps while avoiding obstacles, memoized recursion.

## Graphs (`graphs/`)
- **adjacency_list_matrix.py** — vertex/edge counts (directed & undirected), odd-degree counts, adjacency list ↔ matrix conversion, and directed-graph inversion.

## Applied ML (`ml_basics/`)
- **nearest_neighbour_classifier.py** — nearest-neighbour point classifier across grouped 2D data, with a matplotlib visualization.

## Running

Most files are self-contained; a few need NumPy, Pillow, and/or Matplotlib
(see `requirements.txt`):

```
pip install -r requirements.txt
```
