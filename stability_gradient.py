import random, importlib, sys
import populationshit
import sim

#tweaking species simulation
def tweak_species_info(original_info, population_variation=0.1, rate_variation=0.05):
    """
    Create a tweaked copy of the species info.
    
    Args:
    original_info (dict): The original species information dictionary.
    population_variation (float): Maximum percentage variation for population.
    rate_variation (float): Maximum percentage variation for growth rate.

    Returns:
    dict: A new dictionary with tweaked species information.
    """
    tweaked_info = {}
    for species, attributes in original_info.items():
        # Random factors for population and rate variation
        population_factor = 1 + random.uniform(-population_variation, population_variation)
        rate_factor = 1 + random.uniform(-rate_variation, rate_variation)

        # Tweaking the population and growth rate
        tweaked_population = int(attributes["population"] * population_factor)
        tweaked_rate = attributes["growth_rate"] * rate_factor

        # Ensuring tweaked_rate doesn't exceed 1 or fall below 0
        tweaked_rate = min(max(tweaked_rate, 0), 1)

        # Copying the original attributes and applying tweaks
        tweaked_attributes = attributes.copy()
        tweaked_attributes["population"] = tweaked_population
        tweaked_attributes["growth_rate"] = tweaked_rate

        tweaked_info[species] = tweaked_attributes

    return tweaked_info

# Example usage
original_species_info = {
    # ... (your original species_info data) ...
}

# Get a tweaked version of the species information
tweaked_species_info = tweak_species_info(original_species_info)



#start stability function and gradient descent control function
def evaluate_stability(final_populations, initial_populations):
    """
    Evaluate the stability of populations.

    Args:
    final_populations (dict): Final populations after the simulation.
    initial_populations (dict): Initial populations at the start of the simulation.

    Returns:
    dict: A dictionary indicating the stability status of each species.
    """
    stability = {}
    for species, final_population in final_populations.items():
        initial_population = initial_populations[species]
        if final_population > initial_population * 1.1:  # Greater than 10% increase
            stability[species] = 'rising'
        elif final_population < initial_population * 0.9:  # Less than 10% decrease
            stability[species] = 'falling'
        else:
            stability[species] = 'stable'
    return stability

def gradient_descent_simulation(species_info, relationships, iterations=10, learning_rate=0.01):
    """
    Perform gradient descent to find stable growth rates.

    Args:
    species_info (dict): The species information including growth rates.
    relationships (dict): The predator-prey relationships.
    iterations (int): Number of iterations for gradient descent.
    learning_rate (float): Learning rate for adjusting growth rates.

    Returns:
    dict: Optimized growth rates for stable populations.
    """
    for _ in range(iterations):
        # Run the ecosystem simulation
        ecosystem = populationshit.Ecosystem(species_info, relationships)
        sim.run_simulation(species_info, relationships)
        final_populations = {species: info.population for species, info in ecosystem.species.items()}

        # Evaluate stability
        stability = evaluate_stability(final_populations, {name: info["population"] for name, info in species_info.items()})

        # Adjust growth rates based on stability
        for species, status in stability.items():
            if status == 'rising':
                species_info[species]["growth_rate"] -= learning_rate
            elif status == 'falling':
                species_info[species]["growth_rate"] += learning_rate

            # Ensure growth rate stays within reasonable bounds
            species_info[species]["growth_rate"] = max(min(species_info[species]["growth_rate"], 1), 0)

    return species_info

# # Example usage
optimized_species_info = gradient_descent_simulation(populationshit.species_info, populationshit.relationships, 100, 0.1)
