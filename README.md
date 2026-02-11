# U.S. States Guessing Game

A fun interactive game built with Python where you test your knowledge of U.S. state locations and names.

## Overview

This project uses the Pandas and Turtle graphics library to display a blank map of the United States. Players are prompted to guess state names, and when a correct guess is made, the state name is displayed on the map at its corresponding location. The game tracks how many states you've correctly guessed out of 50.

## Features

- **Interactive Map Display**: Uses Turtle graphics to show a blank U.S. map background
- **Real-time Feedback**: Correct guesses are displayed on the map with their locations
- **Progress Tracking**: Shows your current score (e.g., "15/50 states guessed")
- **Case-Insensitive Input**: Accepts state names in any case format
- **Missed States Report**: Automatically generates a CSV file of states you couldn't guess for future study

## Requirements

- Python 3.x
- `turtle` (built-in)
- `pandas`

## Installation

```bash
pip install pandas
```

## Files Needed

- `main.py` - Main game script
- `50_states.csv` - Data file containing state names and map coordinates
- `blank_states_img.gif` - Image file of blank U.S. map (must be in same directory)

The CSV should contain at least these columns:
- `state` - State name
- `x` - X-coordinate for display on map
- `y` - Y-coordinate for display on map

## How to Play

1. Run the script:
   ```bash
   python main.py
   ```

2. A window will open with a blank U.S. map

3. When prompted, enter the name of a U.S. state (e.g., "Texas", "california", "NEW YORK")

4. If correct, the state name appears on the map at its location and your score increases

5. Continue guessing until you've found all 50 states or want to quit

6. When you exit the game, a CSV file (`states_to_learn.csv`) is generated containing all the states you missed

## Future Study

After playing, check `states_to_learn.csv` to see which states you need to practice with!

## Project Structure

```
.
├── main.py                    # Main game script
├── 50_states.csv             # State data and coordinates
├── blank_states_img.gif      # Map image
└── states_to_learn.csv       # Generated file with missed states
```

## Notes

- The game is case-insensitive, but state names must match exactly (e.g., "North Carolina", not "N Carolina")
- Duplicate guesses are counted as incorrect
- The game ends when you exit by clicking the window
