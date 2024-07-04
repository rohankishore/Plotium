from const import density
import matplotlib.pyplot as plt

values = list(density.values())
elements = list(density.keys())


def plot():
    plt.figure(figsize=(10, 5))
    plt.plot(elements, values, color='skyblue')
    plt.xlabel('Actinoids')
    plt.ylabel('Density (in g/cm^3)')
    plt.title('Density of Actinoids')
    plt.xticks(rotation=90)
    plt.tight_layout()
    return plt
