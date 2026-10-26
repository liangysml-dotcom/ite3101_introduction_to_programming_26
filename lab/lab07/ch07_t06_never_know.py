def trip_cost(city, days, spending_money = 0):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money