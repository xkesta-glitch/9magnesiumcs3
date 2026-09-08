# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision
No major changes were needed from my original design.

## Visibility Decisions
| Attribute | Data Type | Visibility | Why Public/Private? |
|---|---|---|---|
| Name | string | Public | The name of the song is public so it can easily be found. |
| Author | string | Public | The author of the song is public, because it is another way to find the song. |
| Duration | integer | Private | The duration is private, because it isn't needed when finding a song. |
| Release Date | string | Private | The release date is private, becausse it isn't needed when finding a song. |

## Updated UML Class Diagram
<img width="1545" height="1999" alt="P-pop 2" src="https://github.com/user-attachments/assets/80537df0-1dc7-4f84-9d48-458981d3c79b" />

## Python Implementation
[View Python Source](https://github.com/xkesta-glitch/9magnesiumcs3/blob/main/q1/classImplementation.py)

## Test Run
<img width="1917" height="1021" alt="Screenshot 2026-09-09 002622" src="https://github.com/user-attachments/assets/7cd24111-8eab-4c60-ba0b-dd7f8d6cea55" />
<img width="1917" height="1013" alt="Screenshot 2026-09-09 002645" src="https://github.com/user-attachments/assets/67517444-4fe4-4f98-af0c-5e3230bd27e0" />

## Object Diagram
<img width="1545" height="1999" alt="P-pop 3" src="https://github.com/user-attachments/assets/de4f0eb4-6baa-4732-8820-c31be6c818f4" />

## Analysis
### 1. Why did you make your chosen attribute private?
- Because they are irrelevant when finding a specific song and they just take up wasted space.
### 2. Which method changes the state of your object?
- The fast_forward changes the state of my object.
### 3. How did your two objects demonstrate that instances are independent?
- When both song's durations were changed.
### What is the difference between your class diagram and your object diagram?
- The class diagram shows the attributes, data types, and methods. The object diagram shows more specific intances and values.
