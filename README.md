# streampeek

streampeek is a simple command-line tool that checks if your favorite Twitch streamers are currently live.

## Features

- Check if specific Twitch streamers are currently live
- Display what game they're playing
- Can be integrated with other scripts (like the included demo launcher)

## Setup

### Prerequisites

- Python 3
- pip packages: `requests`, `python-dotenv`

### Twitch API Setup

1. Visit the [Twitch Developer Console](https://dev.twitch.tv/console/apps)
2. Log in with your Twitch account
3. Click "Register Your Application"
4. Fill in the required fields:
   - Name: StreamPeek (or any name you prefer)
   - OAuth Redirect URLs: http://localhost (this won't actually be used)
   - Category: Select "Application Integration"
5. Click "Create"
6. On the next screen, take note of your Client ID
7. Click "New Secret" to generate a Client Secret
8. Copy both the Client ID and Client Secret

### Configuration

1. Clone the repository
2. Create a `.env` file in the project directory (see `.env.example`)
3. Add your Twitch API credentials:

   ```
   TWITCH_CLIENT_ID=your_client_id
   TWITCH_CLIENT_SECRET=your_client_secret
   ```
4. Save the file
5. Edit the `streampeek.py` file to specify which streamers you want to track

## Usage

1. Run `python streampeek.py` or `python3 streampeek.py`
2. The script will display which streamers are currently live and what games they're playing

## Integration Example

For an example on how I would use this script I included a dirty little demo launcher. It shows the currently online streamers in wofi (should also work with dmenu, rofi, etc) and opens the URL in firefox via cli. I haven't tested this for any other browsers but shouldn't be hard to figure out.

To use it you have to make `launcher.sh` executable and pipe the output of streampeek into the launcher.
`$ chmod +x launcher.sh`
`$ python3 streampeek.py | ./launcher.sh`


## Troubleshooting

- Double-check your Twitch API credentials in the `.env` file
- Refer to the [Twitch API documentation](https://dev.twitch.tv/docs/api) for more information on rate limits and authentication