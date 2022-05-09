# tao mot ham tra ve gia tri cua 'year'

def myFunc (e):
    return e['year']

cars=[
        {'car': 'Ford', 'year': 2005},
        {'car': 'Mitsubishi', 'year': 2000},
        {'car': 'BMW', 'year': 2019},
        {'car': 'VW', 'year': 2011}
      ]
# sap xep tu dien theo thu tu tang dan cua nam
cars.sort(key=myFunc)
print(cars)
