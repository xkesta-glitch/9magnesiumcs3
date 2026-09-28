#Advanced Class Relationships
## Previous Activities
[classAttrib](https://github.com/xkesta-glitch/9magnesiumcs3/blob/main/q1/classAttributesMethods.md)

[classRel](https://github.com/xkesta-glitch/9magnesiumcs3/blob/main/q1/classRelationships.md)
## Existing System Description:
## Inheritance Relationship
Parent: P-pop

Child: P-pop groups

Explanation: They inherit the properties and adds groups.
## Inheritance UML
![Inheritance](https://github.com/xkesta-glitch/9magnesiumcs3/blob/main/q1/inheritance.png)
## Composition/Aggregation
Relationship: Aggregation, HAS-A

Explanation: Album contains P-pop songs and P-pop groups.
## Advanced UML Diagram
![Advanced UML](https://github.com/xkesta-glitch/9magnesiumcs3/blob/main/q1/advanceRelationshipsClassDiagram.png)
## Python Implementation
[Source Code](https://github.com/xkesta-glitch/9magnesiumcs3/blob/main/q1/advanceRelationships.py)
## Test Run
![Test](https://github.com/xkesta-glitch/9magnesiumcs3/blob/main/q1/Screenshot%202026-09-29%20002257.png)
## Object Diagram
![Objects](https://github.com/xkesta-glitch/9magnesiumcs3/blob/main/q1/advanceRelationshipsObjectDiagram.png) 
## Reflection
Answers: 
1. Why did you choose your inheritance relationship? Explain why your child class is a type of your
parent class.
- I chose P-pop groups as an inheritance relationship because they have the same basic properties. 
2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
- It reused all the other properties from the P-pop songs.
3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship
between the two objects.
- Its Aggregation because they do not depent on the album.
4. What is the difference between Association from Part III and the advanced relationship you
implemented?
- Part III only showed how two classes interact, while advanced relationship provided more detail and information.
5. How does your design follow the DRY principle?
- It reuses and keeps the old attributes so I won't need to rewrite the code.
