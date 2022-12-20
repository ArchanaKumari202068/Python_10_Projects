def main():
    print("This program converts US dollars to Rupee")
    print()
    
    # eval is used for evaluation
    dollars =eval(input("Enters amount in dollars: "))

    Rupee = convert_to_Rupee(dollars)
    print("That is",Rupee,"Rupee.")

convert_to_Rupee = lambda dollars: dollars * 82.75
main()   