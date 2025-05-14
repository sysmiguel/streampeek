#!/usr/bin/env bash

browser="firefox"
streams=$(cat)

streamer=$(echo "$streams" | sed 's|https://twitch.tv/[^:]*: ||' | wofi -d menu | cut -d ' ' -f 1 )

[ -z "$streamer" ] && exit 0

if [ "$streams" == "No one is live right now." ]; then
    exit 0
fi

streamer_url=$(echo "$streams" | grep -i -o "https://twitch.tv/[^:]*$streamer[^ ]*" | head -n 1 | sed 's/:$//')

$browser "$streamer_url"
exit 0
