# Twitch Username Availability Checker

This script checks the availability of usernames on Twitch using the Twitch GraphQL API. It reads a list of usernames from a file and outputs the available and unavailable usernames to separate files.

## Prerequisites

- Python 3.6 or higher
- `aiohttp` library
- `colorama` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/dancer/twitch-username-checker.git
    cd twitch-username-checker
    ```

2. Install the required Python packages:

    ```bash
    pip install aiohttp colorama
    ```

## Usage

1. Create a `words.txt` file in the same directory as `twitch.py` and list the usernames you want to check, one per line.

2. Run the script:

    ```bash
    python twitch.py
    ```

3. The script will output the available usernames to `available.txt` and the unavailable usernames to `unavailable.txt`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you have suggestions for improvements or find a bug, feel free to open an issue or submit a pull request.

## Acknowledgments

- This script uses the Twitch GraphQL API to check username availability.
