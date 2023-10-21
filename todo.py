import boto3
from utils import *
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")
table_name = "LevelXP_Todo"
table = dynamodb.Table(table_name)

class TodoAPI:

    # initalizing
    def __init__(self) -> None:
        pass

    # routing
    def rounter(self, event):
        # 
        param = event.get("type", "")
        uid = event.get("uid", "")
        id = event.get("id", None)
        task = event.get("task", "")
        done = event.get("done", False)

        if param == "create":
            return todoDB.create(uid, id, task)
        
        elif param == "read":
            return todoDB.read(uid)
        
        elif param == "get":
            return todoDB.get(uid, id)
        
        elif param == "update":
            return todoDB.toogle(uid, id, done)
        
        elif param == "delete":
            return todoDB.delete(uid, id)
        
        return "ERROR.. ERROR.."
        
    # creating
    def create(self, uid, id, task):
        response = table.put_item(Item = {
            "uid":uid, 
            "id": id, 
            "task": task,
            "done": False
        })
        return response.get("ResponseMetadata").get("HTTPStatusCode")
    
    # reading
    def read(self, uid):
        filtering_exp = Key("uid").eq(uid)
        response = table.query(KeyConditionExpression = filtering_exp)
        return response.get("Items", {})
    
    # getitem
    def get(self, uid, id):
        response = table.get_item(
            Key = {'uid': uid, 'id': id},
        )
        return response.get("Item", {})
    
    # updating
    def toogle(self, uid, id, done):    
        update_expression, attribute_values, attribute_names = get_update_params(
            {"done": done}
        )
        response = table.update_item(
            Key = {"uid": uid, "id":id},
            UpdateExpression = update_expression,
            ExpressionAttributeValues = attribute_values,
            ExpressionAttributeNames = attribute_names,
            ReturnValues="UPDATED_NEW"
        )
        return response.get("Attributes", {})
    
    # deleting
    def delete(self, uid, id):
        response = table.delete_item(
            Key = {'uid': uid, 'id': id},
        )
        return response.get("ResponseMetadata").get("HTTPStatusCode")


todoDB = TodoAPI()
