from ib111 import week_10  # noqa


# Napište (čistou) funkci, která dostane na vstupu množinu čísel a
# vrátí délku nejdelšího šestnáctkového kruhu, který se z nich dá
# vytvořit. Pokud se žádný kruh vytvořit nedá, vrátí 0.

# Šestnáctkový kruh je posloupnost čísel (bez opakování) taková, že
# každé další číslo začíná v šestnáctkovém zápisu stejnou cifrou,
# jakou končí číslo předchozí. Navíc první číslo v posloupnosti
# začíná stejnou číslicí, jakou končí poslední číslo.

def first_and_last_digit(number: int) -> tuple[int, int]:
    ld = number % 16
    fd = number
    while fd >= 16:
        fd //= 16
    return fd, ld

def build_graph(numbers: set[int]) -> dict[int, list[int]]:
    graph = {}
    for number in numbers:
        fd, ld = first_and_last_digit(number)
        if ld not in graph:
            graph[ld] = []
        graph[ld].append(fd)
    return graph

def dfs(node: int, graph: dict[int, list[int]], visited: set[int], path: list[int]) -> int:
    if node in visited:
        # Cycle detected, calculate the length of the cycle
        cycle_start_index = path.index(node)
        return len(path) - cycle_start_index
    visited.add(node)
    path.append(node)
    max_length = 0
    for neighbor in graph.get(node, []):
        max_length = max(max_length, dfs(neighbor, graph, visited, path))
    path.pop()
    visited.remove(node)
    return max_length

def hex_circle(numbers: set[int]) -> int:
    if not numbers:
        return 0

    graph = build_graph(numbers)
    print("Graph:", graph)  # Debug print to check graph construction

    max_cycle_length = 0
    for start_node in list(graph.keys()):  # Use list(graph.keys()) to avoid direct dictionary iteration
        max_cycle_length = max(max_cycle_length, dfs(start_node, graph, set(), []))

    return max_cycle_length


def main() -> None:
    assert hex_circle(set()) == 0
    assert hex_circle({0xabc, 0x123}) == 0
    assert hex_circle({0xabcd, 0xdef, 0xfa}) == 3
    assert hex_circle({0xaba}) == 1
    assert hex_circle({0xabc, 0xca, 0xcd, 0xda}) == 3

    hexes = {0xabc, 0xca, 0xacd, 0xda}
    assert hex_circle(hexes) == 4
    assert hexes == {0xabc, 0xca, 0xacd, 0xda}


if __name__ == '__main__':
    main()

