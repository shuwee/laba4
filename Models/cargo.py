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
        return f"{self.weight}"
