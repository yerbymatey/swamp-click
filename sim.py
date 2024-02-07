
import pandas as pd
import numpy as np

# Initial populations and growth rates from the user's data
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
    "water_plants": {"population": 400, "growth_rate": 0.09},
    "small_birds" : {"population": 100, "growth_rate": 0.05}
}

# Relationships between predators and prey
relationships = {
    "bobcat": ["rabbits", "rodents"],
    "snapping_turtle": ["fish", "frogs", "water_plants"],
    "river_otter": ["fish"],
    "great_blue_heron": ["fish", "frogs"],
    "raccoon": ["berries", "insects"],
    "water_moccasin": ["fish", "frogs"],
    "red_tailed_hawk": ["rodents", "small_birds"], # Assuming small birds are part of the system
    "eagle": ["red_tailed_hawk", "rabbits"],
    "coyote": ["rabbits", "rodents"],
    "frogs": ["insects"],
    "fish": ["water_plants", "insects"]
}

# Function to run the simulation
def run_simulation(species_info, relationships, time_steps=100):
    # Initialize DataFrame to store population data
    population_data = pd.DataFrame(index=np.arange(time_steps), columns=species_info.keys())

    # Set initial populations
    for species, info in species_info.items():
        population_data.at[0, species] = info['population']

    # Run the simulation over the specified time steps
    for t in range(1, time_steps):
        for species, info in species_info.items():
            current_population = population_data.at[t-1, species]
            growth_rate = info['growth_rate']
            new_population = current_population * (1 + growth_rate)

            # Adjust for predation/carrying capacity if the species is a predator
            if info.get("predator"):
                prey_population = min([population_data.at[t-1, prey] for prey in relationships.get(species, [])])
                new_population = min(new_population, prey_population)  # Limit by prey population

            # Update the population for this time step
            population_data.at[t, species] = new_population

    return population_data

# Run the simulation
simulation_result = run_simulation(species_info, relationships)
simulation_result.head()  # Display the first few rows of the simulation results

print(simulation_result)
print()
print(simulation_result.head)