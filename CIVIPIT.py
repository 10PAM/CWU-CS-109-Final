# Author(s): Mario Aguilera; 

# Pre-define algorithmic variables
current_score = 0
# For symptoms, in each include 1 specific unique symptom to each if possible,
# if not, 1 specific system unique to few to allow for easier determination
common_illnesses = ("Common Cold", "Influenza", "Stomach Flu", "Coronavirus", "Pnuemonia")
common_illnesses_symptoms = ["Coughing", "Sweating", ""]

# Import our algo AI algorithm
with open("algo_AI.txt", "a+") as algo_ai:
    
    found_sicknesses = -1
    for line in algo_ai:
        if line.substr(0, 9) == "sicknesses":
            print(line)
            found_sicknesses = line
        
        # Initialize algo_AI
        if(found_sicknesses == -1):
            for illness in common_illnesses:
                print(illness)
                #line.append("sicknesses: " + common_illnesses[illness] + "\n")
