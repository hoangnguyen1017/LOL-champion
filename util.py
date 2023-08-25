# Objectives of champion_outcome function
# 1. Calculate the effective damage one champion would deal to another.
# 2. Compute the number of hits required for one champion to defeat another.
# 3. Determine the winner of each battle by comparing the number of hits each champion requires to defeat the other.
# 4. Return a list of battle outcomes.

# Create a function name champion_outcome
# function champion_outcome will take the dataframe as an parameter
# in function champion_outcome we will compute the champion outcome as follow
# Compute the effective damage by champ1 to champ2 considering attack_power, defense_power, and attack_speed.
# Calculate the number of hits required by champ1 to defeat champ2 using the effective damage and health of champ2.
# We'll use the formula:
# Effective Damage = (champ1.attack_power * 2 - champ2.defense_power * 3) * champ1.attack_speed
# Hits Required = champ2.health / Effective damge
# If Hits Required for champ1 is less than that for champ2, then champ1 is the winner.

# Pseudocode 
# Function champion_outcome (Input: List of Champions with their stats)
    
#     Initialize an empty list called "battle_results"

#     For each "champion1" in the list of Champions:
#         For each "champion2" in the list of Champions:
            
#             If champion1 is not equal to champion2:
                
#                 // Calculate the effective damage of champion1 against champion2
#                 effective_damage_champ1 = (champion1's attack_power * 2 - champion2's defense_power * 3) * champion1's attack_speed
                
#                 // Calculate the number of hits champion1 needs to defeat champion2
#                 hits_required_champ1 = champion2's health divided by effective_damage_champ1

#                 // Calculate the effective damage of champion2 against champion1
#                 effective_damage_champ2 = (champion2's attack_power * 2 - champion1's defense_power * 3) * champion2's attack_speed
                
#                 // Calculate the number of hits champion2 needs to defeat champion1
#                 hits_required_champ2 = champion1's health divided by effective_damage_champ2
                
#                 // Determine the outcome based on who needs fewer hits
#                 If hits_required_champ1 is less than hits_required_champ2:
#                     champion1 is the winner
#                     Append (champion1's name, champion2's name, and the result) to "battle_results"
#                 Else:
#                     champion2 is the winner
#                     Append (champion1's name, champion2's name, and the result) to "battle_results"
    
#     Return "battle_results"
