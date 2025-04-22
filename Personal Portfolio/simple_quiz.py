# Avery simple quiz


def quiz_game():
   score = 0  # Track the user's score


   # Question 1
   print("1. What is the average lifespan of a domestic dog?")
   print("A. 5-7 years")
   print("B. 10-13 years")
   print("C. 15-20 years")
   print("D. 20-25 years")
   answer = input("Your answer: ").strip().upper()


   if answer == "B":
       print("Correct!")
       score += 1
   else:
       print("Incorrect.")
       print("1a. What sense is particularly strong in dogs?")
       print("A. Smell")
       print("B. Hearing")
       print("C. Sight")
       print("D. Taste")
       easier_answer = input("Your answer: ").strip().upper()
       if easier_answer == "A":
           print("Correct!")
           score += 1
       else:
           print("Incorrect. The correct answer was A. Smell.")


   # Question 2
   print("2. Which breed is known for its blue-black tongue?")
   print("A. Labrador Retriever")
   print("B. Dalmatian")
   print("C. Chow Chow")
   print("D. Poodle")
   answer = input("Your answer: ").strip().upper()


   if answer == "C":
       print("Correct!")
       score += 1
   else:
       print("Incorrect.")
       print("2a. Which dog breed is known for its exceptional sense of smell?")
       print("A. Beagle")
       print("B. Boxer")
       print("C. Chihuahua")
       print("D. Dachshund")
       easier_answer = input("Your answer: ").strip().upper()
       if easier_answer == "A":
           print("Correct!")
           score += 1
       else:
           print("Incorrect. The correct answer was A. Beagle.")


   # Question 3
   print("3. What is the fastest dog breed?")
   print("A. Greyhound")
   print("B. Bulldog")
   print("C. Border Collie")
   print("D. Golden Retriever")
   answer = input("Your answer: ").strip().upper()


   if answer == "A":
       print("Correct!")
       score += 1
   else:
       print("Incorrect.")
       print("3a. Which dog breed is known for its long ears?")
       print("A. Bulldog")
       print("B. Beagle")
       print("C. Greyhound")
       print("D. Dalmatian")
       easier_answer = input("Your answer: ").strip().upper()
       if easier_answer == "B":
           print("Correct!")
           score += 1
       else:
           print("Incorrect. The correct answer was B. Beagle.")


   # Question 4
   print("4. Which of these is NOT a herding breed?")
   print("A. Australian Shepherd")
   print("B. Border Collie")
   print("C. German Shepherd")
   print("D. Pug")
   answer = input("Your answer: ").strip().upper()


   if answer == "D":
       print("Correct!")
       score += 1
   else:
       print("Incorrect.")
       print("4a. Which breed is known for its tiny size and big personality?")
       print("A. Chihuahua")
       print("B. Great Dane")
       print("C. Pug")
       print("D. Mastiff")
       easier_answer = input("Your answer: ").strip().upper()
       if easier_answer == "A":
           print("Correct!")
           score += 1
       else:
           print("Incorrect. The correct answer was A. Chihuahua.")


   # Question 5
   print("5. How many teeth does an adult dog typically have?")
   print("A. 24")
   print("B. 28")
   print("C. 30")
   print("D. 42")
   answer = input("Your answer: ").strip().upper()


   if answer == "D":
       print("Correct!")
       score += 1
   else:
       print("Incorrect.")
       print("5a. What is the most popular dog breed in the United States?")
       print("A. Poodle")
       print("B. German Shepherd")
       print("C. Labrador Retriever")
       print("D. Beagle")
       easier_answer = input("Your answer: ").strip().upper()
       if easier_answer == "C":
           print("Correct!")
           score += 1
       else:
           print("Incorrect. The correct answer was C. Labrador Retriever.")


   # Display the final score
   print(f"\nYour final score is {score}/5.")
   if score == 5:
       print("Excellent! You really know your dog facts!")
   elif score >= 3:
       print("Good job! You have a solid knowledge of dog facts.")
   else:
       print("Better luck next time. Keep learning about our canine friends!")


# Run the quiz
quiz_game()