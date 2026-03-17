class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.type_label = "plant"

    def grow(self):
        growth_value = 1
        self.height += growth_value
        print(f"{self.name} grew {growth_value}cm")

    def get_info(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = True
        self.type_label = "flowering"

    def get_info(self):
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return (f"""{self.name}: {self.height}cm, """
                f"""{self.flower_color} flowers ({bloom_status})""")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, prize_points):
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points
        self.type_label = "prize flower"

    def get_info(self):
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return (f"{self.name}: {self.height}cm, {self.flower_color} flowers"
                f" ({bloom_status}), Prize points: {self.prize_points}")


class GardenManager:
    total_gardens = 0

    def __init__(self, owner_name: str):
        self.owner = owner_name
        self.plants = []
        self.total_growth_recorded = 0
        GardenManager.total_gardens += 1

    class GardenStats:
        @staticmethod
        def calculate_delta(old, new):
            return new - old

        @staticmethod
        def sum_scores(plant_list):
            score = 0
            for i in range(len(plant_list)):
                p = plant_list[i]
                score += p.height
                if p.type_label == "prize flowers":
                    score += p.points
            return score

    def add_plant(self, plant_obj):
        self.plants.append(plant_obj)
        print(f"Added {plant_obj.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"\n{self.owner} is helping all plants grow...")
        for i in range(len(self.plants)):
            current_plant = self.plants[i]
            old_height = current_plant.height
            current_plant.grow()
            diff = self.GardenStats.calculate_delta(
                old_height, current_plant.height)
            self.total_growth_recorded += diff
            # print(f"{current_plant.name} grew {diff}cm")

    def display_report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")

        print("Plants in garden:")
        counts = {"plant": 0, "flowering": 0, "prize flower": 0}
        for i in range(len(self.plants)):
            current_plant = self.plants[i]
            counts[current_plant.type_label] += 1
            print(f"- {current_plant.get_info()}")

        print(
            f"\nPlants added: {len(self.plants)}, Total growth: {self.total_growth_recorded}cm")
        print(
            f"Plant types: {counts['plant']} regular, {counts['flowering']} flowering, {counts['prize flower']} prize flowers")

    @classmethod
    def get_total_garden_count(cls) -> int:
        return cls.total_gardens

    @classmethod
    def create_garden_network(cls, names):
        return [cls(name) for name in names]

    @staticmethod
    def validate_height(h) -> bool:
        return h > 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    network = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = network[0]
    bob = network[1]

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    alice.grow_all()
    alice.display_report()

    is_valid = GardenManager.validate_height(alice.plants[0].height)
    print(f"\nHeight validation test: {is_valid}")

    alice_score = GardenManager.GardenStats.sum_scores(alice.plants)
    bob.add_plant(Plant("Mango", 92))
    bob_score = GardenManager.GardenStats.sum_scores(bob.plants)

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.get_total_garden_count()}")
