# Author(s): Mario Aguilera
# Date: 11/15/2026
# File: CIVIPIT.py
# About: Program that screens a user for 5 of the most commo viral infections in the US (Per the CDC)

#import libraries for algorithm needs and data visualization
import random
import matplotlib.pyplot as pypl

# Define Program Properties
program_name = "CIVIPIT"

# For symptoms, in each include 1 specific unique symptom to each if possible,
# if not, 1 specific system unique to few to allow for easier determination
# Create list of symptoms
sl = ["Feverish", "Chills", "Cough", "Shortness of Breath", "Sore Throat", "Nasal Congestion", "Runny Nose", "Loss of Taste", "Loss of Smell", "Fatigue", "Body Aches", "Headache", "Nausea", "Vomiting", "Diarrhea", "Dehydration", "Decreased Urination", "Dry Mouth", "Dry Throat", "Dizzy", "Stomach Pain", "Chest Pain", "Confusion", "Sneezing"]
common_illnesses = ("Covid", "Common Cold", "Influenza", "Stomach Flu", "Pnuemonia")

# Create a list of the common viral illnesses and tie in symptoms with each
covid_symptoms = [sl[0], sl[1], sl[2], sl[3], sl[4], sl[5], sl[6], sl[7], sl[8], sl[9], sl[10], sl[11], sl[12], sl[13], sl[14]]
common_cold_symptoms = [sl[0], sl[2], sl[4], sl[5], sl[6], sl[10], sl[11], sl[23]] 
influenza_symptomps = [sl[0], sl[4], sl[5], sl[6], sl[9], sl[11], sl[13], sl[14]]
stomach_flu_symptoms = [sl[0], sl[10], sl[11], sl[12], sl[13], sl[14], sl[15], sl[16], sl[17], sl[18], sl[19], sl[20]]
pneumonia_symptoms = [sl[0], sl[1], sl[2], sl[3], sl[12], sl[13], sl[14], sl[21], sl[22]]
# Import our algo AI algorithm

# Function to check symptoms and return True or False
def checkSymptom(symptom):
    answer = 0
    
    # Use try and expect to help with input error handling for user
    error_message = "Please enter either 1 (for true) or 0 (for false)."
    try:
        answer = int(input(symptom + "?: "))
        if answer != 0 and answer != 1:
            print(error_message)
            answer = checkSymptom(symptom)
    except:
        print(error_message)
        answer = checkSymptom(symptom)
        
    return bool(answer)

# Function to screen the user (either real or generated)
def screenUser(user_first="", user_age=0):
    # Get user info
    user_is_generated = True
    user_generated_symptoms = []
    
    # Pre-intitalize potential for illnesses variables
    potential_for_covid = 0.0
    potential_for_common_cold = 0.0
    potential_for_stomach_flu = 0.0
    potential_for_influenza = 0.0
    potential_for_pneumonia = 0.0
    
    if user_first == "":
        user_is_generated = False
        user_first = input("Please enter your first name: ")
        print("\nHello", user_first + ", please answer with either 1 (true) or 0 (false) to the following symptoms you may be feeling to determine potential illness(s) that you may be experiencing:\n")
    else:
        # Split the user generated data by splitting into list by delimeter and then removing first element (name, not a symptom)
        user_generated_symptoms += user_first.split(',')
        user_first = user_generated_symptoms.pop(0)
        print("Screening generated user:", user_first, "for illnesses. Their symptoms are:", user_generated_symptoms)
    
    def checkPotentiallity(symptom, illness):
        potentiallity = 0
        
        # Subtle Issue: Covid being ahead a lot of the times. Potentially caused by having a lot of similar symptoms as other

        # Determine if symtpom being checked is unqiue to all illnesses, if so, add to unique symptom for more points
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
            
        # If symptom is unique, subtract 0.5 from others
        
        # If symptom is unique, add more points
        if symptom in illness:
            if unique_symptom == 1:
                potentiallity = 3
            else:
                potentiallity = 1
        
        return potentiallity
    
    # Check for Symptom in Symptoms Lists
    for symptom in sl:
        if (not user_is_generated and checkSymptom(symptom)) or (symptom in user_generated_symptoms):
            potential_for_covid += checkPotentiallity(symptom, covid_symptoms)
            potential_for_common_cold += checkPotentiallity(symptom, common_cold_symptoms)
            potential_for_stomach_flu += checkPotentiallity(symptom, stomach_flu_symptoms)
            potential_for_pneumonia += checkPotentiallity(symptom, pneumonia_symptoms)
            potential_for_influenza += checkPotentiallity(symptom, influenza_symptomps)
            
    # Create empty line, then output all potentiallity scores of having a certain illness
    print()
    print("Covid Potential:", potential_for_covid)
    print("Common Cold Potential:", potential_for_common_cold)
    print("Stomach Flu Potential:", potential_for_stomach_flu)
    print("Influenza Potential:", potential_for_influenza)
    print("Pneumonia Potential:", potential_for_pneumonia)
    
    colors = ["red", "green", "blue", "purple", "orange"]
    pypl.bar(["Covid", "Common Cold", "Stomach Flu", "Influenza", "Pneumonia"], [potential_for_covid, potential_for_common_cold, potential_for_stomach_flu, potential_for_influenza, potential_for_pneumonia], color=colors)
    pypl.xlabel("Illness")
    pypl.ylabel("Potentiallity")
    pypl.title("Potentiallity of Illness(es) for " + user_first)
    pypl.show()
    
    # Print white line for spacing/formatting
    print()

