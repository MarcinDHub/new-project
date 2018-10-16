import cv2
from PIL import ImageGrab
import numpy
import cfg
import os
from array import array
import pytesseract
import classes


def screen_capture(x, y, w, h):
    screen = ImageGrab.grab(bbox=(x, y, w, h))
    screen = numpy.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

    return screen


def read_numbers(screen, x, y, w, h, mask):
    number = -1
    tmp_img = screen[y: (y + h), x: (x+w)]
    tmp_img = cv2.inRange(tmp_img, mask, mask)
    number = pytesseract.image_to_string(tmp_img, config='--psm 6')

    return number


def stacks(screen):
    tmp_img = screen[cfg.pos_1_y: (cfg.pos_1_y + cfg.pos_size_y), cfg.pos_1_x: (cfg.pos_1_x + cfg.pos_size_x)]
    tmp_img = cv2.inRange(tmp_img, (150, 0, 150), (255, 0, 255))
    stack_p1 = pytesseract.image_to_string(tmp_img, config='--psm 6')

    tmp_img = screen[cfg.pos_2_y: (cfg.pos_2_y + cfg.pos_size_y), cfg.pos_2_x: (cfg.pos_2_x + cfg.pos_size_x)]
    tmp_img = cv2.inRange(tmp_img, (150, 0, 150), (255, 0, 255))
    stack_p2 = pytesseract.image_to_string(tmp_img, config='--psm 6')

    tmp_img = screen[cfg.pos_h_y: (cfg.pos_h_y + cfg.pos_size_y), cfg.pos_h_x: (cfg.pos_h_x + cfg.pos_size_x)]
    tmp_img = cv2.inRange(tmp_img, (150, 0, 150), (255, 0, 255))
    stack_hero = pytesseract.image_to_string(tmp_img, config='--psm 6')

    return stack_p1, stack_p2, stack_hero


def is_player(screen):
    is_hero = is_pixel(screen, cfg.hero_pixel_x, cfg.hero_pixel_y, (255, 0, 0))
    is_p1 = is_pixel(screen, cfg.p1_pixel_x, cfg.p1_pixel_y, (255, 0, 0))
    is_p2 = is_pixel(screen, cfg.p2_pixel_x, cfg.p2_pixel_y, (255, 0, 0))

    return is_hero, is_p1, is_p2


def hero_turn(screen):
    if is_pixel(screen, cfg.fold_pixel_x, cfg.fold_pixel_y, (0, 255, 255)):
        return True

    if is_pixel(screen, cfg.call_pixel_x, cfg.call_pixel_y, (0, 0, 255)):
        return True

    if is_pixel(screen, cfg.bet_pixel_x, cfg.bet_pixel_y, (255, 0, 0)):
        return True

    else:
        return False


def is_pixel(screen, x, y, template):
    pixel_color = screen[y, x]

    if ((pixel_color[0] == template[2]) & (pixel_color[1] == template[1]) & (pixel_color[2] == template[0])):
        screen[y, x] = (0, 0, 0)
        return True

    else:
        return False


# Read dealer position
def dealer(screen):
    if is_pixel(screen, cfg.hero_dealer_x, cfg.hero_dealer_y, (0, 0, 255)):
        return 'Hero'

    elif is_pixel(screen, cfg.p1_dealer_x, cfg.p1_dealer_y, (0, 0, 255)):
        return 'P1'

    elif is_pixel(screen, cfg.p2_dealer_x, cfg.p2_dealer_y, (0, 0, 255)):
        return 'P2'

    else:
        return '?'


# Counts opponents
def count_opponents(is_p1, is_p2):
    quantity = 0

    if is_p1: quantity += 1
    if is_p2: quantity += 1

    return quantity


# Read cards on board
def get_board(screen, x, y, w, h, folder):
    quantity = 0
    tmp_screen = screen[y : (y + h),x : (x + w)]
    board = classes.Board()

    cv2.rectangle(screen, (x,y), (x+w,y+h), (255,255,255), 1)
    for file in os.listdir('{}/'.format(folder)):
        counter, vertexes = compare_images(tmp_screen, '{}/{}'.format(folder, file))

        for item in vertexes:
            cv2.rectangle(screen, (x + item[0], y + item[1]), (x + item[0] + 20, y + item[1] + 40), (0, 0, 255), 1)
            counter += 1

            for i in range(0, 5):
                if board.board[i] == 0:
                    board.board[i] = file[0:2]
                    break
        quantity += counter

    if quantity == 0:
        street = 'preflop'
    elif quantity == 3:
        street = 'flop'
    elif quantity == 4:
        street = 'turn'
    elif quantity == 5:
        street = 'river'
    else:
        street = 'error'

    return board.board, street


def player_cards(screen, x, y, w, h, folder):
    quantity = 0
    tmp_screen = screen[y: (y + h), x: (x + w)]
    list_hero = [None, None]

    for file in os.listdir('{}/'.format(folder)):
        counter, vertexes = compare_images(tmp_screen, '{}/{}'.format(folder, file))
        quantity += counter

        for item in vertexes:
            cv2.rectangle(screen, (x + item[0], y + item[1]), (x + item[0] + 20, y + item[1] + 40), (0, 0, 255), 2)
            counter += 1

            for i in range(0, 2):
                if list_hero[i] is None:
                    list_hero[i] = str(file[0:2])
                    break

    cv2.rectangle(screen, (x, y), (x + w, y + h), (0, 255, 0), 1)

    if (list_hero[0] is not None) & (list_hero[1] is not None):
        return list_hero

    else:
        return None


def hand_value(hand):

    pf_hand_value = ['X', 'X', 'x']
    pf_hand_value[0] = hand[0][0]
    pf_hand_value[1] = hand[1][0]
    if hand[0][1] == hand[1][1]:
        pf_hand_value[2] = 's'
    else:
        pf_hand_value[2] = 'o'

    return pf_hand_value


def compare_images(screen, image_to_compare):

    screen_tmp = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image_to_compare, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(screen_tmp, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.99
    counter = 0
    loc = numpy.where(res >= threshold)

    vertexes = zip(*loc[::-1])

    return counter, vertexes
