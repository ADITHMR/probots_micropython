import json


def set_parameter(parameter,value):
    with open('config.txt', 'r') as f: 
        data = json.load(f)
        if parameter in data:
            try:
                data[parameter]=str(value)
            except :
                return "Data format error"
            with open('config.txt', 'w') as f:
                json.dump(data, f)
            read_data=get_parameter(parameter)
#                 return(f"-{type(read_data)}-{type(value)}")
            if read_data== str(value):
                return "OK"
            else:
                return "Error Saving Data"
        else: return f"Error 404: No parameter named {parameter}"
def get_parameter(parameter):
        with open('config.txt', 'r') as f:
            data= json.load(f)
            if parameter in data:
                result= data[parameter].replace("'","")
                return  (result)
                
            else:
                return "Error 404: No Such Parameter Found"



