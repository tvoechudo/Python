class Problem:
    edges_dict = {
        'A': [['B', 5], ['D', 5], ['E', 7]],
        'B': [['C', 4]],
        'C': [['D', 8], ['E', 2]],
        'D': [['C', 8], ['E', 6]],
        'E': [['B', 3]]
    }


class DistanceOfTrip(Problem):
    def __init__(self, *points):
        self.points = [*points]
        self.stops = len(self.points) - 1

        for point in self.points:
            if point not in self.edges_dict:
                raise KeyError('At least one of the points does not exist')

    def solve(self):
        if all(point == self.points[0] for point in self.points):
            return 0
        else:
            distance = 0
            for i in range(self.stops):
                for item in self.edges_dict[self.points[i]]:
                    if item[0] == self.points[i + 1]:
                        distance += item[1]
                        break
                else:
                    return 'NO SUCH ROUTE'
            return distance

    def print_solution(self):
        if type(self.solve()) is int:
            print(f'Distance of {"-".join(self.points)}:', self.solve())
        else:
            print(f'{self.solve()}: {"-".join(self.points)}')


class TripsWithMaxStops(Problem):
    def __init__(self, start, end, max_stops):
        self.start = start
        self.end = end
        self.max_stops = max_stops

        if self.start not in self.edges_dict:
            raise KeyError('The start point does not exist')
        if self.end not in self.edges_dict:
            raise KeyError('The end point does not exist')
        if max_stops < 1:
            raise ValueError('Number of maximum stops cannot be less than 1')

    def find_all_ways(self):
        def find_route_continuation(route_start):
            next_points = []
            for item in route_start:
                for key in self.edges_dict[item[-1]]:
                    next_points.append(key[0])
            possible_ways = []
            for x in range(len(route_start)):
                possible_ways = possible_ways + [route_start[x]] * len(self.edges_dict[route_start[x][-1]])
            for i in range(len(possible_ways)):
                possible_ways[i] = possible_ways[i] + [next_points[i]]
            return possible_ways
        start = [[self.start]]
        next_possible_ways = find_route_continuation(start)
        trips = []  # all possible trips starting at start_point and ending in end_point
        for i in range(self.max_stops):
            for way in next_possible_ways:
                if way[-1] == self.end:
                    trips.append(way)
            next_possible_ways = find_route_continuation(next_possible_ways)
        return trips

    def solve(self):
        trips = self.find_all_ways()
        return len(trips)

    def print_solution(self):
        print(f'The number of trips starting at {self.start} and ending at {self.end} '
              f'with a maximum of {self.max_stops} stops: {self.solve()}')
        print('-----------')
        print('The trips:')
        [print("-".join(trip)) for trip in self.find_all_ways()]


class TripsWithExactStops(TripsWithMaxStops):
    def find_all_ways(self):
        trips = super().find_all_ways()
        filtered_trips = [trip for trip in trips if len(trip) == self.max_stops + 1]
        return filtered_trips

    def solve(self):
        trips = self.find_all_ways()
        return len(trips)

    def print_solution(self):
        print(f'The number of trips starting at {self.start} and ending at {self.end} '
              f'with with exactly {self.max_stops} stops: {self.solve()}')
        print('-----------')
        print('The trips:')
        [print("-".join(trip)) for trip in self.find_all_ways()]
