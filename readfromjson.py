import json

file = open('old-testament.json')

data = json.load(file)


# get chapter number and 
print(data['books'][0]['chapters'][0]['verses'][0]['reference'])
print(data['books'][0]['chapters'][0]['verses'][0]['text'])

# iterate on all chapteres
for i in range(100):
    print(data['books'][0]['chapters'][i]['verses'][0]['reference'])
    print(data['books'][0]['chapters'][i]['verses'][0]['text'])
    print("\n")
