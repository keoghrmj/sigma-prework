def max(array):
    remove_square_brackets = array.strip("[]").split(',')
    int_list = [int(num) for num in remove_square_brackets]
    max = int_list[0]
    for x in range(1, len(int_list)):
        if max < int_list[x]:
            max = int_list[x]
    return max


def min(array):
    remove_square_brackets = array.strip("[]").split(',')
    int_list = [int(num) for num in remove_square_brackets]
    min = int_list[0]
    for x in range(1, len(int_list)):
        if min > int_list[x]:
            min = int_list[x]
    return min


if __name__ == "__main__":
    array = input("Please enter an array of numbers: ")
    print(f'The maximum and minimum of the given array are {
          max(array)} and {min(array)} respectively')
