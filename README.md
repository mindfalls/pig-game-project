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


#### 

Clicking the right answer will highlight the answer in green and reveal a next button.
Also clicking the wrong answer will highlight the wrong answer in red and also the right answer in green.


<img src="docs/features/right-wrong.png">


#### Next Button

Clicking the next button will take you to the next question, or reveal your final score

<img src="docs/features/right-wrong.png"

#### Score Counter

Answering a question will increase the score for a maximum of five

<img src="docs/features/right-wrong.png"

#### 404

made a very simple 404 page

<img src="docs/features/404.png"

## Design

### Layout

A simple Layout with a fantasy inspired picture as a background and a square container to hold the quiz

### Colours

I chose antiquewhite for the container i the used a color generator to generate complimentary colors


The specific colours I used on the site are as follows:

1.	Antiquewhite
2.	#FFFBF5
3.	green : rgba(0, 128, 0, 0.5)
4.  red : rgba(255, 0, 0, 0.5)


### Fonts

Google fonts was used to import the Medieval Sharp font since it goes well with the medival fantasy settings for the books

[MedievalSharp]('https://fonts.googleapis.com/css2?family=MedievalSharp&display=swap');



### Wireframes

<details><summary>start</summary><img src="docs/wireframes/wireframe-start.png"></details>

<details><summary>ongoing</summary><img src="docs/wireframes/wireframe-choice.png"></details>

<details><summary>finished</summary><img src="docs/wireframes/wireframe-fininsh.png"></details>

## Technologies used :

### Languages

- HTML
- CSS
- JavaScript

### Tools

- Github
- Gitpod
- Tiny PNG
- Google Fonts
- W3C Validator
- Jigsaw CSS Validator
- WAVE Web Accessibility Evaluation Tool
- Jshint

## Testing

The WC3C Validation Service was used to test and validate the HTML of the website.
Jigsaw CSS Validator is used for the CSS.
WAVE Web Accessibility Evaluation Tool is used to test accesibility function.


## HTML Validation

All tests returned no errors

[Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmindfalls.github.io%2Ffantasy-book-quiz%2F)

## CSS Validation

All tests returned no errors

[Link](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmindfalls.github.io%2Ffantasy-book-quiz%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

## Jshint

Test in Jshint passed with no errors

## Accessibility testing

All tests returned no errors

[Link](https://wave.webaim.org/report#/https://mindfalls.github.io/fantasy-book-quiz/)
Index 

## Performance

Google Lighthouse in Google Chrome Developer Tools was used to test the performance of the website. All aspects are performing well.

index : 

<img src="docs/lighthouse/lighthouse-test.png">



### Performing tests on various devices 

The website was tested on the following devices:
- Lenove i5 Legion desktop 
- Ipad Tablet
- Samsung Galaxy S20

In addition, the website was tested using Google Chrome Developer Tools device toggle option for all available device options.

### Browser compatibility

The website was tested on the following browsers:
- Google Chrome
- Apple Safari
- Mozilla Firefox

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
