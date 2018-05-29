import json, io

def main():
    with open("train.json") as json_data:
        data = json.load(json_data)
        #print data
    exception_list = ["brazilian", "cajun_creole", "filipino", "irish", "jamaican", "moroccan", "russian"]
    print len(data)
    for item in exception_list:
        #print recipe["cuisine"]
        for recipe in data:
            if item == recipe["cuisine"]:
                data.remove(recipe)
    print len(data)
    for item in exception_list:
        #print recipe["cuisine"]
        for recipe in data:
            if item == recipe["cuisine"]:
                data.remove(recipe)
    print len(data)
    json_data_ = json.dumps(data,indent=4,sort_keys=True, ensure_ascii=False)
    #print json_data
    f = io.open("train_refined.json", "w", encoding="utf-8")
    f.write(json_data_)
    f.close()

def wordnet():
    import nltk
    nltk.download('wordnet')

if __name__ == '__main__':
    main()
    #wordnet()
