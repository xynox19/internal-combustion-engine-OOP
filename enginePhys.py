import math

# Constants
R = 8.314  # J/mol·K
ATM = 101325  # Pa
T0 = 300  # K
PISTON_RADIUS = 0.04  # m
STROKE = 0.08  # m
CRANK_RADIUS = STROKE / 2
CONNECTING_ROD = 0.1  # m

class GasMixture:
    def __init__(self, n_moles, temperature=T0, volume=1e-4):
        self.n = n_moles
        self.T = temperature
        self.V = volume
        self.P = self.compute_pressure()

    def compute_pressure(self):
        return (self.n * R * self.T) / self.V

    def compress(self, new_volume):
        self.V = new_volume
        self.T *= (self.V / new_volume) ** (1.4 - 1)  # adiabatic compression
        self.P = self.compute_pressure()

    def ignite(self):
        energy_added = 500  # J, simplified
        delta_T = energy_added / (self.n * 5 * R / 2)
        self.T += delta_T
        self.P = self.compute_pressure()

class Crankshaft:
    def __init__(self):
        self.angle = 0  # degrees

    def rotate(self, delta_angle=5):
        self.angle = (self.angle + delta_angle) % 720
        return self.angle

class Piston:
    def __init__(self):
        self.r = CRANK_RADIUS
        self.l = CONNECTING_ROD
        self.A = math.pi * PISTON_RADIUS ** 2

    def volume(self, angle_deg):
        theta = math.radians(angle_deg)
        x = self.r * (1 - math.cos(theta)) + \
            (self.l - math.sqrt(self.l ** 2 - (self.r * math.sin(theta)) ** 2))
        return self.A * (STROKE - x)

class Cylinder:
    def __init__(self, id):
        self.id = id
        self.gas = GasMixture(n_moles=0.01)
        self.piston = Piston()
        self.crank = Crankshaft()

    def simulate_step(self):
        angle = self.crank.rotate()
        V = self.piston.volume(angle)
        self.gas.compress(V)

        if 355 <= angle <= 365:
            print(f"🔥 Cylinder {self.id}: Igniting at {angle}°")
            self.gas.ignite()

        print(f" {angle}° | P: {self.gas.P:.0f} Pa | T: {self.gas.T:.1f} K | V: {self.gas.V:.6f} m³")

class Engine:
    def __init__(self, cylinders=1):
        self.cylinders = [Cylinder(i + 1) for i in range(cylinders)]

    def run(self, steps=100):
        for _ in range(steps):
            for cyl in self.cylinders:
                cyl.simulate_step()

# Run the enhanced engine
if __name__ == "__main__":
    engine = Engine(cylinders=1)
    engine.run(steps=40)
