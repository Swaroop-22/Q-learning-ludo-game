import ludopy
import numpy as np
import cv2

g = ludopy.Game()
there_is_winner = False

while not there_is_winner:
    (dice, move_pieces, player_pieces, enemy_pieces, player_is_winner, there_is_winner), player_i = g.get_observation()

    if len(move_pieces):
        piece_to_move = move_pieces[np.random.randint(0, len(move_pieces))]
    else:
        piece_to_move = -1

    _, _, _, _, _, there_is_winner = g.answer_observation(piece_to_move)

    board = g.render_environment()
    cv2.imshow("Ludo Board", board)
    cv2.waitKey(0)  #Press 0 to play next move