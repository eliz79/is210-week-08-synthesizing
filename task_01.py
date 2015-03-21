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
    player_matchup = []
    newlist_of_players = list(enumerate(players))
    for first_player in newlist_of_players:
        for second_player in newlist_of_players:
            if first_player[0] < second_player[0]:
                player_matchup.append([(first_player[1]), (second_player[1])])
    return player_matchup
