defaults read \\
    ~/Library/Preferences/com.apple.LaunchServices/com.apple.launchservices.secure \\
    | awk -F'\"' '/http;/{print window[(NR)-1]}{window[NR]=$2}
