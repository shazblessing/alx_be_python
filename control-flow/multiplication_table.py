def main():
    #Prompt user for a Number

    number = int(input("Enter a number to see its multiplication table: "))


    #Generate and Print the Multiplication Table
    for i in range(1, 11):

        product = number * i

        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    main()