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
3. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Tools](#tools)
4. [Features](#features)
5. [Testing](#testing)
    1. [User stories testing](#user-stories-testing)
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

Up to 4 users can play against eachother

 
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


The app was deployed to Heroku CLI. The steps to deploy are as follows:

 * After creating an account and logging in, click "New" to create a new app from the dashboard.

 * Choose a unique name for the app and select relevant region; press "Create app".

 * Go to "Settings" and navigate to Config Vars.

 * Add Config Vars. 
 For this app only one was used: KEY = PORT : VALUE = 8000.
 
 * Add buildpacks Python and NodeJS - in this order.
 
 * Click the Deploy tab.
 
 * Scroll Down to Deployment Method and select GitHub.
 
 * Select repository to be deployed and connect to Heroku.
 
 * Scroll down to deploy: 
    * Option 1 is selecting Automatic deploys (Will Update Automatically with every "git push").
    * Option 2 is selecting Manual deploy (Needs to be manually redeployed after every change, via Heroku deploy tab).



## Credits


### Code

The following tutorial was used as a guide for the application:

[Tech with tim](https://www.youtube.com/watch?v=21FnnGKSRZo)

