# resources.py

HANDS = ['''
      .-.
   __/ / )
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
''', '''
    .-.  _
    | | / )_
    | |/ // )
   _|__ // //
  / __)-'  /
  \  `.-' /
   > ._>-
  / \/
''', '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
''']

MENU_IMAGE = '''
                      .-.  _             .-.
                      | | / )_           | | / )
       .-.            | |/ // )          | |/ /
    __/ / )          _|__ // //         _|__ /_
    / __)-' )        / __)-'  /         / __)-' )
    \  `(.-')        \  `.-' /          \  `(.-')
    > ._>-'          > ._>-             > ._>-'
    / \/             / \/               / \/   
'''

MENU_OPTIONS_PROMPT = ('Please, choose "1", "2" or "3" (or "q" to quit) ' +
                 'and press "Enter"')

MENU_OPTIONS = ['1', '2', '3', 'quit', 'exit']

SORRY_YES_NO = ('Sorry? \x1b[33m' + 'Y' + '\x1b[0m'+'es or ' + '\x1b[33m' +
         'N'+'\x1b[0m' + 'o')

INTRO = ('\x1b[6;37;41m' + '             ####  JANKENPON  ####' +
         '                  ' + '\x1b[0m' + MENU_IMAGE +
         '\n          ___________________________\n'
         '         |                           |\n'
         '         |    1. You vs. Computer    |\n'
         '         |  2. Computer vs. Computer |\n'
         '         |     3. How to play        |\n'
         '         |___________________________|\n\n' +
         MENU_OPTIONS_PROMPT)

OPPONENT_NAMES = ['Rocky Balboa', 'Edwards Scissorhands', 'Paper Parker',
                  'Joker', 'Bart Simpson']

HOW_TO_PLAY = ('                    ' + '==HOW TO PLAY==\n'
               'One player choses paper, scissors or rock; ' +
               'the other player, too.\n\n'
               'Paper beats rock,\n'
               'scissors beat paper\n,'
               'and rock beats scissors.\n\n'
               'If both choices are of the same kind (eg. "rock vs. rock"),' +
               ' it is a tie.\n\n'
               'After three rounds, the  player who has beaten the opponent' +
               ' the most is the winner.\n'
               '-----------\n'
               'If you want to play against the computer, type 1.\n'
               'If you want to see a match, type 2.\n'
               '-----------\n'
               '                       HINTS\n'
               'There are five kinds of strategies your opponent may use:\n'
               'a. playing randomly;\n'
               'b. imitating your last move' +
               ' (eg. if you chose "paper" at round 1,' +
               ' he will play "paper" at round 2.);\n'
               'c. using all of the three options once;\n'
               'd. always choosing "rock";'
               'e. thinking that you are going to repeat your last move' +
               ' (eg. if you chose "paper" at round 1, ' +
               ' he will play "scissors" at round 2.)\n'
               'But sometimes he has just bad luck and loses all rounds.\n'
               'Discover the strategy your opponent is using to raise' +
               ' your chances of winning!\n'
               'By the way, the same player may use different strategies' +
               ' at different matches.\n'
               'And no, Bart does not always play "rock".\n'
               '==============='
               'CREDITS: Developed by Hugo Tiburtino. ASCII art by VK')