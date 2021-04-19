age = int(input())

while True:
    if age <= 16:
        print("Lion King")
    elif 16 < age <= 25:
        print("Trainspotting")
    elif 25 < age <= 40:
        print("Matrix")
    elif 40 < age <= 60:
        print("Pulp Fiction")
    elif 60 < age:
        print("Breakfast at Tiffany's")
    break
