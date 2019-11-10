import json


class SaveTextAsJson:
    def __init__(self, textPath, jsonPath, fix=''):
        self.textPath = textPath
        self.jsonPath = jsonPath
        self.fix = fix
    
    def save(self, prefix=False, suffix=False):
        jsonConten = {}

        with open(self.textPath, 'r', encoding='utf-8') as f:
            line = f.readline().strip().split('=', 1)
            while(line and line != '\n'):
                key = line[0]
                if (prefix or suffix):
                    if (prefix):
                        jsonConten[key] = self.fix + line
                    if (suffix):
                        jsonConten[key] = self.fix + line
                else:
                    jsonConten[key] = line[1]
                line = f.readline().strip().split('=', 1)
        
        with open(self.jsonPath, 'w', encoding='utf-8') as f:
            json.dump(jsonConten, f, ensure_ascii=False, sort_keys=True, indent=4)
            print('Saved. ')

def main():
    # route = 'https://girlimg.epio.app'
    textPath = './urls.txt'
    jsonPath = './cfg.json'

    obj = SaveTextAsJson(textPath, jsonPath)
    obj.save()

textPath = './r.txt'
jsonPath = './r.json'

with open(textPath, 'r', encoding='utf-8') as fp:
    jsonContent = json.load(fp)

with open(jsonPath, 'w', encoding='utf-8') as f:
    json.dump(jsonContent, f, ensure_ascii=False, sort_keys=True, indent=4)
    print('Saved. ')


# if __name__ == '__main__':
#     main()