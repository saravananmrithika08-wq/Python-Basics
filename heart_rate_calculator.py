# Heart Rate Zone Calculator
# Mrithika - Biomedical Engineering Student
# Used clinically to determine safe exercise intensity zones

def calculate_max_heart_rate(age):
    return 220 - age

def calculate_zones(max_hr):
    zones = {
        "Zone 1 - Warm Up": (int(max_hr * 0.50), int(max_hr * 0.60)),
        "Zone 2 - Fat Burn": (int(max_hr * 0.60), int(max_hr * 0.70)),
        "Zone 3 - Aerobic": (int(max_hr * 0.70), int(max_hr * 0.80)),
        "Zone 4 - Anaerobic": (int(max_hr * 0.80), int(max_hr * 0.90)),
        "Zone 5 - Maximum": (int(max_hr * 0.90), int(max_hr * 1.00)),
    }
    return zones


# --- Main Program ---
print("=== Heart Rate Zone Calculator ===")
age = int(input("Enter your age: "))

max_hr = calculate_max_heart_rate(age)
zones = calculate_zones(max_hr)

print(f"\nMaximum Heart Rate: {max_hr} bpm")
print("\nYour Training Zones:")
for zone, (low, high) in zones.items():
    print(f"  {zone}: {low} – {high} bpm")
    }

