# gesture-gaming README.md

# Gesture Controlled Gaming

This project implements a gesture-controlled gaming experience using Python, MediaPipe, OpenCV, and Selenium. The game recognizes hand gestures to control character movements and actions.

## Project Structure

```
gesture-gaming
├── src
│   ├── main.py
│   ├── hand_detector.py
│   ├── game_controller.py
│   └── utils
│       └── constants.py
├── tests
│   └── test_hand_detector.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd gesture-gaming
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the game, run the following command:
```
python src/main.py
```

## Gesture Controls

- **1 Finger**: Jump
- **2 Fingers**: Roll
- **3 Fingers**: Move Right
- **4 Fingers**: Move Left

## Contributing

Feel free to submit issues or pull requests for improvements and bug fixes.