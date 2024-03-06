# NESTED  DICTIONARY

DICT = {
    "RB100":{"Name":"rithin","Brand":"BMW","Models":[2001,2024]},
    "RB200":{"Name":"surya","Brand":"mercedies","Models":[2005,2023]},
    "RB300":{"Name":"sreedin","Brand":"plam","Models":[2003,2026]},
    "RB400":{"Name":"amulya","Brand":"fortunar","Models":[2002,2030]}
}

print(f"{'Id':>1} {'Name':>10} {'Brand':>14} {'Models':>18}")
print('-'*60)

for one_product in DICT.keys():
    # for the id in the list
    id = one_product
    # name in the dict
    name = DICT[one_product]['Name']
    # for the brand in the dict
    brand = DICT[one_product]['Brand']
    # for the models in the dict
    models = DICT[one_product]['Models']
    # converting the models list into str using join function
    models_str = ', '.join(str(model) for model in models)
    # and print
    print(f"{id: >5} {name: >10} {brand: >14} {models_str: >18}")