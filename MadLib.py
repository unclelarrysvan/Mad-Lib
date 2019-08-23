user_input = {}

user_questions = [
  {
    'name': 'name',
    'question': 'Give me a character name: ',
    'method': 'title'
  },
  {
    'name': 'favorite_teacher',
    'question': 'Name of your favorite teacher: ',
    'method': 'title'
  },
  {
    'name': 'swear_word',
    'question': 'Favorite swear word: ',
    'method': 'capitalize'
  },
  {
    'name': 'number',
    'question': 'Pick a whole number, any whole number: ',
    'method': ''
  },
  {
    'name': 'plural_object',
    'question': 'What about an object, but make it plural: ',
    'method': 'lower'
  },
  {
    'name': 'store_name',
    'question': 'First store name that comes to mind: ',
    'method': ''
  },
  {
    'name': 'body_part',
    'question': 'How about a body part: ',
    'method': 'lower'
  },
  {
    'name': 'silly_word',
    'question': 'Best silly word ever: ',
    'method': 'lower'
  },
  {
    'name': 'holiday',
    'question': 'Name a holiday: ',
    'method': 'title'
  },
  {
    'name': 'movie_title',
    'question': 'Name a movie title: ',
    'method': 'title'
  },
  {
    'name': 'verb',
    'question': 'Name a verb ending in ING: ',
    'method': 'lower'
  },
  {
    'name': 'distance',
    'question': 'Write a distance: ',
    'method': 'lower'
  },
  {
    'name': 'country',
    'question': 'Country: ',
    'method': 'title'
  },
  {
    'name': 'animal',
    'question': 'Wild animal: ',
    'method': 'lower'
  },
  {
    'name': 'quote',
    'question': 'Pick a famous movie quote (in quotes): ',
    'method': 'title'
  },
  {
    'name': 'body_part2',
    'question': 'How about a different body part: ',
    'method': 'lower'
  },
  {
    'name': 'song',
    'question': "Name a children's song: ",
    'method': 'title'
  },
  {
    'name': 'adjective',
    'question': 'What is a strong adjective: ',
    'method': 'lower'
  },
]

def print_gap():
  print(" ")
  print(" ")
  print(" ")

def titlizer(word):
    return word.title()

def capitalizer(word):
    return word.capitalize()

def lowerizer(word):
    return word.lower()

def gather_user_data():
  for question in user_questions:
      switcher = {
        'title': titlizer,
        'capitalize': capitalizer,
        'lower': lowerizer
      }
      result = input(question.get('question'))
      method = switcher.get(question.get('method'))
      return user_input[question.get('name')] = result if method == None

      user_input[question.get('name')] = method(result)

# Start Mad Lib
gather_user_data()
print_gap()
print("Alright! Thanks for the input!  Now it's time for your very own personalized story!")
print_gap()
print(f"Detective {user_input['name']}: Hi!  I'm Detective {user_input['name']}.  And you are!?")
print(f"{user_input['favorite_teacher']}: {user_input['favorite_teacher']}.")
print(f"Detective {user_input['name']}: You're here today on the suspicion of second degree robbery.")
print(f"{user_input['favorite_teacher']}: {user_input['swear_word']}!")
print(f"Detective {user_input['name']}: That's right! {user_input['number']} {user_input['plural_object']} were stolen from {user_input['store_name']}. And the crime scene has your {user_input['body_part']} written all over it!")
print(f"{user_input['favorite_teacher']}: That is {user_input['silly_word']}!")
print(f"Detective {user_input['name']}: Where were you on the night of {user_input['holiday']}?")
print(f"{user_input['favorite_teacher']}: I was watching {user_input['movie_title']} on my couch at home.")
print(f"Detective {user_input['name']}: Then why did the security camera footage show you {user_input['verb']} just {user_input['distance']} away from the crime scene! Alright, alright.  I'm done with playing games.  Where are you from?")
print(f"{user_input['favorite_teacher']}: {user_input['country']}")
print(f"Detective {user_input['name']}: Just as I suspected.  You know, one of the best parts of being a detective is that I get to lock up criminals like you. Then I go home to my children and my pet {user_input['animal']} and say, {user_input['quote']}!")
print(f"{user_input['favorite_teacher']}: Fine! I did it! But I only did it because I needed the money to buy myself {user_input['body_part2']} implants.")
print(f"Detective {user_input['name']}: I knew it all along. And when I solve a crime, I sing my favorite song of all time; {user_input['song']}.")
print(f"{user_input['favorite_teacher']}: You have a {user_input['adjective']} voice! I love it! You inspired me to change!")

print_gap()
print("The End")
