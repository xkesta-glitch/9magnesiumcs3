# ILA 3-1: Applying the Four Pillars of OOP

**Name:** Xian Kyle Esta
**Section:** Magnesium    
**Date:** August 20, 2026

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation groups variables and methods together to form one object. Properties are variables inside the object which can be simple data types like strings or integers and can also be complex data structures like lists or dictionaries.
CLASS Product
   PRIVATE name
   PRIVATE price
   PRIVATE stock

   METHOD addStock(amount)
        stock = stock + amount
   END METHOD

   METHOD removeStock(amount)
       IF amount <= stock THEN
           stock = stock - amount
       END IF
   END METHOD
END CLASS

### 2. Abstraction
Abstraction is a design-level concept focusing on hiding irrelevant details to simplify the model. This allows developers creating the model to put effort in enhancing it. Developers working on others would not need to know how certain elements work inside the model.
ABSTRACT CLASS Product
   name
   price

   METHOD displayDetails()
       DISPLAY name
       DISPLAY price
   END METHOD
END CLASS

### 3. Inheritance
Inheritance allows objects to acquire the properties and methods of an existing parent object. Conversely, this also allows objects to pass their properties and methods down to objects that use the former as a parent object.
CLASS Product
   name
   price
   stock
END CLASS

CLASS FoodProduct INHERITS Product
   expirationDate
END CLASS

CLASS HouseholdProduct INHERITS Product
   category
END CLASS

### 4. Polymorphism
Polymorphism allows objects to take on different forms and behave differently. This may use and reuse existing code to reduce development time. 
CLASS Product
    METHOD displayDetails()
        DISPLAY "Product details"
    END METHOD
END CLASS

CLASS FoodProduct INHERITS Product
    METHOD displayDetails()
        DISPLAY "Food product details"
    END METHOD
END CLASS

CLASS HouseholdProduct INHERITS Product
    METHOD displayDetails()
        DISPLAY "Household product details"
    END METHOD
END CLASS

CREATE food AS FoodProduct
CREATE household AS HouseholdProduct

CALL food.displayDetails()
CALL household.displayDetails()

## Reflection
Among the four pillars of Object-Oriented Programming, I think encapsulation would be the most useful for improving the sari-sari store inventory system. It keeps important information such as product prices and stock quantities protected and ensures that they are changed only through proper methods. This can help prevent incorrect inventory data and make the program easier to maintain.
