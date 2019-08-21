user_input = {}

user_input['name'] = input("Give me a character name: ").title()
user_input['favorite_teacher'] = input("Name of your favorite teacher: ").title()
user_input['swear_word'] = input("Favorite swear word: ")
user_input['number'] = input("Pick a whole number, any whole number: ")
user_input['plural_object'] = input("What about an object, but make it plural: ").lower()
user_input['store_name'] = input("First store name that comes to mind: ")
user_input['body_part'] = input("How about a body part: ").lower()
user_input['silly_word'] = input("Best silly word ever: ").lower()
user_input['holiday'] = input("Name a holiday: ").title()
user_input['movie_title'] = input("Name a movie title: ").title()
user_input['verb'] = input("Name a verb ending in ING: ").lower()
user_input['distance'] = input("Write a distance: ").lower()
user_input['country'] = input("Country: ").title()
user_input['animal'] = input("Wild animal: ").lower()
user_input['quote'] = input("Pick a famous movie quote (in quotes): ").title()
user_input['body_part2'] = input("How about a different body part: ")
user_input['song'] = input("Name a children's song: ").title()
user_input['adjective'] = input("What is a strong adjective: ").lower()
print(" ")
print(" ")
print(" ")
print("Alright! Thanks for the input!  Now it's time for your very own personalized story!")
print(" ")
print(" ")
print(" ")
print("Detective " + user_input['name'] + ": Hi!  I'm Detective " + user_input['name'] + ".  And you are!?")
print(user_input['favorite_teacher'] + ": " + user_input['favorite_teacher'] + ".")
print("Detective " + user_input['name'] + ": You're here today on the suspicion of second degree robbery.")
print(user_input['favorite_teacher'] + ": " + user_input['swear_word'].capitalize() + "!")
print("Detective " + user_input['name'] + ": That's right! " + user_input['number'] + " " + user_input['plural_object'] + " were stolen from "
      + user_input['store_name'] + ". And the crime scene has your " + user_input['body_part'] + " written all over it!")
print(user_input['favorite_teacher'] + ": That is " + user_input['silly_word'] + "!")
print("Detective " + user_input['name'] + ": Where were you on the night of " + user_input['holiday'] + "?")
print(user_input['favorite_teacher'] + ": I was watching " + user_input['movie_title'] + " on my couch at home.")
print("Detective " + user_input['name'] + ": Then why did the security camera footage show you " + user_input['verb'] + " just "
      + user_input['distance'] + " away from the crime scene!  Alright, alright.  I'm done with playing games.  Where are you from?")
print(user_input['favorite_teacher'] + ": " + user_input['country'] + "")
print("Detective " + user_input['name'] + ": Just as I suspected.  You know, one of the best parts of being a detective"
                                    "is that I get to lock up criminals like you.  Then I go home to my children and ")
print("       my pet " + user_input['animal'] + " and say, " + user_input['quote'] + "!")
print(user_input['favorite_teacher'] + ": Fine! I did it! But I only did it because I needed the money to buy myself "
      + user_input['body_part2'] + " implants.")
print("Detective " + user_input['name'] + ": I knew it all along. And when I solve a crime, I sing my favorite song of "
                                    "all time; " + user_input['song'] + ".")
print(user_input['favorite_teacher'] + ": You have a " + user_input['adjective'] + " voice! I love it! You inspired me to change!")

print(" ")
print(" ")
print(" ")
print("The End")



