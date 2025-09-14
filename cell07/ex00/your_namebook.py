#!/usr/bin/env python3
def name(person):
    name_list = []
    for k, v in person.items():
        formatted_name = f'{k.capitalize()} {v.capitalize()}'
        name_list.append(formatted_name)
    return name_list
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(name(persons))