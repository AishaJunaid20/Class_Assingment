# product_suggester.py

def suggest_product(user_input):
    user_input = user_input.lower()

    if "headache" in user_input:
        return "I recommend 'Panadol'. It's a pain reliever commonly used for headaches."
    elif "cold" in user_input or "flu" in user_input:
        return "You should try 'Disprin Cold & Flu'. It helps relieve flu symptoms."
    elif "stomach ache" in user_input or "abdominal pain" in user_input:
        return "Try using 'Buscopan'. It's effective for relieving stomach cramps."
    elif "fever" in user_input:
        return "You can take 'Paracetamol'. It reduces fever and body pain."
    elif "allergy" in user_input or "sneezing" in user_input:
        return "'Claritin' is a good option. It helps with sneezing and itching."
    else:
        return "Sorry, I couldn't understand. Please describe your symptoms clearly."
