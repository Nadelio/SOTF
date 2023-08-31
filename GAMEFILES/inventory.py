import save_manager

class Inventory:
    def __init__(self):
        self.items = []
        
    
    def add_item(self, item, amount=1):
        for i in range(amount):
            save_manager.write_data(item)
            self.items.append(item)
        save_manager.save_data()
        
    def clear(self):
        self.items.clear()
        save_manager.wipe_save()
        
    def remove_item(self, item, amount=1):
        for i in range(amount):
            if (self.contains_item(item)):
                save_manager.remove_data(item)
                self.items.remove(item)
        save_manager.save_data()
    
    def is_empty(self):
        return self.items == []
    
    def contains_item(self, item, amount=1):
        flag = 0
        for i in range(amount):
            if item in self.items:
                flag += 1
        return flag == amount