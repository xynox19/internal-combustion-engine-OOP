
# 🛠 Internal Combustion Engine Simulation (Python, OOP)

This project simulates the operation of an internal combustion engine using **Object-Oriented Programming (OOP)** in Python. It includes two versions:

- `engineBasic.py`: A simplified conceptual model of an ICE.
- `enginePhys.py`: A physics-based simulation incorporating thermodynamics, kinematics, and real-world approximations.

---

## 📁 File Structure

```
.
├── engineBasic.py   # Conceptual OOP simulation of an ICE
├── enginePhys.py    # Physics-based ICE simulation (Otto cycle)
├── README.md        # You're here!
```

---

## 🔧 Requirements

- Python 3.7+
- No external dependencies (standard library only)

To run:

```bash
python engineBasic.py
python enginePhys.py
```

---

## 🚗 engineBasic.py

A high-level simulation that models:
- Cylinders
- Pistons
- Spark plugs
- Crankshaft motion

### Features
- Simplified 4-stroke cycle
- Text-based output of strokes
- OOP design for extendability

### Example Output

```
Engine: Cycle 1
Cylinder 1: Intake stroke - Air/fuel mixture enters.
Piston: Moving down to BDC
Cylinder 1: Compression stroke - Mixture compressed.
Piston: Moving up to TDC
Cylinder 1: Power stroke - Ignition causes expansion.
Piston: Moving down to BDC
Cylinder 1: Exhaust stroke - Gases expelled.
Piston: Moving up to TDC
```

---

## 🔬 enginePhys.py

A more physically accurate engine model based on:
- Ideal Gas Law: `PV = nRT`
- Adiabatic compression & expansion
- Crank angle kinematics
- Basic thermal energy modeling (e.g., combustion adds energy)

### Simulated Concepts
- Realistic piston volume vs crankshaft angle
- Ignition with heat input
- Changing pressure, volume, and temperature in real-time

### Example Output

```
🔥 Cylinder 1: Igniting at 360°
🔁 365° | P: 320456 Pa | T: 890.2 K | V: 0.000085 m³
🔁 370° | P: 298456 Pa | T: 832.1 K | V: 0.000092 m³
```

---

## 🧩 Future Improvements

- Add fuel injection timing
- Include exhaust & intake valve dynamics
- Plot PV diagrams with `matplotlib`
- Multi-cylinder support with firing offsets

---

## 📜 License

This project is open-source and free to use under the MIT License.

---

## ✍️ Author

Created by Saanvi Sethi
Want to simulate ray tracing or other physics systems? Let's connect!
