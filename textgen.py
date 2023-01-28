import openai

def gen(city, theme, loc1, loc2, loc3):
  openai.api_key = "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"
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"write an airline commercial paragraph about a {theme}-themed trip to {city} in the style of a professional and excited salesman with detailed descriptions of {loc1} and {loc2} and {loc3} with elaborated descriptions of new york",
  temperature=0,
  max_tokens=625,
  top_p=1,)
  outfile = open(f"generated description.txt", "w")
  outfile.write(str(response['choices'][0]['text']))
  outfile.close
gen('new york','music','Zebulon Cafe','National Sawdust','Pyramid CLub')