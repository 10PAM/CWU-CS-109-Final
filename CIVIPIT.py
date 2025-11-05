# Author(s): Mario Aguilera; Jakob Greene; Jacky Njoroge;

# Pre-define algorithmic variables
current_score = 0
# For symptoms, in each include 1 specific unique symptom to each if possible,
# if not, 1 specific system unique to few to allow for easier determination
# Create list of symptoms
sl = ["Coughing", "Fever", "Nausea"]
common_illnesses = ("Common Cold", "Influenza", "Stomach Flu", "Coronavirus", "Pnuemonia")

# Create a list of the common viral illnesses and tie in symptoms with each
list_ = {"COVID": [sl[2], sl[1]]}
print(list_["COVID"])

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
