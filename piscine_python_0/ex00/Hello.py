# Exercise 00: First python script

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Modification de la liste
ft_list[1] = "World!"

# Modification du tuple (recréation car immuable / non modifiable)
ft_tuple = (ft_tuple[0], "France!")

# Modification du set (suppression et ajout)
ft_set.discard("tutu!")
ft_set.add("Paris!")

# Modification du dictionnaire
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
