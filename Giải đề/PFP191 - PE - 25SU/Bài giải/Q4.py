class Suitcase:
    def __init__(self, id: int, name: str, capacity: float, maxWeight: int):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.maxWeight = maxWeight
        
    def expand_suitcase(self) -> float:
        if self.maxWeight >= 15:
            self.capacity += 5
        elif 7 < self.maxWeight < 15:
            self.capacity += 2
        return self.capacity
        
    def toString(self) -> None:
        print(f"{self.id}, {self.name}, {self.capacity:.2f}, {self.maxWeight}")

# ================================
# Example usage (Testing output):
# ================================
if __name__ == '__main__':
    print("--- Test 1 ---")
    s1 = Suitcase(1, "Mia", 6, 6)
    print(f"{s1.expand_suitcase():.2f}")
    
    print("--- Test 2 ---")
    s2 = Suitcase(1, "Mia", 8, 9)
    print(f"{s2.expand_suitcase():.2f}")
    
    print("--- Test 3 ---")
    s3 = Suitcase(1, "Mia", 10, 16)
    print(f"{s3.expand_suitcase():.2f}")
    
    print("--- Test 4 ---")
    s4 = Suitcase(1, "Mia", 10, 16)
    s4.toString()
