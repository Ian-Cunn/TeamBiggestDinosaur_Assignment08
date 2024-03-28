# main.py

#Assignment08 Project
from dataClassPackage.dataClass import Data

if __name__ == "__main__":
    
    # Instantiate object with type data
    myData = Data()
    
    # Invoke the method and store what it returns in another variable 
    myCursor = myData.Connect('GroceryStoreSimulator')
    
    # SQL query
    query = '''
        SELECT dbo.tProduct.ProductID,
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
        print (row[5]);
        print (row[1]);

