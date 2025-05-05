# KAHOOT BOTS

```
 _  __   _   _  _  ___   ___ _____
| |/ /  /_\ | || |/ _ \ / _ \_   _|
| ' <  / _ \| __ | (_) | (_) || |
|_|\_\/_/_\_\_||_|\___/ \___/ |_|
        | _ )/ _ \_   _/ __|
        | _ \ (_) || | \__ \
        |___/\___/ |_| |___/
```

## Description

KAHOOT BOTS is a tool for automated connection of bots to a Kahoot game. The program allows up to 60 bots to connect simultaneously using proxy servers to bypass Kahoot's connection restrictions.

## Requirements

- Python 3.7+
- Libraries:
  - aiohttp
  - kahoot-py
  - asyncio

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/username/kahootbots.git
   cd kahootbots
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```
   python -m main.core
   ```

2. Follow the instructions in the console:
   - Enter the game PIN (5–7 digits)
   - Specify the number of bots (1–60)
   - Enter the base username (e.g., "Hacker")

## Proxy Setup

The program supports the use of proxies to bypass Kahoot’s limit on connections from a single IP address.

The file `main/src/proxy.txt` should contain a list of proxies in the following format:
```
username:password@ip:port
```

Without proxy servers, the number of bots will be limited.

## Project Structure

- `main/core.py` – main program file
- `main/modules/` – modules for various functions:
  - `banner.py` – greeting banner
  - `clear.py` – console clearing
  - `count.py` – bot count input
  - `pin.py` – game PIN input
- `main/src/` – data files:
  - `proxy.txt` – list of proxy servers
  - `usernames.txt` – list of usernames

## Features

- The program groups bots in batches of 10 per proxy
- The max number of bots is limited by the number of available proxies (10 bots per proxy)
- Once connected, bots remain in the game until it ends

## Troubleshooting

1. **"Proxy file not found" error**:
   - Make sure the file `main/src/proxy.txt` exists and contains valid data

2. **Bots fail to connect**:
   - Check the availability of proxy servers
   - Verify that the game PIN is correct
   - Ensure you have an internet connection

## Limitations

- Kahoot may block suspicious connections
- Without proxies, only a few bots can connect
- A stable internet connection is required

## License

This project is licensed under the MIT License.
