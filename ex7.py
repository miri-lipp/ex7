import csv
from unittest import case

# Global BST root
ownerRoot = None

########################
# 0) Read from CSV -> HOENN_DATA
########################


def read_hoenn_csv(filename):
    """
    Reads 'hoenn_pokedex.csv' and returns a list of dicts:
      [ { "ID": int, "Name": str, "Type": str, "HP": int,
          "Attack": int, "Can Evolve": "TRUE"/"FALSE" },
        ... ]
    """
    data_list = []
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')  # Use comma as the delimiter
        first_row = True
        for row in reader:
            # It's the header row (like ID,Name,Type,HP,Attack,Can Evolve), skip it
            if first_row:
                first_row = False
                continue

            # row => [ID, Name, Type, HP, Attack, Can Evolve]
            if not row or not row[0].strip():
                break  # Empty or invalid row => stop
            d = {
                "ID": int(row[0]),
                "Name": str(row[1]),
                "Type": str(row[2]),
                "HP": int(row[3]),
                "Attack": int(row[4]),
                "Can Evolve": str(row[5]).upper()
            }
            data_list.append(d)
    return data_list


HOENN_DATA = read_hoenn_csv("hoenn_pokedex.csv")

########################
# 1) Helper Functions
########################

def read_int_safe(prompt):
    """
    Prompt the user for an integer, re-prompting on invalid input.
    """
    while True:
        try:
            x = input("Your choice:")
            return int(x)
        except ValueError:
            print("Invalid input.")

def get_poke_dict_by_id(poke_id):
    """
    Return a copy of the Pokemon dict from HOENN_DATA by ID, or None if not found.
    """
    pass

def get_poke_dict_by_name(name):
    """
    Return a copy of the Pokemon dict from HOENN_DATA by name, or None if not found.
    """
    pass

def display_pokemon_list(poke_list):
    """
    Display a list of Pokemon dicts, or a message if empty.
    """
    pass


########################
# 2) BST (By Owner Name)
########################

def new_pokedex():
    global ownerRoot
    name = input("Owner name: ")
    root = find_owner_bst(ownerRoot, name)
    if root is not None:
        print(f"Owner '{name}' already exists. No new Pokedex created.\n")
        return
    print('Choose your starter Pokemon:\n'
        '1) Treecko\n'
        '2) Torchic\n'
        '3) Mudkip\n')
    while True:
        try:
            starter = read_int_safe("Your choice: ")
            if starter < 0 | starter > 3:
                print("Invalid input.")
            else:
                break
        except ValueError:
            print("Invalid input.")
    starter_map = {1:0, 2:3, 3:6}
    starter_index = starter_map[starter]
    if ownerRoot is None:
        ownerRoot = create_owner_node(name, starter_index)
    else:
        new_node = create_owner_node(name, starter_index)
        node = insert_owner_bst(ownerRoot, new_node)
    print('New Pokedex created for ' + name + ' with starter ' + HOENN_DATA[starter_index]['Name'] + "\n")
    pass

def create_owner_node(owner_name, first_pokemon=None):
    """
    Create and return a BST node dict with keys: 'owner', 'pokedex', 'left', 'right'.
    """
    owner_dict = {"owner": owner_name,
                  "pokedex": HOENN_DATA[first_pokemon],
                  "left": None,
                  "right": None}
    return owner_dict

def insert_owner_bst(root, new_node):
    """
    Insert a new BST node by owner_name (alphabetically). Return updated root.
    """
    if not root:
        return new_node
    if new_node["owner"].lower() == root["owner"].lower():
        return root
    elif new_node["owner"].lower() < root["owner"].lower():
        root["left"] = insert_owner_bst(root["left"], new_node)
    else:
        root["right"] = insert_owner_bst(root["right"], new_node)
    return root

def find_owner_bst(root, owner_name):
    """
    Locate a BST node by owner_name. Return that node or None if missing.
    """
    if not root:
        return None
    if root["owner"].lower() == owner_name.lower():
        return root
    elif root["owner"].lower() > owner_name.lower():
        return find_owner_bst(root["left"], owner_name)
    else:
        return find_owner_bst(root["right"], owner_name)

def min_node(node):
    """
    Return the leftmost node in a BST subtree.
    """
    pass

def delete_owner_bst(root, owner_name):
    """
    Remove a node from the BST by owner_name. Return updated root.
    """
    pass


########################
# 3) BST Traversals
########################

def bfs_traversal(root):
    """
    BFS level-order traversal. Print each owner's name and # of pokemons.
    """
    pass

def pre_order(root):
    """
    Pre-order traversal (root -> left -> right). Print data for each node.
    """
    pass

def in_order(root):
    """
    In-order traversal (left -> root -> right). Print data for each node.
    """
    pass

def post_order(root):
    """
    Post-order traversal (left -> right -> root). Print data for each node.
    """
    pass


########################
# 4) Pokedex Operations
########################

def add_pokemon_to_owner(owner_node):
    """
    Prompt user for a Pokemon ID, find the data, and add to this owner's pokedex if not duplicate.
    """
    pass

def release_pokemon_by_name(owner_node):
    """
    Prompt user for a Pokemon name, remove it from this owner's pokedex if found.
    """
    pass

def evolve_pokemon_by_name(owner_node):
    """
    Evolve a Pokemon by name:
    1) Check if it can evolve
    2) Remove old
    3) Insert new
    4) If new is a duplicate, remove it immediately
    """
    pass


########################
# 5) Sorting Owners by # of Pokemon
########################

def gather_all_owners(root, arr):
    """
    Collect all BST nodes into a list (arr).
    """
    pass

def sort_owners_by_num_pokemon():
    """
    Gather owners, sort them by (#pokedex size, then alpha), print results.
    """
    pass


########################
# 6) Print All
########################

def print_all_owners():
    """
    Let user pick BFS, Pre, In, or Post. Print each owner's data/pokedex accordingly.
    """
    pass

def pre_order_print(node):
    """
    Helper to print data in pre-order.
    """
    pass

def in_order_print(node):
    """
    Helper to print data in in-order.
    """
    pass

def post_order_print(node):
    """
    Helper to print data in post-order.
    """
    pass


########################
# 7) The Display Filter Sub-Menu
########################

def display_filter_sub_menu(owner_node):
    """
    1) Only type X
    2) Only evolvable
    3) Only Attack above
    4) Only HP above
    5) Only name starts with
    6) All
    7) Back
    """
    pass


########################
# 8) Sub-menu & Main menu
########################

def existing_pokedex():
    """
    Ask user for an owner name, locate the BST node, then show sub-menu:
    - Add Pokemon
    - Display (Filter)
    - Release
    - Evolve
    - Back
    """
    pass

def main_menu():
    print('1) New Pokedex\n'
          '2) Existing Pokedex\n'
          '3) Delete a Pokedex\n'
          '4) Sort owners\n'
          '5) Print All\n'
          '6) Exit\n')
    """
    Main menu for:
    1) New Pokedex
    2) Existing Pokedex
    3) Delete a Pokedex
    4) Sort owners
    5) Print all
    6) Exit
    """
    pass

def main():
    """
    Entry point: calls main_menu().
    """
    while True:
        main_menu()
        key = read_int_safe("Your choice: ")
        if key == 1:
            new_pokedex()
            continue
        elif key == 6:
            break
    print("Goodbye!\n")
    pass

if __name__ == "__main__":
    main()
