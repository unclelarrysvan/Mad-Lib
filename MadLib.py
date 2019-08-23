from story import Story
from question import Question

# XXXXXXXXXXXXXXX Story Data XXXXXXXXXXXXXXXXXXXXX
user_questions = [
  Question('name', 'Give me a character name: ', 'title'),
  Question('favorite_teacher', 'Name of your favorite teacher: ', 'title'),
  Question('swear_word', 'Favorite swear word: ', 'capitalize'),
  Question('number', 'Pick a whole number, any whole number: ', ''),
  Question('plural_object', 'What about an object, but make it plural: ', 'lower'),
  Question('store_name', 'First store name that comes to mind: ', 'title'),
  Question('body_part', 'How about a body part: ', 'lower'),
  Question('silly_word', 'Best silly word ever: ', 'lower'),
  Question('holiday', 'Name a holiday: ', 'title'),
  Question('movie_title', 'Name a movie title: ', 'title'),
  Question('verb', 'Name a verb ending in ING: ', 'lower'),
  Question('distance', 'Write a distance: ', 'lower'),
  Question('country', 'Country: ', 'title'),
  Question('animal', 'Wild animal: ', 'lower'),
  Question('quote', 'Pick a famous movie quote (in quotes): ', 'title'),
  Question('body_part2', 'How about a different body part: ', 'lower'),
  Question('song', "Name a children's song", 'title'),
  Question('adjective', 'What is a strong adjective: ', 'lower'),
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
  Question('name', 'Give me a character name: ', 'title'),
  Question('favorite_teacher', 'Name of your favorite teacher: ', 'title'),
  Question('swear_word', 'Favorite swear word: ', 'capitalize'),
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
