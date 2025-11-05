# Author(s): Mario Aguilera; Jakob Greene; Jacky Njoroge;

# Pre-define algorithmic variables
#import math.py
import random

# For symptoms, in each include 1 specific unique symptom to each if possible,
# if not, 1 specific system unique to few to allow for easier determination
# Create list of symptoms
sl = ["Fever", "Chills", "Cough", "Shortness of Breath", "Sore Throat", "Nasal Congestion", "Runny Norse", "Loss of Taste", "Loss of Smell", "Fatigue", "Body Aches", "Headache", "Nausea", "Vomiting", "Diarrhea", "Runny Nose", "Feverish", "Fatigue", "Dehydration", "Decreased Urination", "Dry Mouth", "Dry Throat", "Dizzy", "Stomach Pain", "Chest Pain", "Confusion"]
common_illnesses = ("Common Cold", "Influenza", "Stomach Flu", "Coronavirus", "Pnuemonia")

# Create a list of the common viral illnesses and tie in symptoms with each
covid_symptoms = [sl[0], sl[1], sl[2], sl[3], sl[4], sl[5], sl[6], sl[7], sl[8], sl[9], sl[10], sl[11], sl[12], sl[13], sl[14]]
common_cold_symptoms = [sl[17], sl[5], sl[2], sl[4], sl[11], sl[10], sl[0]]
influenza_symptomps = [sl[0], sl[4], sl[16], sl[6], sl[5], sl[11], sl[9], sl[13], sl[14]]
stomach_flu_symptoms = [sl[18], sl[19], sl[20], sl[21], sl[22], sl[13], sl[14], sl[12], sl[23], sl[0], sl[11], sl[10]]
pneumonia_symptoms = [sl[24], sl[25], sl[2], sl[0], sl[1], sl[12], sl[13], sl[14], sl[3]]

# Import our algo AI algorithm

# Function to check symptoms and return True or False
def checkSymptom(symptom):
    answer = 0
    # Use try and expect to help with input error handling
    error_message = "Please enter either 1 (for true) or 0 (for false)."
    try:
        answer = int(input(symptom + "?: "))
        if answer != 0 and answer != 1:
            print(error_message)
            answer = checkSymptom(symptom)
    except:
        print(error_message)
        checkSymptom(symptom)
        
    return bool(answer)

def screenUser(user_first="", user_age=0):
    # Get user info
    if user_first == "":
        user_first = input("Please enter your first name: ")
        print("Hello", user_first + ", please answer with either 1 (true) or 0 (false) to the following symptoms you may be feeling to determine potential illness(s) that you may have:")
    else:
        print("Screening generated user:", user_first, "for illnesses...")
    
    # print("Hello", user_first + ", please answer with either 1 (true) or 0 (false) to the following symptoms you may be feeling to determine potential illness(s) that you may have:")
    potential_for_covid = 0
    potential_for_common_cold = 0
    potential_for_stomach_flu = 0
    potential_for_influenza = 0
    potential_for_pneumonia = 0
    
    def checkPotentiallity(symptom, illness):
        potentiallity = 0
        if symptom in illness:
            potentiallity = 1
        return potentiallity
    
    # ToDO: Implement machine learning recognizition algorithms to predict using patterns in user input
    
    for symptom in sl:
        if checkSymptom(symptom):
            potential_for_covid += checkPotentiallity(symptom, covid_symptoms)
            potential_for_common_cold += checkPotentiallity(symptom, common_cold_symptoms)
            potential_for_stomach_flu += checkPotentiallity(symptom, stomach_flu_symptoms)
            potential_for_pneumonia += checkPotentiallity(symptom, pneumonia_symptoms)
            potential_for_influenza += checkPotentiallity(symptom, influenza_symptomps)
    
    print("Covid Potential:", potential_for_covid)
    print("Common Cold Potential:", potential_for_common_cold)
    print("Stomach Flu Potential:", potential_for_stomach_flu)
    print("Influenza Potential:", potential_for_influenza)
    print("Pneumonia Potential:", potential_for_pneumonia)

screenUser()

def generateUser():
    generated_user_name = random.choice(("John", "Arial", "Marques", "Abel"))
    illness_selected = random.choice(["Covid", "Stomach Flu", "Influenza", "Pneumonia", "Common Cold"])
    if illness_selected == "Covid":
        print("Covid")
    elif illness_selected == "Stomach Flu":
        print("Stomach Flu")
    elif illness_selected == "Influenza":
        print("Influenza")
    elif illness_selected == "Pneumonia":
        print("Pneumonia")
    elif illness_selected == "Common Cold":
        print("Common Cold")
    
    return generated_user_name

print(generateUser())

    # generate illness with unique symptoms to a file and generate a random name

# For a presentation, generate 5 seperate data files for a person and include the symptoms they all have relating to a specific illness
# e.g. Mario: Fever, Chills, etc... but it includes one or more few unique symptoms to determine single illness

'''
Old function used to check symptoms on a single illness (Depracated Function On: 11/5/2025 - Mario A.):
def checkSymptoms(illness):
    # Prompt user for 1 to 0 input
    print("Please answer either 1 (for true) or 0 (for false) if you feel you have either of these symptomps:")
    
    # Initialize values
    potentiallity = 0
    
    # Screen symptoms and increase counter if found
    for symptom in illness:
        has_symptom = checkSymptom(symptom)
        potentiallity += int(has_symptom)
        print("User has " + symptom + "?: " + str(has_symptom))
    
    return potentiallity
        
checkSymptoms(covid_symptoms)
'''
