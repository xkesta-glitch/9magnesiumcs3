# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](https://github.com/xkesta-glitch/9magnesiumcs3/blob/main/q1/classObjectUML.md)

[Part II - Class Attributes and Methods](https://github.com/xkesta-glitch/9magnesiumcs3/blob/main/q1/classAttributesMethods.md)
## Existing Class
Class: P-pop
Description: My top 2 favorite P-pop music
## New Related Class
Class: Album
Description: All P-pop music compiled
## Association
Relationship: Album HAS P-pop songs
Explanation: Album contains different p-pop songs
## Multiplicity
| UML | Meaning |
|---|---|
| 1 | Exactly one |
| 0..* | Zero or more

Multiplicity: '1' to '0..*'
Explanation: One Album can have zero or more P-pop songs
## UML Class Relationship Diagram
![Class Relationship Diagram](<img width="1545" height="1999" alt="P-pop" src="https://github.com/user-attachments/assets/8c0ba1ad-db45-4ad9-9937-54a290f0aa54" />
)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
