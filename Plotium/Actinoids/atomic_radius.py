from const import atomic_radii
import matplotlib.pyplot as plt

values = list(atomic_radii.values())
elements = list(atomic_radii.keys())


def plot():
    plt.figure(figsize=(10, 5))
    plt.plot(elements, values, color='skyblue')
    plt.xlabel('Actinides')
    plt.ylabel('Atomic Radii (in Angstroms)')
    plt.title('Atomic Radii of Actinides')
    plt.xticks(rotation=90)
    plt.tight_layout()
    return plt
