#write a program to find maximum monthly income between 3 persons
shiva_income=float(input("enter shiva income:"))
rudra_income=float(input("enter rudra income:"))
raama_income=float(input("enter raama income:"))
if shiva_income>rudra_income:
    print("shiva_income is maximum")
elif rudra_income>raama_income:
    print("rudra_income is maximum")
elif raama_income>shiva_income:
    print("raama_income is maximum")    
    