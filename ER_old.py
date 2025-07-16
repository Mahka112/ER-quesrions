def main():

    def is_it_safe_to_wait():
    """ this function tells if its best to go to family doctor
    or go to urgent care clinic
    """
    print("Please answer Yes or No to each of the following questions:")
    q1 = input("Is the person able to drink fluids, eat something light, and sleep normally?")
    q2 = input("Do you already have, or can you schedule, an appointment with a family doctor within the next 2 days?")
    q3 = input("Has the pain improved with rest or treatment, or is it rated 6 out of 10 or lower?")
    if (q1 == "yes" and q2 == "yes") or (q2 == "yes" and q3 == "yes") or (q3 == "yes" and q1 == "yes") :
        print("You can wait and monitor the situation, and contact your family doctor") 
    elif q1 == "no" and q2 == "no" and q3 == "no":
        print("It’s best to go to an urgent care clinic")
    elif "yes" in [q1,q2,q3] :
        print("It’s best to go to an urgent care clinic")
    else :
        print("invalid input, please try again")

    def should_see_urgent_care():
    """ this function tells of the person shpuld go to urgent care clinic"""
    print("Please answer Yes or No to each of the following questions:")
    q4 = input("Has the symptom lasted more than 48 hours and still hasn’t improved?")
    q5 = input("Did you try any home treatment (like rest, medication, fluids), and it did not help at all?")
    q6 = input("Does the person have a serious health condition like heart disease, uncontrolled diabetes, cancer, or a weak immune system?")
    q7 = input("Is the pain level currently 7 or higher on a scale from 1 to 10?")
    if "yes" in [q4,q5,q6,q7] :
        print ("You should go to an urgent care clinic ")
    elif q4 == "no" and q5 == "no" and q6 == "no" and q7 == "no":
        is_it_safe_to_wait()
    else :
        print("invalid input, please try again")

    def should_go_to_er():
    """ this function decodesif the person should go to the ER"""
    print("Please answer Yes or No to each of the following questions:")
    q8 = input("Is the person experiencing a high fever (above 38.5°C / 101.3°F) along with vomiting, chills, confusion, or a rash?")
    q9 = input("Is the person having a very severe or unusual headache, especially if combined with vomiting or a stiff neck?")
    q10 = input("Is the person having nonstop vomiting or diarrhea and unable to drink or stay hydrated?")
    q11 = input("Is there strong stomach or abdominal pain that has lasted more than 6 hours?:")
    q12 = input("Did the person suddenly develop trouble speaking, seeing clearly, or moving one side of their body?")
    q13 = input("Does the person have a deep cut, a bone sticking out, or a visibly deformed limb?")
    q14 = input("Is the person feeling extremely hopeless or talking about wanting to hurt themselves?")
    if "yes" in [q8,q9,q10,q11,q12,q13,q14]:
        print ("Go to the nearest emergency room as soon as possible.")
    elif q8 == "no" and q9 == "no" and q10 == "no" and q11 == "no" and q12 == "no" and q13 == "no" and q14 == "no" :
        should_see_urgent_care()
    else :
        print("invalid input, please try again")

    def life_threatning_questions():
    """ this funcions decides if the person expiriences life threatning situations"""
  print("Please answer Yes or No to each of the following questions:")
  q15 = input("Is the person having severe difficulty breathing – to the point where they can't speak in full sentences?")
  q16 = input("Has the person fainted, become unresponsive, or acting extremely confused?")
  q17 = input("Is the person having strong chest pain (like pressure or burning) that doesn’t go away after 5 minutes?")
  q18 = input("Is there heavy bleeding that does not stop even with pressure or a bandage?")
  q19 = input("Did the person just have a seizure or convulsions?")
  if "yes" in [q15,q16,q17,q18,q19] :
      print("Call 911 or emergency services immediately")
  elif q15 == "no" and q16 == "no" and q17 == "no" and q18 == "no" and q19 == "no":
      should_go_to_er()

if __name__ == "__main__":
        main()


  
    