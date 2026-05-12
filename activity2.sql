CREATE TABLE IF NOT EXISTS Salesman (

    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    comission REAL
);

INSERT INTO Salesman (Salesman_id, name, city, comission) VALUES
    ('S001', 'John Doe', 'New York', 0.15),
    ('S002', 'Nail Knit', 'Paris', 0.13),
    ('S005', 'Pit Alex', 'London', 0.11),
    ('S006', 'Mc Lyon', 'Paris', 0.14),
    ('S007', 'Paul Adam', 'Rome', 0.13),
    ('S003', 'Lauson Hen', 'AthSan Jose', 0.12);

    SELECT * FROM Salesman;

    CREATE TABLE IF NOT EXISTS Orders (

        ord_no TEXT PRIMARY KEY,
        purch_amt REAL,
        ord_date TEXT,
        customer_id TEXT,
        salesman_id TEXT
    );

    INSERT INTO Orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
        ('O001', 1500.00, '2024-01-10', 'C001', 'S001'),
        ('O002', 2500.00, '2024-01-15', 'C002', 'S002'),
        ('O003', 500.00, '2024-01-20', 'C003', 'S005'),
        ('O004', 3000.00, '2024-01-25', 'C004', 'S006'),
        ('O005', 2000.00, '2024-01-30', 'C005', 'S007'),
        ('O006', 1200.00, '2024-02-05', 'C006', 'S003');

        SELECT * FROM Orders;

        SELECT NAME, Comission
        FROM Salesman;
        


