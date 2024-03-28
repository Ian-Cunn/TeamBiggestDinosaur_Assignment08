# main.py
# Name: TeamBiggestDinosaur (Harsh Shah, Ian Cunninghan, and Elizabeth Stapelton)
# email: shahh4@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 03/28/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: It prints the data from grocery store stimulator database online. 
# Anything else that's relevant: Used worked done in class as a reference. 

from dataClassPackage.dataClass import Data

if __name__ == "__main__":
    
    # Instantiate object with type data
    myData = Data()
    
    # Invoke the method and store what it returns in another variable 
    myCursor = myData.Connect('GroceryStoreSimulator')
    
    # SQL query
    query = '''
        SELECT TOP 1 dbo.tProduct.ProductID,
               dbo.tName.Name,
               dbo.tProduct.Description,
               dbo.tStore.Store,
               dbo.tStore.State,
               MIN(dbo.tProductPriceHist.PricePerSellableUnit) AS Min_Price_of_Product
        FROM dbo.tProduct
        INNER JOIN dbo.tProductPriceHist ON dbo.tProduct.ProductID = dbo.tProductPriceHist.ProductID
        INNER JOIN dbo.tName ON dbo.tProduct.NameID = dbo.tName.NameID
        INNER JOIN dbo.tStore ON dbo.tProductPriceHist.StoreID = dbo.tStore.StoreID
        WHERE dbo.tStore.State = 'TX'
        GROUP BY dbo.tName.Name,
                 dbo.tProduct.ProductID,
                 dbo.tProduct.Description,
                 dbo.tStore.Store,
                 dbo.tStore.State
        ORDER BY Min_Price_of_Product '''
    
    
    # Execute query
    myCursor.execute(query)
    
  
    for row in myCursor:
        location = row[3]
        state = row[4]
        product = row[1]
        price = row[5]
        print(f"Cheapest product in {state}, (Texas) is {product} which costs {price} dollars.")
        
