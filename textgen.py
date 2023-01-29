import openai

def gen(city, theme, locs):
  openai.api_key = "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"
  location = locs[0]
  for i in range(1,len(locs)):
    location += ' and ' + locs[i]
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"write an airline commercial paragraph about a {theme}-themed trip to {city} in the style of a professional and excited salesman with detailed descriptions of {location} with elaborated descriptions of {city}",
  temperature=0,
  max_tokens=625,
  top_p=1,)
  return str(response['choices'][0]['text'])

def temp():
  openai.api_key = "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"
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"write a paragraph about an awesome ongoing american airlines deal",
  temperature=0.2,
  max_tokens=100,
  top_p=1,)
  return str(response['choices'][0]['text'])

def temp2(city):
  openai.api_key = "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"
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"write a paragraph about some background info of {city}",
  temperature=0.3,
  max_tokens=100,
  top_p=1,)
  return str(response['choices'][0]['text'])
def genloc(city, loc,time):
  openai.api_key = "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"
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"write an descriptive paragraph about the speciality of {loc} in {city} that is around {time} minutes away from the airport",
  temperature=0.7,
  max_tokens=50,
  top_p=1,)
  return str(response['choices'][0]['text'])
def gentitle(theme):
  openai.api_key = "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"
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Generate a title for an airline trip about {theme}",
  max_tokens=13,
  top_p=1)
  return str(response['choices'][0]['text'][1:])