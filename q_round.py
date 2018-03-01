(R, C, F, N, B, T) = (int(x) for x in input().split()) 
rides = []

class Ride:
    def __init__(self, ride):
        (a, b, x, y, s, f) = (int(x) for x in ride)
        self.a, self.b, self.x, self.y, self.s, self.f = a, b, x, y, s, f
    def __str__(self):
        return f'a: {self.a}, b:{self.b}, x:{self.x}, y:{self.y}, s:{self.s}, f:{self.f}'

for i in range(N):
    rides.append(Ride(input().split()))


rides = sorted(rides, key=lambda r: r.s)

cars = []
for car_index in range(F):
    cars.append([])

car_index = 0
for ride_index in range(N):
    cars[car_index].append(ride_index)
    car_index += 1
    car_index = car_index if car_index < F  else 0

for c in cars:
    print(' '.join((str(x) for x in [len(c)] + c)))
