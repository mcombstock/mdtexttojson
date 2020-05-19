import json

def read_file():
    
    data = {}
    
    data['name'] = "test"
    data['language'] = "en"
    data['author'] = "jo mama"
    data['calls'] = []
    
    with open("question.txt", "r", encoding='utf-8', errors='ignore') as sources:
            lines = sources.read().splitlines()
            for i in lines:
                question_list = []
                question_list.clear()
                question_list.append(process_question(i))
                
                data['calls'].append(question_list)

    
    data['responses'] = []
    answer_list = []
    
    with open("answers.txt", "r",errors='ignore') as sources:
            lines = sources.read().splitlines()
            for i in lines:
                data['responses'].append(i)
                
    
    with open('data.json5', 'w') as outfile:
        json.dump(data, outfile,indent=2)
    
def process_question(line):
    splut = line.split('___')

    t_line = []
    for e in splut:
        t_line.append(e)
        t_line.append({})
    t_line.pop()
    return t_line

read_file()