def is_it_safe_to_wait():
    """This function tells if it's best to go to a family doctor or an urgent care clinic."""
    possible_answers = ["yes", "no"]

    print("Please answer Yes or No to each of the following questions:")
    while (q1 := input("Is the person able to drink fluids, eat something light, and sleep normally? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q2 := input("Do you already have, or can you schedule, an appointment with a family doctor within the next 2 days? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q3 := input("Has the pain improved with rest or treatment, or is it rated 6 out of 10 or lower? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")

    if (q1 == "yes" and q2 == "yes") or (q2 == "yes" and q3 == "yes") or (q3 == "yes" and q1 == "yes"):
        print("You can wait and monitor the situation, and contact your family doctor")
    elif q1 == "no" and q2 == "no" and q3 == "no":
        print("It’s best to go to an urgent care clinic")
    elif "yes" in [q1, q2, q3]:
        print("It’s best to go to an urgent care clinic")
    else:
        print("Invalid input, please try again")


def should_see_urgent_care():
    """This function tells if the person should go to urgent care clinic."""
    possible_answers = ["yes", "no"]

    print("Please answer Yes or No to each of the following questions:")
    while (q4 := input("Has the symptom lasted more than 48 hours and still hasn’t improved? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q5 := input("Did you try any home treatment (like rest, medication, fluids), and it did not help at all? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q6 := input("Does the person have a serious health condition like heart disease, uncontrolled diabetes, cancer, or a weak immune system? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q7 := input("Is the pain level currently 7 or higher on a scale from 1 to 10? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")

    if "yes" in [q4, q5, q6, q7]:
        print("You should go to an urgent care clinic")
    elif q4 == "no" and q5 == "no" and q6 == "no" and q7 == "no":
        is_it_safe_to_wait()
    else:
        print("Invalid input, please try again")


def should_go_to_er():
    """This function decides if the person should go to the ER."""
    possible_answers = ["yes", "no"]

    print("Please answer Yes or No to each of the following questions:")
    while (q8 := input("Is the person experiencing a high fever (above 38.5°C / 101.3°F) along with vomiting, chills, confusion, or a rash? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q9 := input("Is the person having a very severe or unusual headache, especially if combined with vomiting or a stiff neck? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q10 := input("Is the person having nonstop vomiting or diarrhea and unable to drink or stay hydrated? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q11 := input("Is there strong stomach or abdominal pain that has lasted more than 6 hours? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q12 := input("Did the person suddenly develop trouble speaking, seeing clearly, or moving one side of their body? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q13 := input("Does the person have a deep cut, a bone sticking out, or a visibly deformed limb? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q14 := input("Is the person feeling extremely hopeless or talking about wanting to hurt themselves? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")

    if "yes" in [q8, q9, q10, q11, q12, q13, q14]:
        print("Go to the nearest emergency room as soon as possible.")
    elif q8 == q9 == q10 == q11 == q12 == q13 == q14 == "no":
        should_see_urgent_care()
    else:
        print("Invalid input, please try again")


def life_threatning_questions():
    """This function decides if the person is experiencing life-threatening situations."""
    possible_answers = ["yes", "no"]

    print("Please answer Yes or No to each of the following questions:")
    while (q15 := input("Is the person having severe difficulty breathing – to the point where they can't speak in full sentences? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q16 := input("Has the person fainted, become unresponsive, or acting extremely confused? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q17 := input("Is the person having strong chest pain (like pressure or burning) that doesn’t go away after 5 minutes? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q18 := input("Is there heavy bleeding that does not stop even with pressure or a bandage? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")
    while (q19 := input("Did the person just have a seizure or convulsions? ").strip().lower()) not in possible_answers: print("Invalid input. Please enter 'yes' or 'no'.")

    if "yes" in [q15, q16, q17, q18, q19]:
        print("Call 911 or emergency services immediately")
    elif q15 == q16 == q17 == q18 == q19 == "no":
        should_go_to_er()


# Start the decision flow
life_threatning_questions()
