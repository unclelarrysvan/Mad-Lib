from question import Question

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
      result = input(question.text)
      method = switcher.get(question.method)
      if method == None:
        self.user_input[question.name] = result
      else:
        self.user_input[question.name] = method(result)

    self.print_successful_input_gathering()

  def print_story(self):
      print(self.full_story.format(**self.user_input))

