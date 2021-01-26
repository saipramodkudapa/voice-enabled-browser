# voice-enabled-chrome-browser


This file is best viewed in Markdown reader (eg. https://jbt.github.io/markdown-editor/)

# Setup Environment

This project requires python 3.6 or above. Follow these steps to setup your environment:

1.Install google speech recognition library
```
pip install SpeechRecognition
```

2.Install selenium library
```
pip install selenium
```

3.Install mac-say for mac os
```
pip install mac-say
```

# Setup Local Chrome Path

Set chrome_path variable in main.py (line 10) to your local chrome driver path. Example: chrome_path = "user-data-dir=/Users/shruti/Library/Application Support/Google/Chrome/"


# Start Application

The following python script starts the application. A list of supported voice commands are provided below.

```
python main.py
```

```
1. New Tab - Opens a new tab on your browser
2. Close Tab - Closes the current tab.
3. Open “Website” - Opens the homepage for a popular website
   Website - [Youtube, Facebook, Amazon, Reddit, Twitter, Gmail, Netflix]
   Example - Open Youtube
4. Search “query” - Triggers a search query on google
   Example - Search US election results
5. Play “Any video” - Plays the first video on youtube search results page
   Example - Play starboy weeknd
6. Pause/Resume - Pauses/Resumes the Youtube video player
7. Screenshot - Takes a screenshot of the current window and stores the file in browser downloads
8. Maximize - Maximizes the browser window
9. Minimize - Minimizes the current browser window
10. Scroll Up/Down - Scrolls through the current webpage
11. Page up - Navigates to the top of the webpage
12. On/Off - Activates/Deactivates the voice input system
13. Refresh - Reloads the current page
14. Close all Tabs - closes all open tabs.
```

