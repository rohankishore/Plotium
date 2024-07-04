from const import electronegativity
import matplotlib.pyplot as plt

values = list(electronegativity.values())
elements = list(electronegativity.keys())


def plot():
    plt.figure(figsize=(10, 5))
    plt.plot(elements, values, color='skyblue')
    plt.xlabel('Actinoids')
    plt.ylabel('Electronegativity')
    plt.title('Electronegativity of Actinoids')
    plt.xticks(rotation=90)
    plt.tight_layout()
    return plt
