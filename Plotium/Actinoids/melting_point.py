from const import melting_point
import matplotlib.pyplot as plt

values = list(melting_point.values())
elements = list(melting_point.keys())


def plot():
    plt.figure(figsize=(10, 5))
    plt.plot(elements, values, color='skyblue')
    plt.xlabel('Actinides')
    plt.ylabel('Melting Point (in K)')
    plt.title('Melting Point of Actinides')
    plt.xticks(rotation=90)
    plt.tight_layout()
    return plt
