# Eye Saver 👁️

A simple and elegant desktop application to remind you to take breaks and rest your eyes.

![Eye Saver Screenshot](https://i.imgur.com/your-screenshot.png)  <!-- Replace with a real screenshot -->

## 🌟 Features

*   **Customizable Countdown Timer:** Set the timer for any duration you want (in HH:MM:SS format).
*   **Audio Alerts:** A gentle bell chime and a "Time's Up" voice alert will notify you when it's time for a break.
*   **Simple and Clean UI:** An intuitive and easy-to-use interface built with Pygame.
*   **Persistent Settings:** The app remembers your last used timer duration.

## 🚀 How to Use

1.  **Prerequisites:** Make sure you have Python and Pygame installed.
    ```bash
    pip install pygame
    ```
2.  **Run the application:**
    ```bash
    python main.py
    ```
3.  **Set the timer:**
    *   Click on the input box on the right.
    *   Enter your desired break interval in `HH:MM:SS` format (e.g., `0:30:0` for 30 minutes).
    *   Press `Enter`.
4.  **Start the countdown:**
    *   Click the "START" button.
    *   The timer will begin, and you'll see a confirmation message.
5.  **Time for a break!**
    *   When the countdown finishes, the app will play a sound to notify you.
    *   Click "RESET" to start a new countdown with the same duration.

## 🛠️ Dependencies

*   [Python](https://www.python.org/)
*   [Pygame](https://www.pygame.org/)
*   [playsound](https://pypi.org/project/playsound/)

You can install all the dependencies using pip:

```bash
pip install -r requirements.txt
```
*(Note: You may need to create a `requirements.txt` file)*

## 🎨 Customization

You can easily change the notification sounds:

1.  Place your desired `.mp3` files in the `sound/` directory.
2.  Update the file names in `main.py`:
    ```python
    times_up_sound_file_name = os.path.join("sound", "your_new_times_up_sound.mp3")
    bell_chime_sound_file_name = os.path.join("sound", "your_new_bell_chime_sound.mp3")
    ```

## 🙌 Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.