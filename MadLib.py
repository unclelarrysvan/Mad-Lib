class Story:
  def __init__(self, questions = [], full_story = ''):
    self.user_input = {}
    self.user_questions = questions
    self.full_story = full_story

  def generate(self):
    self.gather_user_data()
    self.print_story()
    self.print_ending()

  def print_gap(self):
    print(" ")
    print(" ")
    print(" ")

  def print_successful_input_gathering(self):
    self.print_gap()
    print("Alright! Thanks for the input!  Now it's time for your very own personalized story!")
    self.print_gap()

  def print_ending(self):
    self.print_gap()
    print("The End")

  def titlizer(self, word):
      return word.title()
  
  def capitalizer(self, word):
      return word.capitalize()
  
  def lowerizer(self, word):
      return word.lower()
  
  def gather_user_data(self):
    for question in self.user_questions:
      switcher = {
        'title': self.titlizer,
        'capitalize': self.capitalizer,
        'lower': self.lowerizer
      }
      result = input(question.question)
      method = switcher.get(question.method)
      if method == None:
        self.user_input[question.name] = result
      else:
        self.user_input[question.name] = method(result)

    self.print_successful_input_gathering()

  def print_story(self):
      print(self.full_story.format(**self.user_input))

class UserQuestion:
  def __init__(self, name, question, method):
    self.name = name
    self.question = question
    self.method = method

# XXXXXXXXXXXXXXX Story Data XXXXXXXXXXXXXXXXXXXXX
user_questions = [
  UserQuestion('name', 'Give me a character name: ', 'title'),
  UserQuestion('favorite_teacher', 'Name of your favorite teacher: ', 'title'),
  UserQuestion('swear_word', 'Favorite swear word: ', 'capitalize'),
  UserQuestion('number', 'Pick a whole number, any whole number: ', ''),
  UserQuestion('plural_object', 'What about an object, but make it plural: ', 'lower'),
  UserQuestion('store_name', 'First store name that comes to mind: ', 'title'),
  UserQuestion('body_part', 'How about a body part: ', 'lower'),
  UserQuestion('silly_word', 'Best silly word ever: ', 'lower'),
  UserQuestion('holiday', 'Name a holiday: ', 'title'),
  UserQuestion('movie_title', 'Name a movie title: ', 'title'),
  UserQuestion('verb', 'Name a verb ending in ING: ', 'lower'),
  UserQuestion('distance', 'Write a distance: ', 'lower'),
  UserQuestion('country', 'Country: ', 'title'),
  UserQuestion('animal', 'Wild animal: ', 'lower'),
  UserQuestion('quote', 'Pick a famous movie quote (in quotes): ', 'title'),
  UserQuestion('body_part2', 'How about a different body part: ', 'lower'),
  UserQuestion('song', "Name a children's song", 'title'),
  UserQuestion('adjective', 'What is a strong adjective: ', 'lower'),
]

story_string = """Detective {name}: Hi!  I'm Detective {name}.  And you are!?
{favorite_teacher}: {favorite_teacher}.
Detective {name}: You're here today on the suspicion of second degree robbery.
{favorite_teacher}: {swear_word}!
Detective {name}: That's right! {number} {plural_object} were stolen from {store_name}. And the crime scene has your {body_part} written all over it!
{favorite_teacher}: That is {silly_word}!
Detective {name}: Where were you on the night of {holiday}?
{favorite_teacher}: I was watching {movie_title} on my couch at home.
Detective {name}: Then why did the security camera footage show you {verb} just {distance} away from the crime scene! Alright, alright.  I'm done with playing games.  Where are you from?
{favorite_teacher}: {country}
Detective {name}: Just as I suspected.  You know, one of the best parts of being a detective is that I get to lock up criminals like you. Then I go home to my children and my pet {animal} and say, {quote}!
{favorite_teacher}: Fine! I did it! But I only did it because I needed the money to buy myself {body_part2} implants.
Detective {name}: I knew it all along. And when I solve a crime, I sing my favorite song of all time; {song}.
{favorite_teacher}: You have a {adjective} voice! I love it! You inspired me to change!
"""
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# XXXXXXXXXXXXX Test data XXXXXXXXXXXXXXXXXXX
sample_user_questions = [
  UserQuestion('name', 'Give me a character name: ', 'title'),
  UserQuestion('favorite_teacher', 'Name of your favorite teacher: ', 'title'),
  UserQuestion('swear_word', 'Favorite swear word: ', 'capitalize'),
]
sample_user_input = {
  'name': 'steve',
  'favorite_teacher': 'dave',
  'swear_word': 'fuuuuck'
}
sample_story_string = """Detective {name}: Hi!  I'm Detective {name}.  And you are!?
{favorite_teacher}: {favorite_teacher}.
Detective {name}: You're here today on the suspicion of second degree robbery.
{favorite_teacher}: {swear_word}!"""
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# XXXXXXXXXXXXXXXXXX Start Mad Lib XXXXXXXXXXXXXXXXXXXXXXXX
# story = Story(sample_user_questions, sample_story_string)
story = Story(user_questions, story_string)
story.generate()
