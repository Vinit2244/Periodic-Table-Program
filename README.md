# Periodic Table Program Readme

I developed this as a personal project as my class 12th year end project.

## Project Overview

This Python-based Periodic Table program provides users with an interactive interface to explore information about the 118 chemical elements. The program includes a secure login system, utilizes an SQL database to store user credentials, and incorporates audio narration using Google Text-to-Speech. Users can navigate through elements, view detailed information, and listen to descriptions.

## Getting Started

### Prerequisites

Make sure to have the following dependencies installed:

1. **Tkinter:** `pip install tk`
2. **Mysql Connector:** `pip install mysql-connector-python`
3. **Pillow (PIL):** `pip install Pillow`
4. **Pygame:** `pip install pygame`
5. **Keyboard:** `pip install keyboard`

### Additional Setup

- Run the program as an administrator.
- Execute the 'audio_generator' file in the audio folder if audio files are not created.

### Installing Tkinter on Various Platforms

#### Ubuntu/Debian:

```bash
sudo apt-get install python3-tk
```
#### MacOS:
```bash
sudo brew install python-tk@3.10
```

### Running the Program
1. If running the program for the first time:
    <ul>
        <li>Run the database creator script.</li>
        <li>Execute the audio generator script.</li>
    </ul>
2. Launch the Python app.

3. The login window will appear. Users can log in or create a new account.

4. Explore the Periodic Table:
    <ul>
        <li>Click on an element to view detailed information and an image.</li>
        <li>Use the Google Text-to-Speech library to convert and listen to the element's description. Press 'Esc' to stop audio.</li>
    </ul>
5. Navigate through elements using forward and backward buttons.
6. Switch accounts or log out when done.

### Authors
Vinit Mehta

### Acknowledgments
<ul>
    <li>Special thanks to the creators of Tkinter, Mysql Connector, Pillow, Pygame, and Keyboard modules.</li>
    <li>Google Text-to-Speech API for audio narration.</li>
</ul>

<br>

Feel free to contribute to the project and improve its functionality!