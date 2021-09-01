from assignment_2.problem import DistanceOfTrip

distance_ABC = DistanceOfTrip('A', 'A', 'A')
distance_AD = DistanceOfTrip('A', 'D')
distance_ADC = DistanceOfTrip('A', 'D', 'C')
distance_AEBCD = DistanceOfTrip('A', 'E', 'B', 'C', 'D')
distance_AED = DistanceOfTrip('A', 'E', 'D')

distance_ABC.print_solution()
distance_AD.print_solution()
distance_ADC.print_solution()
distance_AEBCD.print_solution()
distance_AED.print_solution()
