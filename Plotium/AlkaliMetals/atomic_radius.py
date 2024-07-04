from const import atomic_radii, sec_name
import matplotlib.pyplot as plt

values = list(atomic_radii.values())
elements = list(atomic_radii.keys())


def plot():
    plt.figure(figsize=(10, 5))
    plt.plot(elements, values, color='skyblue')
    plt.xlabel(f'{sec_name}')
    plt.ylabel('Atomic Radii (in Angstroms)')
    plt.title(f'Atomic Radii of {sec_name}')
    plt.xticks(rotation=90)
    plt.tight_layout()
    return plt