valid_commands = ['newtab', 'closetab', 'takescreenshot', 'closealltabs', 'openyoutube', 'openfacebook',
                  'openreddit', 'opengmail', 'opentwitter', 'opennetflix', 'openamazon', 'pause', 'resume',
                  'maximize', 'minimize', 'bottom', 'pageup', 'scrollup', 'scrolldown', 'refresh', 'on', 'off',
                  'of']


def is_valid(command):
    """
    Boolean function to check the validity of a command
    :param command: String
    :return: Boolean
    """
    is_predefined = command in valid_commands
    is_search = command.startswith('search')
    is_play = command.startswith('play')
    return is_predefined or is_search or is_play
