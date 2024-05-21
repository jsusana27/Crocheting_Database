CREATE TABLE Yarn (
    YarnID SERIAL PRIMARY KEY,
    Brand VARCHAR(100),
    Price DECIMAL(10, 2),
    FiberType VARCHAR(50),
    FiberWeight INT,
    Color VARCHAR(50),
    YardagePerSkein DECIMAL(10, 2),
    GramsPerSkein DECIMAL(10, 2),
    NumberOfSkeinsOwned INT
);

CREATE TABLE SafetyEyes (
    SafetyEyesID SERIAL PRIMARY KEY,
    Price DECIMAL(10, 2),
    SizeInMM INT,
    Color VARCHAR(50),
    Shape VARCHAR(50),
    NumberOfEyesOwned INT
);

CREATE TABLE Stuffing (
    StuffingID SERIAL PRIMARY KEY,
    Brand VARCHAR(100),
    PricePerFivelbs DECIMAL(10, 2),
    Type VARCHAR(50)
);

CREATE TABLE FinishedProducts (
    FinishedProductsID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    TimeToMake INTERVAL,
    TotalCostToMake DECIMAL(10, 2),
    SalePrice DECIMAL(10, 2),
    NumberInStock INT
);

CREATE TABLE FinishedProductMaterials (
    FinishedProductMaterialsID SERIAL PRIMARY KEY,
    FinishedProductsID INT,
    MaterialType VARCHAR(50),
    MaterialID INT,
    QuantityUsed DECIMAL(10, 2),
    FOREIGN KEY (FinishedProductsID) REFERENCES FinishedProducts(FinishedProductsID)
);

CREATE TABLE Customers (
    CustomerID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    PhoneNumber VARCHAR(30),
    EmailAddress VARCHAR (200)
);

CREATE TABLE CustomerPurchases (
    CustomerPurchaseID SERIAL PRIMARY KEY,
    CustomerID INT,
    FinishedProductsID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (FinishedProductsID) REFERENCES FinishedProducts(FinishedProductsID)
);

CREATE TABLE Orders (
    OrderID SERIAL PRIMARY KEY,
    CustomerID INT,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FormOfPayment VARCHAR(50),
    TotalPrice DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderProducts (
    OrderProductID SERIAL PRIMARY KEY,
    OrderID INT,
    FinishedProductsID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (FinishedProductsID) REFERENCES FinishedProducts(FinishedProductsID)
);
