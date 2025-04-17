# 🧪 Quantum Channel Analysis with Qiskit

A project into simulating **noisy quantum channels** using Qiskit 2.0, and analyzing their impact on quantum states through key **quantum information theory** metrics.

---

## 📌 Project Goal

The goal of this project is to:

- Simulate quantum noise models (e.g., amplitude damping, depolarizing, phase damping).
- Study how these channels affect quantum states.
- Apply **quantum information theory tools** like:
  - Fidelity
  - Trace distance
  - Entropy
  - Channel discrimination

---

## 🧱 Structure

This project is broken into the following phases:

### ✅ Phase 1: Channel Simulation
- Prepare quantum states (e.g., `|+⟩`, Bell states)
- Apply noisy channels to states
- Visualize and store resulting density matrices

### 📊 Phase 2: Information-Theoretic Analysis
- Compute fidelity and trace distance
- Analyze entropy changes
- Compare behavior under different channels

### 🔬 Phase 3 (Planned): Channel Discrimination Task
- Use measurements and statistics to distinguish between unknown quantum channels
- Explore optimal input states for discrimination

---

## 📦 Tech Stack

- **Qiskit v2.0** (`quantum_info`, `primitives`)
- **Python 3.10+**
- `NumPy` and `Matplotlib` for calculations and visualizations
- Optionally: `SciPy`, `Seaborn` for advanced plotting or metrics

---


---

## 🛠️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/Ishaan-Chaturvedi/quantum-noise-analysis.git
cd quantum-noise-analysis

# Install dependencies
pip install -r requirements.txt
