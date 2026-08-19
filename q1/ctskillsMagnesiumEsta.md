# Computational Thinking Exercise

## Smart School Canteen Queue

**Name:** Xian Kyle Esta
**Section:** Magnesium    
**Date:** August 19, 2026  

---

## Step 1: Identify the Big Problem

### Main Problem
The canteen experiences long, inefficient queues during lunch times, leading to wasted time for students and disorganized order fulfillment for the staff. 
---
## Step 2: Identify the Sub-Problems
1. Some students take their friend's orders so they can avoid the line. 
2. Staff having difficulty managing orders. 
3. The line easily gets crowded because of the number of students ordering. 
4. Some students may accidentally take the wrong order. 
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT skill | Proposed Solution |
| Skipping line | Abstraction| Staff should only get one ticket from students with two or more. |
| Management problem | CT skill | Automatically assign queue numbers and process orders in order. |
| Crowded line | CT skill | Separate the line into two parts: one for odering and paying and one for picking up the ordered food  |
| Wrong Order| CT skill | Identify common causes of wrong orders, such as similar orders or students having similar ticket numbers. |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Wrong Order
### Pseudocode
START
    Student enters their ticket number
    System finds the order matching the ticket number
    System displays the order details
    Student checks that the order is correct
  IF the order matches THEN
    System allows the student to collect the food
  ELSE
    System alerts the canteen staff
    Student waits for the correct order
  END IF
END
