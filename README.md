# Pig Game Project
[Live webpage](https://pig-game-project-426f7f2476af.herokuapp.com/)

Developer : Mattias Lundkvist

## project overview


## Subject 
Made a simple dice game,that you can play when you are bored.

<img src="docs/pig-screendhot.png">



## Table of contents


1. [Project Goal](#project-goal)
2. [User Experience](#user-experience)
    1. [User Requirements and Expectations](#user-requirements-and-expectations)
    2. [User Stories](#user-stories)
3. [Design](#design)
    1. [Colours](#colours)
    2. [Fonts](#fonts)
    3. [Wireframes](#wireframes)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Tools](#tools)
5. [Features](#features)
6. [Testing](#testing)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [Accessibility](#accessibility-testing)
    4. [Performance](#performance)
    5. [Device testing](#performing-tests-on-various-devices)
    6. [Browser compatibility](#browser-compatibility)
    7. [User stories testing](#user-stories-testing)
7. [Bugs](#bugs)    
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgements](#acknowledgements)


## Project goal

The goal of the project was to create a simple app. Which you could play in single play agains the computer,
or together with a few friends

## User Experience

- For someone who is looking to spend a few minutes doing something that requires no deep thinking

### User requirements and expectations

- A easy understandable game
- Game doesn't take to long to play
- Can be enjoyed alone or with friends


### User Stories

### First-Time Users


1. As a first-time user, I would like to have a simple explanation of the rules

2. As a first-time user, I would like to enjoy a short game alone

3. As a first-time user, I would like to enjoy a short game with friends

4. As a first-time user, I would like to keep track of my score easily

5. As a first-time user, I would like to be able to restart a game when the current game is finished



## Features



#### Rule Explanation

When you open the game there will be a choice to show the rules of the game 

<img src="docs/features/quizzes.png">


#### Number of Players

User will be asked how many players will be playing


<img src="docs/features/quizzes.png">


#### 'Dice' rolls

A random number function generates a number between 1 and 6

<img src="docs/features/quizzes.png">


#### Play again

After a winner is decided, user will be asked if they want to play again.
'y' will start a new game and any other button will exit program


<img src="docs/features/right-wrong.png">


#### 1 Player game

User is given a oppurtunity to play against the computer in a 1 player game

<img src="docs/features/right-wrong.png"

#### Multiplayer game

Users up to 4 can play against eachother

 


### Wireframes

<details><summary>start</summary><img src="docs/wireframes/wireframe-start.png"></details>

<details><summary>ongoing</summary><img src="docs/wireframes/wireframe-choice.png"></details>

<details><summary>finished</summary><img src="docs/wireframes/wireframe-fininsh.png"></details>

## Technologies used :

### Languages

- Python

### Tools

- Github
- Gitpod
- Ci Python Linter

## Testing

Ran the code through the Ci Python Linter.
Also played through the game multiple times


## Ci Python Linter

Returns two warnings of the following: E225 missing whitespace around operator.
Although the lines referred to clearly has whitespaces

<img src="docs/line.png"


## User stories testing

### First time users

1. As a first-time user, I would like to have a short quiz about The lord of the rings books

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Lord of the rings quiz| Click Lord of the rings button| Starts Lord of the rings quiz| Works as expected |


<details><summary></summary><img src="docs/userstories/user-story1.png"></details>

2. As a first-time user, I would like to have a short quiz about The Lies of Locke Lamora books

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Locke Lamora quiz| Click Locke Lamora button| Starts Locke Lamora quiz| Works as expected |

<details><summary></summary><img src="docs/userstories/user-story2.png"></details>

3. As a first-time user, I would like to have a short quiz about The first Law triology books

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|First Law quiz| Click First Law button| Starts First Law Quiz| Works as expected |


<details><summary></summary><img src="docs/userstories/user-story3.png"></details>


4. As a first-time user, I would like to keep track of my score easily


| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Score Counter | Answer any question| Answering a question with the right answer will increase the score| Works as expected |

<details><summary></summary><img src="docs/userstories/user-story4.png"></details>

5. As a first-time user, I would like to know which answer is correct

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Correct/Incorrect| Click any answer| Right answer will highlight as green wrong answer as red | Works as expected |

<details><summary></summary><img src="docs/userstories/user-story5.png"></details>

### Site owner

6. As a site owner, I want to test peoples knowledge about the books


| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| All quizzes| Click any quiz| Starts clicked quiz for user| Works as expected |

<details><summary></summary><img src="docs/userstories/user-story6.png"></details>


## Bugs

- There are no known bugs in the code.




## Deployment

The website was deployed using GitHub Pages by following these steps:

1. In the GitHub repository navigate to the Settings tab
2. On the left-hand menu select Pages
3. For the source select Branch: master
4. After the webpage refreshes automatically you will see a ribbon on the top saying: Your site is live at

https://mindfalls.github.io/fantasy-book-quiz/

You can for fork the repository by following these steps:

1. Go to the GitHub repository
2. Click on Fork button in upper right-hand corner

You can clone the repository by following these steps:

1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone.



## Credits

### Images

- background image taken from Shutterstock

### Code

The following tutorials was used as a guide for the application:

[Web dev simplified](https://www.youtube.com/watch?v=riDzcEQbX6k)

[Easy tutorials](https://www.youtube.com/watch?v=PBcqGxrr9g8&t=1856s)
