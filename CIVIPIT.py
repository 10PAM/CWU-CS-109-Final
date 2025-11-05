# Author(s): Mario Aguilera; Jakob Greene; Jacky Njoroge;

# Pre-define algorithmic variables
#import math.py
import random

# import numpy?
# import pillow/PIL?

# For symptoms, in each include 1 specific unique symptom to each if possible,
# if not, 1 specific system unique to few to allow for easier determination
# Create list of symptoms
sl = ["Feverish", "Chills", "Cough", "Shortness of Breath", "Sore Throat", "Nasal Congestion", "Runny Nose", "Loss of Taste", "Loss of Smell", "Fatigue", "Body Aches", "Headache", "Nausea", "Vomiting", "Diarrhea", "Dehydration", "Decreased Urination", "Dry Mouth", "Dry Throat", "Dizzy", "Stomach Pain", "Chest Pain", "Confusion"]
common_illnesses = ("Common Cold", "Influenza", "Stomach Flu", "Coronavirus", "Pnuemonia")

# Create a list of the common viral illnesses and tie in symptoms with each
covid_symptoms = [sl[0], sl[1], sl[2], sl[3], sl[4], sl[5], sl[6], sl[7], sl[8], sl[9], sl[10], sl[11], sl[12], sl[13], sl[14]]
common_cold_symptoms = [sl[5], sl[6], sl[2], sl[4], sl[11], sl[10], sl[0]]
influenza_symptomps = [sl[0], sl[4], sl[6], sl[5], sl[11], sl[9], sl[13], sl[14]]
stomach_flu_symptoms = [sl[15], sl[16], sl[17], sl[18], sl[19], sl[13], sl[14], sl[12], sl[20], sl[0], sl[11], sl[10]]
pneumonia_symptoms = [sl[21], sl[22], sl[2], sl[0], sl[1], sl[12], sl[13], sl[14], sl[3]]

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

# Function to screen the user (either real or generated)
def screenUser(user_first="", user_age=0):
    # Get user info
    user_is_generated = True
    user_generated_symptoms = []
    
    if user_first == "":
        user_is_generated = False
        user_first = input("Please enter your first name: ")
        print("Hello", user_first + ", please answer with either 1 (true) or 0 (false) to the following symptoms you may be feeling to determine potential illness(s) that you may have:")
    else:
        #print("Screening generated user:", user_first, "for illnesses...")
        
        # Split the user generated data by splitting into list by delimeter and then removing first element (name, not a symptom)
        user_generated_symptoms += user_first.split(',')
        user_name = user_generated_symptoms.pop(0)
        print("Screening generated user:", user_name, "for illnesses. Their symptoms are:", user_generated_symptoms)
        
        
        
    # print("Hello", user_first + ", please answer with either 1 (true) or 0 (false) to the following symptoms you may be feeling to determine potential illness(s) that you may have:")
    potential_for_covid = 0
    potential_for_common_cold = 0
    potential_for_stomach_flu = 0
    potential_for_influenza = 0
    potential_for_pneumonia = 0
    
    def checkPotentiallity(symptom, illness):
        potentiallity = 0

        # adds two to probaility if symptom is unique to one list/illness only
        unique_symptom = 0
        if symptom in covid_symptoms:
            unique_symptom += 1
        if symptom in common_cold_symptoms:
            unique_symptom += 1
        if symptom in stomach_flu_symptoms:
            unique_symptom += 1
        if symptom in pneumonia_symptoms:
            unique_symptom += 1
        if symptom in influenza_symptomps:
            unique_symptom += 1
        
        # If symptom is unique, add more points
        if symptom in illness:
            if unique_symptom > 1:
                potentiallity = 1
            else:
                potentiallity = 3
        
        return potentiallity
    
    # ToDO: Implement machine learning recognizition algorithms to predict using patterns in user input
    for symptom in sl:
        if (not user_is_generated and checkSymptom(symptom)) or (symptom in user_generated_symptoms):
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

# Generate user function for creating and testing samples
def generateUser():
    
    # Gather a list of symptoms from the chosen generated illness
    def addSymptomsToGeneratedData(illness):
        
        generated_user_data = ""
        symptoms_total = random.randint(5, int(len(illness)))
        #list_shuffled = random.shuffle(illness)
        
        for symptom in range(0, symptoms_total - 1):
            generated_user_data += illness[symptom] + ","
            
        generated_user_data += illness[-1]
            
        return generated_user_data
    
    generated_user_name = random.choice(("John", "Arial", "Marques", "Abel"))
    illness_selected = random.choice(["Covid", "Stomach Flu", "Influenza", "Pneumonia", "Common Cold"])
    generated_user_data = generated_user_name + ","
    
    if illness_selected == "Covid":
        generated_user_data += addSymptomsToGeneratedData(covid_symptoms)
    elif illness_selected == "Stomach Flu":
        generated_user_data += addSymptomsToGeneratedData(stomach_flu_symptoms)
    elif illness_selected == "Influenza":
        generated_user_data += addSymptomsToGeneratedData(influenza_symptomps)
    elif illness_selected == "Pneumonia":
        generated_user_data += addSymptomsToGeneratedData(pneumonia_symptoms)
    elif illness_selected == "Common Cold":
        generated_user_data += addSymptomsToGeneratedData(common_cold_symptoms)
        
    print("Generated User(" + generated_user_name + ") With:", illness_selected, "Illness.")
    
    return generated_user_data

# Generate user(s) and write to a text file to save the samples
def generateUsers(amount_to_generate=1):
    with open("Generated_Samples.txt", "w+") as generated_sample_file:
        for index in range(0, amount_to_generate):
            generated_sample_file.write(generateUser() + "\n")

#generateUsers(8)

screenUser(generateUser())

# generate illness with unique symptoms to a file and generate a random name

# For a presentation, generate 1 data file for 10 generated persons and include the symptoms they all have relating to a generated specific illness
# e.g. Mario: Fever, Chills, etc... but it includes one or more few unique symptoms to determine single illness
