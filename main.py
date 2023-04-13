import Functions

def main():
    # print(Functions.concat('str', 'ing'))

    #list
    # myFirstList = [1, 2, 3, 4, 5, 6]

    #dictionary -        key      :  value
    myFirstDictionary = {
        "day one": "Monday", 
        "day two": "Tuesday", 
        "day three": "Wednesday"
        }

    # print(myFirstDictionary["day three"])

    myFirstDictionary["day four"] = "Thursday"

    print(myFirstDictionary["day four"])


if __name__ == "__main__":
    main()
