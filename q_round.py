(R, C, F, N, B, T) = (int(x) for x in input().split()) 
rides = []

class Ride:
    def __init__(self, ride):
        (a, b, x, y, s, f) = (int(x) for x in ride)
        self.a, self.b, self.x, self.y, self.s, self.f = a, b, x, y, s, f

for i in range(N):
    rides.append(Ride(input().split()))


rides = sorted(rides, key=lambda r: r.s)
print(rides)