# Function to generate a user with a randomly picked name and a range of symptoms from their radnomly selected illness
def generateUser():
    
    # Gather a list of symptoms from the chosen generated illness
    def addSymptomsToGeneratedData(illness):
        
        generated_user_data = ""
        symptoms_total = random.randint(int(len(illness)/2), int(len(illness)))
        #list_shuffled = random.shuffle(illness)
        
        for symptom in range(0, symptoms_total - 1):
            generated_user_data += illness[symptom] + ","
            
        generated_user_data += illness[-1]
            
        return generated_user_data
    
    
    generated_user_name = random.choice(("John", "Arial", "Marques", "Abel", "Mark"))
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

# Load generated data and test each

# Generate user(s) and write to a text file to save the samples
def generateUsers(directory, amount_to_generate=1):
    with open("Generated_Samples.txt", "w+") as generated_sample_file:
        for index in range(0, amount_to_generate):
            generated_sample_file.write(generateUser() + "\n")
            
    # Print a white line for spacing
    print()
    
    return directory

# Screen users that are contained in a dataset file
def screenUsers(dataset):
    try:
        with open(dataset, "r") as userData:
            for user_data_line in userData:
                screenUser(user_data_line)
    except:
        print("Error opening data file!")

# Function to check if program mode is testing or not
def checkMode():
    answer = 0
    
    # Use try and expect to help with input error handling for user
    error_message = "Please enter either 1 (for true) or 0 (for false)."
    try:
        answer = int(input("Would you Like to Run in Testing Mode? \n" + "(0 = False; 1 = True): "))
        if answer != 0 and answer != 1:
            print(error_message)
            answer = checkMode()
    except:
        print(error_message)
        answer = checkMode()
    
    # Return answer as a bool (1 or 0)
    return bool(answer)

# If Testing, Ask User How Many Users To Generate with Viral Illnesses
def amountToGenerate():
    amount = 0
    
    # Use try and expect to help with input error handling for user
    error_message = "Please enter a proper number of users to generate."
    try:
        amount = int(input("Please enter a number of users to generate: "))
        if amount == None:
            print(error_message)
            amount = amountToGenerate()
    except:
        print(error_message)
        amount = amountToGenerate()
        
    return amount

# Method to Begin Program
def startProgram():
    # Describe program
    print("Welcome, Thank You For Trying " + program_name + "! \n")
    
    # Determine if program is in testing mode
    testingMode = checkMode()
    if testingMode:
        # Generate (n) users
        screenUsers(generateUsers("Generated_Samples.txt", amountToGenerate()))
    else:
        screenUser()

# Begin Program
startProgram()
