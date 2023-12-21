class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        
    def __repr__(self):
        return f"User(username={self.username}, name={self.name}, email={self.email})"
    
    def __str__(self) -> str:
        return self.__repr__()
        
john_doe = User("john", "John Doe", "john@doe.com")
jack = User("jack", "Jack Ma", "jack@ma.com")
job = User("job", "Job Null", "job@null.com")
alice = User("alice", "Alice Weng", "alice@weng.com")
ed = User("ed", "Ed Ma", "ed@ma.com")


"""
Naive solution,
Use a list to store users
Make sure the list is sorted by username

we insert elements making sure the list is still sorted
we can return the list of users on find all

insert - O(N)
find - O(N)
update - O(N)
list - O(1)

"""


class UserDatabase:
    def __init__(self) -> None:
        self.users = []
        
    def insert(self, user: User):
        # into an empty database
        # insert user where the username does not exist
        # insert user where username exists
        i = 0
        while i <  len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
        
    def find(self, username):
        # existing user
        # user that does not exist
        for user in self.users:
            if user.username == username:
                return user
        return -1
        
        
    def update(self, user):
        # existing user
        # user that does not exist
        # updating to an existing username
        # updating to an inexisting username
        target_user = self.find(user.username)
        if target_user != -1:
            target_user.name, target_user.email = user.name, user.email 
    def list_all(self):
        # no users
        # one user
        # many users
        return self.users

ed = User("ed", "Edwin", "edwin@ma.com")


database = UserDatabase()
print(database.list_all())
database.insert(john_doe)
print(database.find("john"))
print(database.find("john_skjhgd"))
database.insert(jack)
database.insert(alice)
database.insert(ed)
database.update(ed)
print(database.list_all())



class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.left = self.right = None
        self.parent = None

def remove_none(items):
    return [x for x in items if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    
    is_bst_node = (is_bst_l and is_bst_r and
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r)
                   )
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    
    return is_bst_node, min_key, max_key
    
def insert(node, key, value):
    if node is None:
        node = Node(key=key, value=value)
    elif key < node.key:
        node.left = insert(node=node.left, key=key, value=value)
        node.left.parent = node
    else:
        node.right = insert(node=node.right, key=key, value=value)
        node.right.parent = node
    return node

def find(node, key):
    if node is None:
        return None
    if node.key == key:
        print(node.value)
        return node
    if key < node.key:
        return find(node.left, key)
    else:
        return find(node.right, key)
    
def list_all(node):
    if node is None:
        return []
    return list_all(node=node.left) + [(node.key, node.value)] + list_all(node=node.right)
    
def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.key)
    in_order(node.right)
node = Node(jack.username, jack)
insert(node, john_doe.username, john_doe)
insert(node, job.username, job)
insert(node, alice.username, alice)
insert(node, ed.username, ed)
in_order(node=node)
print("---------------find-----------------")
find(node, "ed")
print("------------------------------------")

print("----------------List all------------")
print(list_all(node=node))
print("------------------------------------")

print("----------is bst-------------")
print(is_bst(node=node))
print("-----------------------------")
# determine if a tree is balanced or not
def is_balanced(node):
    if not node:
        return True, 0
    balanced_l, height_l = is_balanced(node=node.left)
    balanced_r, height_r = is_balanced(node=node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height

print("------------is balanced-------------")
print(is_balanced(node=node))
print("------------------------------------")


def make_balanced_bst(nodes, l = 0, r= None, parent = None):
    if not nodes:
        return []
    if r is None:
        r = len(nodes) - 1
    if l > r:
        return None
    mid = (l + r) // 2
    key, value = nodes[mid]
    root = Node(key=key, value=value)
    root.parent = parent
    root.left = make_balanced_bst(nodes, l, mid - 1, root)
    root.right = make_balanced_bst(nodes, mid + 1, r, root)
    return root

def balance_bst(node):
    # list the nodes in sorted order
    # make balanced binary tree from the sorted array of nodes
    return make_balanced_bst(nodes=list_all(node))

print("--------Balanced bst----------")
balanced_bst = balance_bst(node=node)
print(list_all(balanced_bst))
print(is_balanced(balanced_bst))
print("------------------------------")

def tree_size(node):
    if node is None:
        return 0
    return tree_size(node.left) + 1 + tree_size(node.right)

class TreeMap:
    def __init__(self) -> None:
        self.root = None
        
    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            # balance the bst
            self.root = balance_bst(self.root)
        else:
            print("Node already exists")
    
    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None
    
    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return tree_size(self.root)


print("-------------Treemap---------")
treemap = TreeMap()
treemap["ed"] = ed
treemap["jack"] = jack
treemap["job"] = job
treemap["john_doe"] = john_doe
treemap["alice"] = alice
for key, value in treemap:
    print(key, value)

print(len(treemap))
print(is_balanced(treemap.root))

print(list(treemap))
print("------------------------------")