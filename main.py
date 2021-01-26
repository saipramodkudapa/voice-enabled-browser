import speech_recognition as sr
import mac_say
from selenium import webdriver
from helpers import is_valid
from voice_browser import execute_command, show_banner

help_commands = 'HELP:  New Tab, Close Tab, Take Screenshot, Scroll Up/Down, open **, play **, search **, pause/resume, refresh, Maximize/Minimize, On/Off, Page Up'
help_tag = "<span id='help-message' style='font-family:sans-serif; padding:10px; font-size: 20px; background: lightgrey; bottom:0; width:100%; position:fixed; z-index:1; color: slategrey;'>" + help_commands + "</span>"

chrome_path = "user-data-dir=/Users/shruti/Library/Application Support/Google/Chrome/"

if __name__ == "__main__":
    # initialising recognizer
    r = sr.Recognizer()
    r.energy_threshold = 100
    r.dynamic_energy_threshold = False
    should_recognize = True
    # Checking for source
    with sr.Microphone() as source:

        # Default Chrome Options
        options = webdriver.ChromeOptions()
        options.add_argument(chrome_path)
        driver = webdriver.Chrome(options=options)

        # Adding Help Footer on every window
        element_on_page = driver.find_element_by_tag_name('body')
        driver.execute_script("arguments[0].insertAdjacentHTML('afterend', arguments[1]);", element_on_page, help_tag)

        # While loop to always listen
        while True:

            # adjusting to input
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit=2)

            try:
                # Recognising Input
                raw_command = r.recognize_google(audio)
                command = ''.join(raw_command.split()).lower()

                # Check if valid Command
                isCommandValid = is_valid(command)
                print('command is', command)

                # Show banner when activation turned back on
                if should_recognize or (command == 'on'):
                    driver.switch_to.window(driver.window_handles[-1])
                    show_banner(command, driver, isCommandValid)

                # Turn off the Voice Browser
                if command in ['off', 'of']:
                    should_recognize = False
                    print('turned off')
                    mac_say.say('Turned Off')

                # Adding helper Tag
                elif isCommandValid and should_recognize:
                    execute_command(command, driver)
                    # driver.switch_to.window(driver.window_handles[-1])
                    element_on_page = driver.find_element_by_tag_name('body')
                    driver.execute_script("arguments[0].insertAdjacentHTML('afterend', arguments[1]);", element_on_page,
                                          help_tag)
                # Turn on Browser
                elif command in ['on']:
                    should_recognize = True
                    print('turned back on')
                    mac_say.say('Turned Back On')
            except:
                print('Not recognised')
