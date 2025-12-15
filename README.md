# AutoClaim-AutoRoll-AutoReact-MudaeBot-2025

This project is based on: https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2025

**Disclaimer:** I do not condone selfbotting in Discord as it is against their Terms of Service (TOS). This project was used for trolls and friends.

## Updates
- **Button Clicking:** Updated the bot to click buttons for claiming instead of using reactions.
- **Character Sniping:** Added support for sniping specific characters.

## How to Run

### Prerequisites
- Python 3.x installed.
- `pip` (Python package installer).

### Installation
1.  Clone the repository or download the files.
2.  Install the required Python libraries:
    ```bash
    pip install discum requests schedule
    ```

### Configuration
1.  Open `Vars.py` in a text editor.
2.  Update the following variables with your information:
    - `token`: Your Discord user token.
    - `channelId`: The ID of the channel where the bot will roll.
    - `serverId`: The ID of the server (guild) where the bot will roll.
    - `rollCommand`: The slash command to use (e.g., `'wa'`, `'wg'`, etc.).
    - `repeatMinute`: The minute of the hour to start rolling (e.g., `'25'` for XX:25).
    - Customize `desiredCharacters`, `desiredSeries`, and `desiredKakeras` as needed.

### Usage
Run the main bot script:
```bash
python claimOnlyv2.py
```

The bot will start and schedule rolls according to the `repeatMinute` setting in `Vars.py`.

**Note:** dont use the other stuff cuz i didnt test
