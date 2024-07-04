from const import boiling_point, sec_name
import matplotlib.pyplot as plt

values = list(boiling_point.values())
elements = list(boiling_point.keys())


def plot():
    plt.figure(figsize=(10, 5))
    plt.plot(elements, values, color='skyblue')
    plt.xlabel(f'{sec_name}')
    plt.ylabel('Boiling Point (in K)')
    plt.title(f'Boiling Point of {sec_name}')
    plt.xticks(rotation=90)
    plt.tight_layout()
    return plt
