def TSP(adj_list):
    # енфакториел
    """
    Implement an algorithm that solves the Travelling Salesman Problem using backtracking. 
    
    :param adj_list: An adjacency list of a weighted fully connected, undirected graph, 
    with nodes from 0 to n. 
    :type adj_list: dict(dict(int))
 
    :return: A tuple (path, cost), where path is a list with the path of 
    minimal weight, starting and ending at node 0
    :rtype: tuple(list, int)
    """
    n = len(adj_list)
    
    # 1. Защита за тест с един единствен град (test_single_node)
    if n == 1:
        # Пътят е от 0 до 0, а цената е 0
        return ([0], 0)
    visited = [0]
    # best_res[0] е пътят, best_res[1] е цената
    best_res = [None, float("inf")]
    def backtrack(node, current_cost):
        # 2. Базов случай: Посетили сме всички градове
        if len(visited) == n:
            # Проверяваме дали можем да се върнем в град 0
            if 0 in adj_list[node]:
                return_price = adj_list[node][0]
                total_cost = current_cost + return_price
                
                # Ако намерим по-добър път, го записваме
                if total_cost < best_res[1]:
                    best_res[0] = visited + [0]
                    best_res[1] = total_cost
            return
        # 3. Обхождане на съседите (Твоята стратегия)
        for neighbour in adj_list[node]:
            if neighbour not in visited:
                # Маркираме като посетен
                visited.append(neighbour)
                
                # Взимаме цената до съседа
                price = adj_list[node][neighbour]
                
                # Рекурсия - продължаваме напред
                backtrack(neighbour, current_cost + price)
                
                # ВАЖНО: Backtrack (изчистваме след себе си)
                visited.pop()
    # Стартираме от град 0 с начална цена 0
    backtrack(0, 0)
    
    # Връщаме резултата като кортеж (път, цена)
    return tuple(best_res)
