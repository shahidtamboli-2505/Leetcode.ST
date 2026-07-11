from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):

        if source == target:
            return 0

        # stop -> buses
        stop_to_bus = defaultdict(list)

        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_bus[stop].append(bus)

        q = deque([source])

        visited_stops = set([source])
        visited_buses = set()

        buses = 0

        while q:

            buses += 1

            for _ in range(len(q)):

                stop = q.popleft()

                for bus in stop_to_bus[stop]:

                    if bus in visited_buses:
                        continue

                    visited_buses.add(bus)

                    for next_stop in routes[bus]:

                        if next_stop == target:
                            return buses

                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            q.append(next_stop)

        return -1