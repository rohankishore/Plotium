from const import density, sec_name
import matplotlib.pyplot as plt

values = list(density.values())
elements = list(density.keys())


def plot():
    plt.figure(figsize=(10, 5))
    plt.plot(elements, values, color='skyblue')
    plt.xlabel(f'{sec_name}')
    plt.ylabel('Density (in g/cm^3)')
    plt.title(f'Density of {sec_name}')
    plt.xticks(rotation=90)
    plt.tight_layout()
    return plt
