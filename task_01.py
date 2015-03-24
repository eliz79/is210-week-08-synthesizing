#! usr/bin/env python
# *-* coding: utf-8 *-*
"""A list of versus matchups for players."""


def get_matches(players):
    """This is a docstring.
    Arg:
        players(list): list of names to produce a new list of unique matchups
                       between players stored as tuples.
    Return:
        A new generated list of tuples.
    Example:
        >>> import task_01
        >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
    """
    player = []
    
    for index1, first_player in enumerate(players):
        for index2, second_player in enumerate(players):
            if index1 < index2:
                new = first_player, second_player
                player.append(players)
                print new
                #return player, new
        
                
            
