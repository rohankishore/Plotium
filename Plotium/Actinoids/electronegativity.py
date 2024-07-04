from const import electronegativity, sec_name
import matplotlib.pyplot as plt

values = list(electronegativity.values())
elements = list(electronegativity.keys())


def plot():
    plt.figure(figsize=(10, 5))
    plt.plot(elements, values, color='skyblue')
    plt.xlabel(f'{sec_name}')
    plt.ylabel('Electronegativity')
    plt.title(f'Electronegativity of {sec_name}')
    plt.xticks(rotation=90)
    plt.tight_layout()
    return plt
