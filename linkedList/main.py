import json

# Handling Json
def read_json(file: str = 'data.json') -> dict:
    with open(file, 'r') as read:
        data = json.load(read)
    return data

def commit_json(data: dict) -> None:
    with open('data.json', 'w') as write:
        json.dump(data, write, indent = 4)

# Linked List
class LinkedList:
    def __init__(self):
        self.data = read_json()

    def get_list(self) -> list: return self.data['data']

    def get_ptr(self) -> int: return self.data['ptr']

    def get_string(self) -> str:
        arr, curr = [], self.get_ptr()
        while curr is not None:
            arr.append(self.get_list()[curr]['data'])
            curr = self.get_list()[curr]['next']
        return " | ".join([str(i) for i in arr])

    def insert_at_beginning(self, data) -> None:
        new_node = {"data": data, "next": self.get_ptr()}
        self.get_list().append(new_node)
        self.data['ptr'] = len(self.get_list()) - 1
        commit_json(self.data)

    def insert_at_end(self, data) -> None:
        if self.get_ptr() is None:
            self.insert_at_beginning(data)
        else:
            new_node = {"data": data, "next": None}
            curr = self.get_ptr()
            while self.get_list()[curr]['next'] is not None:
                curr = self.get_list()[curr]['next']
            self.get_list()[curr]['next'] = len(self.get_list())
            self.get_list().append(new_node)
            commit_json(self.data)
        
    def insert_after_value(self, data, key) -> None:
        curr = self.get_ptr()
        while curr is not None:
            if self.get_list()[curr]['data'] == key: break
            curr = self.get_list()[curr]['next']
        if curr is None: raise ValueError(f"Key {key} not found in the list")

        new_node = {"data": data, "next": self.get_list()[curr]['next']}
        self.get_list()[curr]['next'] = len(self.get_list())
        self.get_list().append(new_node)
        commit_json(self.data)
    
    def insert_at_index(self, index: int, data) -> None:
        if index < 0: raise ValueError("Index cannot be negative")
        if index == 0: 
            self.insert_at_beginning(data)
            return
        curr = self.get_ptr()
        length = 0
        while curr is not None:
            if length == index - 1:
                break
            curr = self.get_list()[curr]['next']
            length += 1
        if curr is None:
            self.insert_at_end(data)
        else:
            new_node = {"data": data, "next": self.get_list()[curr]['next']}
            self.get_list()[curr]['next'] = len(self.get_list())
            self.get_list().append(new_node)
            commit_json(self.data)

# Sample Driver Code
if __name__ == '__main__':
    llist = LinkedList()

    llist.insert_at_beginning("Inserted At Start")
    print(llist.get_string())
    llist.insert_at_end("Inserted At End")
    print(llist.get_string())
    llist.insert_after_value('Inserted After Second', 'Second')
    print(llist.get_string())
    llist.insert_at_index(3, "Inserted at Index: 3")
    print(llist.get_string())