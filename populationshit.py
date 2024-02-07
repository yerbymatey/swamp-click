species_info = {
    "bobcat": {"population": 30, "growth_rate": 0.04, "predator": True},
    "snapping_turtle": {"population": 50, "growth_rate": 0.03, "predator": True},
    "river_otter": {"population": 40, "growth_rate": 0.035, "predator": True},
    "great_blue_heron": {"population": 35, "growth_rate": 0.03, "predator": True},
    "raccoon": {"population": 70, "growth_rate": 0.025, "predator": True},
    "water_moccasin": {"population": 45, "growth_rate": 0.04, "predator": True},
    "red_tailed_hawk": {"population": 25, "growth_rate": 0.03, "predator": True},
    "eagle": {"population": 20, "growth_rate": 0.02, "predator": True},
    "coyote": {"population": 30, "growth_rate": 0.03, "predator": True},
    "rabbits": {"population": 150, "growth_rate": 0.1},
    "rodents": {"population": 200, "growth_rate": 0.12},
    "fish": {"population": 300, "growth_rate": 0.08},
    "frogs": {"population": 250, "growth_rate": 0.07},
    "insects": {"population": 500, "growth_rate": 0.15},
    "grass": {"population": 1000, "growth_rate": 0.2},
    "berries": {"population": 500, "growth_rate": 0.1},
    "water_plants": {"population": 400, "growth_rate": 0.09}
}

relationships = {
    "bobcat": ["rabbits", "rodents"],
    "snapping_turtle": ["fish", "frogs"],
    "river_otter": ["fish"],
    "great_blue_heron": ["fish", "frogs"],
    "raccoon": ["berries", "insects"],
    "water_moccasin": ["fish", "frogs"],
    "red_tailed_hawk": ["rodents", "small_birds"],
    "eagle": ["red_tailed_hawk", "rabbits"],
    "coyote": ["rabbits", "rodents"]
}

class Species:
    def __init__(self, name, population, growth_rate, is_predator=False):
        self.name = name
        self.population = population
        self.growth_rate = growth_rate
        self.is_predator = is_predator

    def logistic_growth(self, carrying_capacity):
        growth = self.growth_rate * self.population * (carrying_capacity - self.population) / carrying_capacity
        self.population += growth
        if self.population < 0:
            self.population = 0  # Ensure population doesn't go negative

class Ecosystem:
    def __init__(self, species_info, relationships):
        # Initialize species and relationships
        self.species = {name: Species(name, info["population"], info["growth_rate"], "predator" in info)
                        for name, info in species_info.items()}
        self.relationships = relationships

    def update_ecosystem(self):
        for species_name, species in self.species.items():
            if species.is_predator:
                # For predators, carrying capacity is based on prey availability
                total_prey_population = sum(self.species[prey].population for prey in self.relationships[species_name])
                species.logistic_growth(total_prey_population)
            else:
                # For non-predators, use a constant or environmentally defined carrying capacity
                constant_carrying_capacity = 1000  # Example value
                species.logistic_growth(constant_carrying_capacity)

    # ... other methods ...

# Example usage
# Define species_info and relationships as before
# ecosystem = Ecosystem(species_info, relationships)
# Run the simulation and plot results
