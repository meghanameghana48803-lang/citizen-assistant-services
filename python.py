import os
import sys

# ------------------ VOICE FUNCTION ------------------
def speak(text):
    print("\nAssistant:", text)
    if sys.platform.startswith("win"):
        os.system(
            f'powershell -Command "Add-Type –AssemblyName System.Speech; '
            f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
        )

# ------------------ LANGUAGE DATA ------------------
languages = {
    "1": {
        "name": "English",
        "welcome": "Hello, I am Citizen Assistant. How can I help you today?",
    },
    "2": {
        "name": "తెలుగు",
        "welcome": "నమస్కారం, నేను సిటిజన్ అసిస్టెంట్. నేను మీకు ఎలా సహాయం చేయగలను?",
    },
    "3": {
        "name": "हिंदी",
        "welcome": "नमस्ते, मैं सिटीजन असिस्टेंट हूँ। मैं आपकी कैसे मदद कर सकता हूँ?",
    }
}

# ------------------ DOCUMENT DETAILS ------------------
documents = {
    "aadhaar": "Proof of Identity, Proof of Address, Date of Birth proof",
    "pan": "Aadhaar Card, Photo, Signature, Address proof",
    "voter": "Age proof, Address proof, Passport size photo",
    "passport": "Aadhaar, Birth proof, Address proof, Police verification",
}

# ------------------ AP GOVERNMENT SCHEMES ------------------
ap_schemes = {
    "Annadata Sukhibhava": "Aadhaar, Land records, Bank account",
    "Aarogyasri": "Aadhaar, White Ration Card, Income certificate",
    "Auto Driver Seva": "Aadhaar, Driving License, Vehicle RC, Bank account",
    "Andhra Pradesh BPS": "Building approval documents, Aadhaar, Property tax receipt",
    "Crop Insurance": "Aadhaar, Land records, Bank account",
    "Cooperative Loans": "Aadhaar, Society membership, Income certificate",
    "Digi Lakshmi": "Aadhaar, Bank account, Mobile number",
    "DWACRA Women": "Aadhaar, SHG membership, Bank account",
    "Land Lease Income": "Lease agreement, Aadhaar, Bank account",
    "Fee Reimbursement": "Aadhaar, Income certificate, Caste certificate",
    "Free Bus (Stree Shakti)": "Aadhaar, Residence proof",
    "Pravasandira Bheema": "Aadhaar, Employment proof, Nominee details"
}

# ------------------ CENTRAL GOVERNMENT SCHEMES ------------------
central_schemes = {
    "Ayushman Bharat": "Aadhaar, Ration Card",
    "Jal Jeevan Mission": "Aadhaar, Address proof",
    "GST 2.0": "PAN, Aadhaar, Business registration",
    "PMAY-G": "Aadhaar, Income certificate, Land proof",
    "PMAY-U 2.0": "Aadhaar, Income certificate, Address proof",
    "PMEGP": "Aadhaar, PAN, Project report",
    "PMFME": "Aadhaar, Business details, Bank account",
    "PM Internship": "Aadhaar, Education certificates",
    "PM Kisan": "Aadhaar, Land records, Bank account",
    "PMKMY": "Aadhaar, Age proof, Bank account",
    "PMMVY": "Aadhaar, MCP card, Bank account",
    "PM Surya Ghar": "Aadhaar, Electricity bill, Bank account",
    "PM SVANidhi": "Aadhaar, Vendor certificate",
    "PM Vishwakarma": "Aadhaar, Skill proof, Bank account"
}

# ------------------ MAIN ASSISTANT ------------------
def citizen_assistant():
    print("Select Language:")
    print("1. English\n2. Telugu\n3. Hindi")
    lang_choice = input("Enter choice: ")

    lang = languages.get(lang_choice, languages["1"])
    speak(lang["welcome"])

    while True:
        print("\nOptions:")
        print("1. Aadhaar Service")
        print("2. PAN Card Service")
        print("3. Voter ID Service")
        print("4. Passport Service")
        print("5. Andhra Pradesh Government Schemes")
        print("6. Central Government Schemes")
        print("7. Emergency Numbers")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == "1":
            speak(f"Aadhaar services available at uidai.gov.in. Required documents: {documents['aadhaar']}")
        elif choice == "2":
            speak(f"PAN services at incometax.gov.in. Required documents: {documents['pan']}")
        elif choice == "3":
            speak(f"Voter ID services at nvsp.in. Required documents: {documents['voter']}")
        elif choice == "4":
            speak(f"Passport services at passportindia.gov.in. Required documents: {documents['passport']}")
        elif choice == "5":
            speak("Andhra Pradesh Government Schemes and required documents:")
            for scheme, docs in ap_schemes.items():
                print(f"- {scheme}: {docs}")
        elif choice == "6":
            speak("Central Government Schemes and required documents:")
            for scheme, docs in central_schemes.items():
                print(f"- {scheme}: {docs}")
        elif choice == "7":
            speak("Emergency numbers: Police 100, Ambulance 108, Fire 101")
        elif choice == "8":
            speak("Thank you for using Citizen Assistant. Goodbye.")
            break
        else:
            speak("Invalid choice. Please select a valid option.")

# ------------------ RUN ------------------
citizen_assistant()
