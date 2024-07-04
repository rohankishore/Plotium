from const import melting_point, sec_name
import matplotlib.pyplot as plt

values = list(melting_point.values())
elements = list(melting_point.keys())


def plot():
    plt.figure(figsize=(10, 5))
    plt.plot(elements, values, color='skyblue')
    plt.xlabel(f'{sec_name}')
    plt.ylabel('Melting Point (in K)')
    plt.title(f'Melting Point of {sec_name}')
    plt.xticks(rotation=90)
    plt.tight_layout()
    return plt
