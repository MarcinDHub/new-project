import cv2
import window
import cfg
import time
import classes
import decision

def play():

    last_time = time.time()
    last_street = 'blank'
    last_turn = True

    # Main loop
    while True:
        screen = window.screen_capture(cfg.window_x, cfg.window_y, cfg.window_size_x, cfg.window_size_y)
        turn = window.hero_turn(screen)

        # Get data from live screen grabbing
        if turn != last_turn:
            board_info, hero_data, p1_data, p2_data, screen = get_data(screen, last_street)
            last_street = board_info.street
            last_turn = hero_data.turn

        # Calculate decision
        decision.calculate()

        # Execute decision
        # execute(<str>, <int>)
        cv2.imshow('Window', screen)

        fps = round(1 / (time.time() - last_time), 1)
        print('FPS: {} '.format(fps))

        last_turn = turn
        last_time = time.time()



        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        # time.sleep(0.3)


def get_data(screen, last_street):
    # Create class objects
    hero_data = classes.Player()
    p1_data = classes.Player()
    p2_data = classes.Player()
    board_info = classes.Board()

    # Read board
    board_info.board, board_info.street = window.get_board(screen, cfg.board_x, cfg.board_y, cfg.board_size_x, cfg.board_size_y, cfg.cards_folder)
    board_info.pot = window.read_numbers(screen, cfg.pot_x, cfg.pot_y, cfg.pot_size_x, cfg.pot_size_y, (255, 0, 255))

    # Read stack's (pytesseract)
    hero_data.stack = window.read_numbers(screen, cfg.pos_h_x, cfg.pos_h_y, cfg.pos_size_x, cfg.pos_size_y, (255, 0, 255))
    p1_data.stack = window.read_numbers(screen, cfg.pos_p1_x, cfg.pos_p1_y, cfg.pos_size_x, cfg.pos_size_y, (255, 0, 255))
    p2_data.stack = window.read_numbers(screen, cfg.pos_p2_x, cfg.pos_p2_y, cfg.pos_size_x, cfg.pos_size_y, (255, 0, 255))

    hero_data.present, p1_data.present, p2_data.present = window.is_player(screen)
    hero_data.hand = window.player_cards(screen, cfg.hero_cards_x, cfg.hero_cards_y, cfg.hero_cards_size_x, cfg.hero_cards_size_y, cfg.cards_folder)
    hero_data.turn = window.hero_turn(screen)
    hero_data.opponents = window.count_opponents(p1_data.present, p2_data.present)
    board_info.dealer = window.dealer(screen)

    if hero_data.hand is not None:
        hero_data.pf_value = window.hand_value(hero_data.hand)

    cv2.circle(screen, (cfg.p1_pixel_x, cfg.p1_pixel_y), 10, (255, 0, 0))
    cv2.circle(screen, (cfg.p2_pixel_x, cfg.p2_pixel_y), 10, (255, 0, 0))
    cv2.circle(screen, (cfg.hero_pixel_x, cfg.hero_pixel_y), 10, (255, 0, 0))

    print_data(hero_data, board_info, p1_data, p2_data)

    return board_info, hero_data, p1_data, p2_data, screen


# print all recognized data
def print_data(hero_data, board_info, p1_data, p2_data):
    def text(string, x, y):
        cv2.putText(data, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), lineType=cv2.LINE_AA)

    cv2.namedWindow('data')
    cv2.moveWindow('data', 500,700)
    data = cv2.imread('gfx/blank.png')

    # if hero_data.present:
    hero_txt = 'Hero: {} BB'.format(hero_data.stack)
    text(hero_txt, 20, 30)

    # if p1_data.present:
    p1_text = 'P1: {} BB'.format(p1_data.stack)
    text(p1_text, 20, 60)
    # if p2_data.present:
    p2_text = 'P2: {} BB'.format(p2_data.stack)
    text(p2_text, 20, 90)

    opponents_txt = 'Opponents: {}'.format(hero_data.opponents)
    text(opponents_txt, 20, 140)

    deal_txt = 'Dealer: {}'.format(board_info.dealer)
    text(deal_txt, 20, 170)

    street_txt = "Street: {}".format(board_info.street)
    text(street_txt, 20, 200)

    board_txt = "Board: {}".format(board_info.board)
    text(board_txt, 20, 250)

    hand_value_txt = 'Hand value: {}'.format(hero_data.pf_value)
    text(hand_value_txt, 20, 280)

    pot_txt = 'Pot: {}'.format(board_info.pot)
    text(pot_txt, 20, 310)

    cv2.imshow('data', data)


def hand_new_level(last_street, street):
    if last_street != street:
        return True
    else:
        return False



