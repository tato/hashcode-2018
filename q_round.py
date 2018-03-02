import sys
(R, C, F, N, B, T) = (int(x) for x in input().split()) 
rides = []

class Ride:
    def __init__(self, i, ride):
        (a, b, x, y, s, f) = (int(x) for x in ride)
        self.i = i
        self.a, self.b, self.x, self.y, self.s, self.f = a, b, x, y, s, f
    def __str__(self):
        return f'a: {self.a}, b:{self.b}, x:{self.x}, y:{self.y}, s:{self.s}, f:{self.f}'

for i in range(N):
    rides.append(Ride(i, input().split()))

class CarState:
    def __init__(self):
        self.time = 0
        self.x = 0
        self.y = 0
        self.rides = []

cars = []
for car_index in range(F):
    c = CarState()
    cars.append(c)

while len(rides) > 0:
    car = sorted(cars, key=lambda c: c.time)[0]
    
    if car.time > T:
        break
    
    chosen_ride = sorted(rides, key=lambda r: abs(r.a - car.x) + abs(r.b - car.y) + r.s)[0]

    car.time += abs(chosen_ride.x - car.x) + abs(chosen_ride.y - car.y)
    car.x = chosen_ride.x
    car.y = chosen_ride.y

    car.rides.append(chosen_ride.i)
    rides.remove(chosen_ride)


# for car in cars:
#     while car.time < T and len(rides) > 0:
#         sorted_rides = sorted(rides, key=lambda r: abs(r.a - car.x) + abs(r.b - car.y) + r.s)
#         if len(sorted_rides) > 0:
#             chosen_ride = sorted_rides[0]
#             car.time += abs(chosen_ride.x - car.x) + abs(chosen_ride.y - car.y)
#             car.x = chosen_ride.x
#             car.y = chosen_ride.y
# 
#             car.rides.append(chosen_ride.i)
#             rides.remove(chosen_ride)

# rides = sorted(rides, key=lambda r: r.s)
# 
# for ride_index, ride in enumerate(rides):
#     sorted_cars = sorted(cars, key=lambda c: c.time)
#     sorted_rides
#     best_car, best_time = None, 99999999
#     for c in cars[:100]:
#         time_left = ride.f - c.time
#         reach_time = abs(ride.a - c.x) + abs(ride.b - c.y)
#         ride_time = abs(ride.x - ride.a) + abs(ride.y - ride.b)
#         wait_time = ride.s - (reach_time + c.time)
#         if reach_time + ride_time <= time_left:
#             end_time = c.time + reach_time + ride_time + wait_time
#             if end_time < best_time:
#                 best_car = c
#                 best_time = end_time
# 
#     if best_car:
#         best_car.x = ride.x
#         best_car.y = ride.y
#         best_car.time += reach_time + ride_time + wait_time
#         best_car.rides.append(ride_index)

for c in cars:
    print(' '.join((str(x) for x in [len(c.rides)] + c.rides)))
