import json

    
file_name = "Save.json"
save = []
        
def write_data(data):
    save.append(data)         
        
def remove_data(data):
    save.remove(data)
        
def save_data():
    with open(file_name, 'w') as file:
        json.dump(save, file, indent=4)
    
def wipe_save():
    save.clear()
    save_data()
