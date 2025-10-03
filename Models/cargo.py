import math

class Cargo:
    def __init__(self, weight):
        self.weight = weight

    def get_base_price(self):
        if self.weight <= 50:
            return 300
        elif self.weight <= 100:
            return 1000
        elif self.weight <= 300:
            return 2000
        else:
            return 2000 + (self.weight - 300) * 10

    def __str__(self):
        return f"Груз весом {self.weight} кг"


class TransportCalculator:
    def calculate_total_cost(self, weight, floor, has_elevator):
        cargo = Cargo(weight)
        base_cost = cargo.get_base_price()
        
        if has_elevator:
            manual_cost = 0
            weight_units = 0
            floors_to_climb = 0
        else:
            floors_to_climb = max(0, floor - 1)
            weight_units = math.ceil(weight / 100)
            manual_cost = 300 * floors_to_climb * weight_units
        
        total_cost = base_cost + manual_cost
        
        return {
            'base_cost': base_cost,
            'manual_cost': manual_cost,
            'total_cost': total_cost,
            'weight_units': weight_units,
            'floors_to_climb': floors_to_climb
        }