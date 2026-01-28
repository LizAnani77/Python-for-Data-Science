# Exercise 02: First function python


def all_thing_is_obj(object: any) -> int:
    # Fonction qui affiche le type d'un objet et retourne 42
    obj_type = type(object)

    if obj_type == list:
        print(f"List : {obj_type}")
    elif obj_type == tuple:
        print(f"Tuple : {obj_type}")
    elif obj_type == set:
        print(f"Set : {obj_type}")
    elif obj_type == dict:
        print(f"Dict : {obj_type}")
    elif obj_type == str:
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not found")

    return 42
