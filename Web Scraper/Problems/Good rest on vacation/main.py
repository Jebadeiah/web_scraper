duration = int(input())
food_per_day = int(input())
flight = 2 * int(input())
hotel_night = int(input())

total_cost = (food_per_day * duration) + flight + (hotel_night * (duration - 1))
print(total_cost)
