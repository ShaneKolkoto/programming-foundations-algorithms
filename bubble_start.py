# Bubble sort algorithm

from operator import length_hint


def bubbleSort(dataset):
    # TODO: start with the array length and decrement each item
    # Example of the Perfomance O loop
    for i in range(len(dataset) -1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j + 1]:
                temp = dataset[j]
                dataset[j] = dataset[j + 1]
                dataset[j + 1] = temp
                
    print("Current state: ", dataset)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubbleSort(list1)
    print("Result: ", list1)

if __name__ == "__main__":
    main()