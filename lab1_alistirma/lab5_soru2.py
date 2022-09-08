import re

def lab5_soru2(deneme): #soru2
    for i in deneme:
        deneme = re.sub('(.)([A-Z][a-z0-9]+)', r'\1_\2', i).lower()
        print(deneme)

