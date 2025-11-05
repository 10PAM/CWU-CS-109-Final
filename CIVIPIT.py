# Author(s): Mario Aguilera; Jakob Greene; Jacky Njoroge;

# Pre-define algorithmic variables
#import math.py
current_score = 0

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

def checkSymptom(illness):
    answer = 0
    
    try:
        answer = int(input(illness + "?: "))
        if answer != 0 and answer != 1:
            print("Please enter either 1 (for true) or 0 (for false).")
            answer = checkSymptom(illness)
    except:
        print("Please enter either 1 (for true) or 0 (for false).!!!")
        checkSymptom(illness)
        
    return bool(answer)

def checkSymptoms(illness):
    print("Please answer either 1 (for true) or 0 (for false) if you feel you have either of these symptomps:")
    for symptom in illness:
        has_symptom = checkSymptom(symptom)
        print("User has " + symptom + "?: " + str(has_symptom))
        
checkSymptoms(covid_symptoms)
