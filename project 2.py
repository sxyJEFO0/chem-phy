# Molecular Weight Calculator

# Define atomic weights dictionary (in atomic mass units, u)
atomic_weights = {
    'H': [1.00784, 1.00811],
    'He': 4.002602,
    'Li': [6.938, 6.997],
    'Be': 9.0121831,
    'B': [10.806, 10.821],
    'C': [12.0096, 12.0116],
    'N': [14.00643, 14.00728],
    'O': [15.99903, 15.99977],
    'F': 18.998403163,
    'Ne': 20.1797,
    'Na': 22.98976928,
    'Mg': [24.304, 24.307],
    'Al': 26.9815385,
    'Si': [28.084, 28.086],
    'P': 30.973761998,
    'S': [32.059, 32.076],
    'Cl': [35.446, 35.457],
    'Ar': 39.948,
    'K': 39.0983,
    'Ca': 40.078,
    'Sc': 44.955908,
    'Ti': 47.867,
    'V': 50.9415,
    'Cr': 51.9961,
    'Mn': 54.938044,
    'Fe': 55.845,
    'Co': 58.933194,
    'Ni': 58.6934,
    'Cu': 63.546,
    'Zn': 65.38,
    'Ga': 69.723,
    'Ge': 72.630,
    'As': 74.921595,
    'Se': 78.971,
    'Br': [79.901, 79.907],
    'Kr': 83.798,
    'Rb': 85.4678,
    'Sr': 87.62,
    'Y': 88.90594,
    'Zr': 91.224,
    'Nb': 92.90637,
    'Mo': 95.95,
    'Tc': 97,  # Note: Tc is an integer
    'Ru': 101.07,
    'Rh': 102.90550,
    'Pd': 106.42,
    'Ag': 107.8682,
    'Cd': 112.414,
    'In': 114.818,
    'Sn': 118.710,
    'Sb': 121.760,
    'Te': 127.60,
    'I': 126.90447,
    'Xe': 131.293,
    'Cs': 132.90545196,
    'Ba': 137.327,
    'La': 138.90547,
    'Ce': 140.116,
    'Pr': 140.90766,
    'Nd': 144.242,
    'Pm': 145,  # Note: Pm is an integer
    'Sm': 150.36,
    'Eu': 151.964,
    'Gd': 157.25,
    'Tb': 158.92535,
    'Dy': 162.500,
    'Ho': 164.93033,
    'Er': 167.259,
    'Tm': 168.93422,
    'Yb': 173.045,
    'Lu': 174.9668,
    'Hf': 178.49,
    'Ta': 180.94788,
    'W': 183.84,
    'Re': 186.207,
    'Os': 190.23,
    'Ir': 192.217,
    'Pt': 195.084,
    'Au': 196.966569,
    'Hg': 200.592,
    'Tl': [204.382, 204.385],
    'Pb': 207.2,
    'Bi': 208.98040,
    'Po': 209,  # Note: Po is an integer
    'At': 210,  # Note: At is an integer
    'Rn': 222,  # Note: Rn is an integer
    'Fr': 223,  # Note: Fr is an integer
    'Ra': 226,  # Note: Ra is an integer
    'Ac': 227,  # Note: Ac is an integer
    'Th': 232.0377,
    'Pa': 231.03588,
    'U': 238.02891,
    'Np': 237,  # Note: Np is an integer
    'Pu': 244,  # Note: Pu is an integer
    'Am': 243,  # Note: Am is an integer
    'Cm': 247,  # Note: Cm is an integer
    'Bk': 247,  # Note: Bk is an integer
    'Cf': 251,  # Note: Cf is an integer
    'Es': 252,  # Note: Es is an integer
    'Fm': 257,  # Note: Fm is an integer
    'Md': 258,  # Note: Md is an integer
    'No': 259,  # Note: No is an integer
    'Lr': 262,  # Note: Lr is an integer
    'Rf': 263,  # Note: Rf is an integer
    'Db': 268,  # Note: Db is an integer
    'Sg': 271,  # Note: Sg is an integer
    'Bh': 270,  # Note: Bh is an integer
    'Hs': 270,  # Note: Hs is an integer
    'Mt': 278,  # Note: Mt is an integer
    'Ds': 281,  # Note: Ds is an integer
    'Rg': 281,  # Note: Rg is an integer
    'Cn': 285,  # Note: Cn is an integer
    'Uut': 286,  # Note: Uut is an integer
    'Fl': 289,  # Note: Fl is an integer
    'Uup': 289,  # Note: Uup is an integer
    'Lv': 293,  # Note: Lv is an integer
    'Uus': 294,  # Note: Uus is an integer
    'Uuo': 294,  # Note: Uuo is an integer
}

def calculate_molecular_weight(formula):
    total_weight = 0.0
    current_element = ''
    current_count = 0

    for char in formula:
        if char.isalpha():
            if current_element:
                # Update total weight based on the current element and count
                if current_element in atomic_weights:
                    atomic_weight = atomic_weights[current_element]
                    if isinstance(atomic_weight, list):
                        # Choose the first isotope in the list
                        atomic_weight = atomic_weight[0]
                    total_weight += atomic_weight * current_count

            # Start a new element
            current_element = char
            current_count = 1
        elif char.isdigit():
            # Update the count if the character is a digit
            current_count = int(char)
        else:
            # Handle parentheses, if needed
            pass

    # Calculate the weight of the last element
    if current_element:
        if current_element in atomic_weights:
            atomic_weight = atomic_weights[current_element]
            if isinstance(atomic_weight, list):
                # Choose the first isotope in the list
                atomic_weight = atomic_weight[0]
            total_weight += atomic_weight * current_count

    return total_weight

def main():
    print("Welcome to the Molecular Weight Calculator!")
    chemical_formula = input("Enter the chemical formula: ")

    molecular_weight = calculate_molecular_weight(chemical_formula)
    print(f"The molecular weight of {chemical_formula} is: {molecular_weight} u")

if __name__ == "__main__":
    main()
