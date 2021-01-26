from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from constants import command_mapping


# Show Command Banner
def show_banner(cmd, a_driver, is_valid_cmd):
    # default styles for valid and invalid commands

    style = "background: #ffd7d2; text-align: center; font-family:sans-serif; font-size: 40px; top:120px; width:100%; position:fixed; z-index:1;"
    style_v = "background: #d4edda; text-align: center; font-family:sans-serif; font-size: 40px; top:120px; width:100%; position:fixed; z-index:1;"

    # If element already existing in window
    try:
        existing = a_driver.find_element_by_id('cmd-message')
        # Check if valid command or not
        if is_valid_cmd:
            # banner command mapping
            mapped_command = command_mapping[cmd]
            # adding space after Play and search commands
            if cmd.startswith('play'):
                mapped_command = 'Play ' + cmd.replace('play', '')
            elif cmd.startswith('search'):
                mapped_command = 'Search ' + cmd.replace('search', '')
            # setting command as an attribute
            a_driver.execute_script("arguments[0].innerHTML = arguments[1];", existing, mapped_command)
            a_driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", existing, style_v)

            sleep(.5)
            # remove banner after showing
            a_driver.execute_script("arguments[0].innerHTML = '';", existing)
        # Command is not valid
        else:
            a_driver.execute_script("arguments[0].innerHTML = arguments[1];", existing, cmd)
            a_driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", existing, style)

            sleep(.5)
            # remove banner after showing
            a_driver.execute_script("arguments[0].innerHTML = '';", existing)

    # If element banner is added for first time in window
    except:
        element = a_driver.find_element_by_tag_name('head')
        # banner command mapping
        if cmd in command_mapping.keys():
            mapped_command = command_mapping[cmd]
        else:
            if cmd.startswith('play'):
                mapped_command = 'Play ' + cmd.replace('play', '')
            elif cmd.startswith('search'):
                mapped_command = 'Search ' + cmd.replace('search', '')
            else:
                mapped_command = cmd
        # style for new banner message

        temp_elm = "<h3 id='cmd-message' style='text-align: center; font-family:sans-serif; font-size: 40px; background: #ffd7d2; top:120px; width:100%; position:fixed; z-index:1;'>" + mapped_command + "</h3> "
        temp_elm_v = "<h3 id='cmd-message' style='text-align: center; font-family:sans-serif;  font-size: 40px; background: #d4edda; top:120px; width:100%; position:fixed; z-index:1;'>" + mapped_command + "</h3> "

        # Check if valid command or not
        if is_valid_cmd:
            a_driver.execute_script("arguments[0].insertAdjacentHTML('afterend', arguments[1]);", element, temp_elm_v)
            sleep(.5)
            # remove banner after showing
            exis_elem = a_driver.find_element_by_id('cmd-message')
            a_driver.execute_script("arguments[0].innerHTML = '';", exis_elem)
        else:
            a_driver.execute_script("arguments[0].insertAdjacentHTML('afterend', arguments[1]);", element, temp_elm)
            sleep(.5)
            # remove banner after showing
            exis_elem = a_driver.find_element_by_id('cmd-message')
            a_driver.execute_script("arguments[0].innerHTML = '';", exis_elem)


def execute_command(command, driver):
    # new tab
    if command == "newtab":
        try:
            # remove banner when new window
            existing = driver.find_element_by_id('cmd-message')
            driver.execute_script("arguments[0].remove();", existing)
        except:
            print('no banner to remove')
        driver.execute_script('''window.open("http://google.com","_blank");''')
        driver.switch_to.window(driver.window_handles[-1])

    # close tab
    elif command == "closetab":
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()

    # take screenshot
    elif command == "takescreenshot":
        print('\a')
        driver.save_screenshot("screenshot.png")

    # close all tabs
    elif command == "closealltabs":
        driver.quit()

    # open sites
    elif command == "openyoutube":
        driver.get('http://youtube.com')
    elif command == "openfacebook":
        driver.get('http://www.facebook.com')
    elif command == "opengmail":
        driver.get('http://www.gmail.com')
    elif command == "opentwitter":
        driver.get('http://www.twitter.com')
    elif command == "openreddit":
        driver.get("http://www.reddit.com")
    elif command == "opennetflix":
        driver.get("http://www.netflix.com")
    elif command == "openamazon":
        driver.get("http://www.amazon.com")

    # search on google
    elif command.startswith('search'):
        query_msg = command.replace('search', '')
        search_url = 'https://www.google.com/search?q=' + query_msg
        driver.get(search_url)

    # play on youtube
    elif command.startswith('play'):
        query_msg = command.replace('play', '')
        wait = WebDriverWait(driver, 3)
        visible = EC.visibility_of_element_located
        search_url = 'https://www.youtube.com/results?search_query=' + query_msg
        driver.get(search_url)
        wait.until(visible((By.ID, "video-title")))
        driver.find_element_by_id("video-title").click()

    # pause
    elif command == 'pause':
        try:
            video = driver.find_element_by_id('movie_player')
            video.send_keys(Keys.SPACE)  # hits space
        except:
            print('no video playing')

    # resume
    elif command == 'resume':
        try:
            video = driver.find_element_by_id('movie_player')
            video.send_keys(Keys.SPACE)  # hits space
        except:
            print('no video paused')

    # maximize
    elif command == 'maximize':
        driver.maximize_window()

    # minimize
    elif command == 'minimize':
        driver.minimize_window()

    # top of page
    elif command == 'pageup':
        height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", height, 0)

    # scroll down
    elif command == 'scrolldown':
        driver.execute_script("window.scrollBy(arguments[0], arguments[1]);", 0, 600)

    # scroll up
    elif command == 'scrollup':
        driver.execute_script("window.scrollBy(arguments[0], arguments[1]);", 0, -600)

    # refresh
    elif command == 'refresh':
        driver.refresh()



