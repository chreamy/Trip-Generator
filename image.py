import requests
import json

def getimage(keyword):
  url =f'https://serpapi.com/search.json?q={keyword.replace(" ","%20")}&tbm=isch&ijn=0&apikey=0620922f9171f8756b3b6adf9e7d228d10a9bd172aadfe7fd9889eba28b337f1'
  response = requests.get(url)
  try:
    imgs = [{'url':i['original'],'width':i['original_width'],'height':i['original_height'],'ratio':i['original_width']/i['original_height']} for i in json.loads(response.text)['images_results'][:10]]
    return imgs
  except:
    print(response.text)

def usebestratio(imgs,ratio):
  min = abs(imgs[0]['ratio']-ratio)
  index = 0
  for i in range(1,len(imgs)):
    if min > abs(imgs[i]['ratio']-ratio):
      min = abs(imgs[i]['ratio']-ratio)
      index = i
  best = imgs[index]['url']
  imgs.pop(index)
  return best,imgs