# Type Practice Programm

## this is a pet-project that the developer will use to practice his typing skills in a programming environment, as the typing-skill is one of the best friends a programmer can have when composing, A' la' Prima.

### - just the same as a musician sings a melody for the first time like he's done it for a thousand times before, only because he has built a robust reading discipline. 


[view live link](https://typinggame.herokuapp.com/)

## Table of contents
 
1.  [Project Mission](#project-mission)
    - [User requirements](#user-requirements)
    - [Developer Goal](#developer-goal)
    - [future improvements](#future-improvements)

2.  [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [Scope]
    3. User Manual

3.  Technical Design
    - Flowchart
    - Data Models
4.  Technologies Used
    - Languages
    - Frameworks and Tools
5.  [Features](#features)
6.  Testing
    - Python Validation
    - Testing user stories
7.  Bugs
8.  Deployment
9.  Credits
10. Acknowledgements

## Project Mission
- User requirements
- Developer Goal

## Technical Design
    
    - the Auth class is using a recursive flow in the majority of it's methods, as it was considered to be a more elegant way to handle the red-cases and insist on the desired outcome in the authentication process  
     
## Technologies Used

## Features

to be implemented: 
currently you can not reset a password if you forget it.
there is only one file to train on
can't press control+backspace for deleting a whole word at once
doesn't tell you if you do the same mistake and what finger is more suitable to press the key that was repeatedly missed. 

## Testing
 1. during development of the three Classes, their methods were runned and tested independently, that way the end-points of each Object remained clear untill the final testing of the overall project. 
 2. [Pyton code validator]() 

## Bugs

1. - when in the game_state.game_start() running the game, if the esc key gets pressed, you return to the home-menu. after enabeling the keypad option in curses, the  stdscr.getkey() was returning '^[' and the esc_code variable was set to the same value: '^[' , but for some reason they were not equal even though the type of both was str.
   - to check if the flow wasn't at fault, I changed the esc-code variable to 'a', and when pressing a the exiting was possible. 
   - I fixed this issue by setting the esc_code variable to chr(27), which seemed to work perfectly

## Deployment

## Credits

## Acknowledgements