import json

# with open('src/test/b.txt', 'r') as fp:
#     content = fp.read()
#     with open('src/test/b.json', 'w') as fa:
#         fa.write(content)

with open('src/test/b.json', 'r') as fc:
    json_obj = json.loads(fc.read())
    path = json_obj['path']
    print(path)
    