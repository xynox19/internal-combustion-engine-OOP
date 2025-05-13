import time
import random

class SparkPlug:
    def ignite(self):
        print("SparkPlug: Igniting air-fuel mixture!")

class Piston:
    def __init__(self):
        self.position = "TDC"  # Top Dead Center or Bottom Dead Center

    def move(self, direction):
        self.position = "BDC" if direction == "down" else "TDC"
        print(f"Piston: Moving {direction} to {self.position}")

class Crankshaft:
    def __init__(self):
        self.rotation_angle = 0

    def rotate(self):
        self.rotation_angle += 180  # Each stroke = 180°
        print(f"Crankshaft: Rotated to {self.rotation_angle} degrees")

class Cylinder:
    def __init__(self, id):
        self.id = id
        self.piston = Piston()
        self.spark_plug = SparkPlug()
        self.crankshaft = Crankshaft()

    def intake(self):
        print(f"Cylinder {self.id}: Intake stroke - Air/fuel mixture enters.")
        self.piston.move("down")
        self.crankshaft.rotate()

    def compression(self):
        print(f"Cylinder {self.id}: Compression stroke - Compressing mixture.")
        self.piston.move("up")
        self.crankshaft.rotate()

    def power(self):
        print(f"Cylinder {self.id}: Power stroke - Combustion begins.")
        self.spark_plug.ignite()
        self.piston.move("down")
        self.crankshaft.rotate()

    def exhaust(self):
        print(f"Cylinder {self.id}: Exhaust stroke - Expelling gases.")
        self.piston.move("up")
        self.crankshaft.rotate()

    def run_cycle(self):
        self.intake()
        self.compression()
        self.power()
        self.exhaust()

class Engine:
    def __init__(self, num_cylinders=4):
        self.cylinders = [Cylinder(i+1) for i in range(num_cylinders)]
        self.running = False

    def start(self):
        print("Engine: Starting...")
        self.running = True
        self.run()

    def stop(self):
        print("Engine: Stopping...")
        self.running = False

    def run(self, cycles=2):
        for cycle in range(cycles):
            if not self.running:
                break
            print(f"\nEngine: Cycle {cycle + 1}")
            for cylinder in self.cylinders:
                cylinder.run_cycle()
                time.sleep(0.5)  # Simulate time delay

# Simulate the engine
if __name__ == "__main__":
    engine = Engine(num_cylinders=2)  # Create a 2-cylinder engine
    engine.start()
