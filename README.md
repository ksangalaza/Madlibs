# MadLibs

An interactive Madlibs game that *creates* a story by user inputs or computer generated inputs. The users get the option to begin their game by choosing a theme for the game they want to play. The user can also *delete* the saved archives from the entire database at the beginning of the prompts. Once the user chooses a theme they have the option to choose a game mode; either user inputted values or computer generated values. When a user decides to input their values they are prompted to enter pronouns, verbs, adjectives, adverbs, or nouns. Once all values have been entered, the story will print out with the values the user previously inputted. Should a user decide to have the computer generate words, the system will automatically print the story with random generated words *read* from a CSV file. All word data that is entered or generated is *updated* into a MongoDB database/collection. Project changes and updates are uploaded to a GitHub repository.


# Technologies Used

**Python3**
>All code written in Python3 (Modules: Pymongo, Random, CSV)

**MongoDB**
>Database where game data is saved

**VS Code**
>Program used to write code

**Git/GitHub**
>Repository where files and process for this project is saved

# Features

 - Data entered by the user is saved to MongoDB
 - User can play as many times as they want
 - A computer can generate random words for the user
 
**To-do list**
>- Enhance the CLI UI
>- Add more stories to the options
>- Save full stories for user personal use

# Getting Started

unix:
>git clone https://github.com/ksangalaza/Madlibs.git
git pull 
![Cloning to your local repository](https://ucarecdn.com/b45aff8c-4408-4ca2-bc60-2c96f75a3abd/ScreenShot20220524at23943PM.png)
>

VS Code: 
>Download Visual Studio Code and install the Python Extension.
>
>Load the Madlibs_Random **or** your own CSV with words (please include headers for each column).
Load the Madlibs file
Load the words file
>![Files to download](https://ucarecdn.com/58143f03-f6c5-4964-91d4-b92f01c7e456/ScreenShot20220524at25737PM.png)


# Usage

CLI:
>Run the file in the Terminal.
>Begin the interaction
>
>![MadLibs interaction](https://ucarecdn.com/45254786-6058-4b29-8702-13c0aedc092c/ScreenShot20220524at22729PM.png)


>Play as many times as you would like. 
>Delete MongoDB database by choosing the options in the interaction menu.
