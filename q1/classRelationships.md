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
![Class Relationship Diagram](https://github.com/xkesta-glitch/9magnesiumcs3/blob/main/q1/P-pop.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](https://github.com/xkesta-glitch/9magnesiumcs3/blob/main/q1/Screenshot%202026-09-28%20001010.png)
## Object Relationship Diagram
![Object Relationship Diagram](https://github.com/xkesta-glitch/9magnesiumcs3/blob/main/q1/Album.png)
## Analysis
### What is the association between your two classes?
- Their association is stores HAS-A relationship, the Album stores P-pop songs. The albums allows for easy access to the songs. 
### What multiplicity did you choose and why?
- 1 to 0..* because the album can store 0 or more songs. The album can have no songs and have many songs added to it later.
### How did you implement the relationship in Python?
- I turn the album into an empty list.
### Why did you store an object reference instead of copying its data?
- It prevents data duplication.
### If your relationship uses many, why is a list appropriate?
- It is appropriate because it adjusts the album if songs are added or removed.
