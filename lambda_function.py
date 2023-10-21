from todo import todoDB
import json

def lambda_handler(event, context):
    response = todoDB.rounter(event)
    return response

if __name__ == "__main__":
    test_event = {
        "type":"get", 
        "uid":"123456789", 
        "id":3, 
        "task":"new task asd kola",
        "done":False
    }
    result = lambda_handler(test_event, None)
    print(result)
