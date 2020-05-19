import json

def read_file():
    
    data = {}
    
    data['name'] = "test"
    data['language'] = "en"
    data['author'] = "jo mama"
    question_list = []
    t_as = []
    data['calls'] = []
    with open("question.txt", "r") as sources:
            lines = sources.read().splitlines()
            for i in lines:
                question_list.clear()
                question_list.append(process_question(i))
                
                data['calls'].append(question_list)
                
    answer_list = []
    data['responses'] = []
    with open("answers.txt", "r") as sources:
            lines = sources.read().splitlines()
            for i in lines:
                data['responses'].append(process_answer(i))
                
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

def process_answer(line):
    a_line = []
    a_line.append(line)
    
    return line

read_file()