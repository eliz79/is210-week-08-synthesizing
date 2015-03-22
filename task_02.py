#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" A login requesting password authentication."""

import authentication
import getpass


def login(username, maxattempts):
    """Implementing something that resembles the structure of a login or
    authentication screen.

    Args:
        username(str): A string representing the username.

        maxatempts((int, optional)): An integer representing the maximum number
        of prompted attempts before the function returns False.

    Returns:
        Will returns True if the user has successfully authenticated before
        hitting the maximum number of attempts. Will return False if they
        exceed that maximum number of failed attempts.

    Examples:
        >>> import task_02
        >>> task_02.login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attempts left.
        Please enter your password:
        Incorrect username or password. You have 2 attempts left.
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password. You have 0 attempts left.
        False
    """
    
    authenticated = False
    username = raw_input('What is your username?: ')
    password = getpass.getpass('Please enter your password: ')
    counter = 1
    passwords = []

    while not authenticated:
        if passwords in maxattempts:
            pswrd = maxattempts([passwords]
        if pswrd == ['kindness', 'television', 'greed', 'gum']:
                                authenticated = True
        if not authenticated:
                                print '''Incorrect username or password.
                                         You have {} attempts left.'''
        else:
                                break
                                counter += 1
    return authenticated
