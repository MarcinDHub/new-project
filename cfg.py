from configparser import ConfigParser

def config():
    config = ConfigParser()
    config.read('cfg.ini')

    # Window position and size
    window_x = config.getint('Window', 'window x')
    window_y = config.getint('Window', 'window y')
    window_size_x = config.getint('Window', 'window size x')
    window_size_y = config.getint('Window', 'window size y')

    # Board cards position and size
    board_x = int(config.getint('Board', 'board % X') * window_size_x / 100)
    board_y = int(config.getint('Board', 'board % Y') * window_size_y / 100)
    board_size_x = int(config.getint('Board', 'board % size X') * window_size_x / 100)
    board_size_y = int(config.getint('Board', 'board % size Y') * window_size_y / 100)

    # Hero cards position and size
    hero_cards_x = int(config.getint('Hero', 'cards % X') * window_size_x / 100)
    hero_cards_y = int(config.getint('Hero', 'cards % Y') * window_size_y / 100)
    hero_cards_size_x = int(config.getint('Hero', 'cards % size X') * window_size_x / 100)
    hero_cards_size_y = int(config.getint('Hero', 'cards % size Y') * window_size_y / 100)

    # Hero and players pixel finding
    hero_pixel_x = int(config.getint('Hero', 'hero % pixel X') * window_size_x / 100)
    hero_pixel_y = int(config.getint('Hero', 'hero % pixel Y') * window_size_y / 100)
    p1_pixel_x = int(config.getint('Player 1', 'p1 % pixel X') * window_size_x / 100)
    p1_pixel_y = int(config.getint('Player 1', 'p1 % pixel Y') * window_size_y / 100)
    p2_pixel_x = int(config.getint('Player 2', 'p2 % pixel X') * window_size_x / 100)
    p2_pixel_y = int(config.getint('Player 2', 'p2 % pixel Y') * window_size_y / 100)

    # Dealer pixel finding
    hero_dealer_x = int(config.getint('Hero', 'dealer % pixel X') * window_size_x / 100)
    hero_dealer_y = int(config.getint('Hero', 'dealer % pixel Y') * window_size_y / 100)
    p1_dealer_x = int(config.getint('Player 1', 'dealer % pixel X') * window_size_x / 100)
    p1_dealer_y = int(config.getint('Player 1', 'dealer % pixel Y') * window_size_y / 100)
    p2_dealer_x = int(config.getint('Player 2', 'dealer % pixel X') * window_size_x / 100)
    p2_dealer_y = int(config.getint('Player 2', 'dealer % pixel Y') * window_size_y / 100)

    # Folders
    cards_folder = config.get('Cards', 'folder')

    # Fold button
    fold_x = int(config.getint('Button', 'fold % X') * window_size_x / 100)
    fold_y = int(config.getint('Button', 'fold % Y') * window_size_y / 100)
    fold_size_x = int(config.getint('Button', 'fold % size X') * window_size_x / 100)
    fold_size_y = int(config.getint('Button', 'fold % size Y') * window_size_y / 100)
    fold_pixel_x = int(config.getint('Button', 'fold % pixel X') * window_size_x / 100)
    fold_pixel_y = int(config.getint('Button', 'fold % pixel Y') * window_size_y / 100)


    # Call/check button
    call_x = int(config.getint('Button', 'check % X') * window_size_x / 100)
    call_y = int(config.getint('Button', 'check % Y') * window_size_y / 100)
    call_size_x = int(config.getint('Button', 'check % size X') * window_size_x / 100)
    call_size_y = int(config.getint('Button', 'check % size Y') * window_size_y / 100)
    call_pixel_x = int(config.getint('Button', 'check % pixel X') * window_size_x / 100)
    call_pixel_y = int(config.getint('Button', 'check % pixel Y') * window_size_y / 100)

    # Bet button
    bet_x = int(config.getint('Button', 'bet % X') * window_size_x / 100)
    bet_y = int(config.getint('Button', 'bet % Y') * window_size_y / 100)
    bet_size_x = int(config.getint('Button', 'bet % size X') * window_size_x / 100)
    bet_size_y = int(config.getint('Button', 'bet % size Y') * window_size_y / 100)
    bet_pixel_x = int(config.getint('Button', 'bet % pixel X') * window_size_x / 100)
    bet_pixel_y = int(config.getint('Button', 'bet % pixel Y') * window_size_y / 100)

    # Players position for pytesseract
    pos_size_x = int(config.getint('Positions', 'size % x') * window_size_x / 100)
    pos_size_y = int(config.getint('Positions', 'size % y') * window_size_x / 100)
    pos_p1_x = int(config.getint('Positions', 'p1 % x') * window_size_x / 100)
    pos_p1_y = int(config.getint('Positions', 'p1 % y') * window_size_x / 100)
    pos_p2_x = int(config.getint('Positions', 'p2 % x') * window_size_x / 100)
    pos_p2_y = int(config.getint('Positions', 'p2 % y') * window_size_x / 100)
    pos_h_x = int(config.getint('Positions', 'p3 % x') * window_size_x / 100)
    pos_h_y = int(config.getint('Positions', 'p3 % y') * window_size_x / 100)

    # Pot size
    pot_x = int(config.getint('Bets', 'pot % x') * window_size_x / 100)
    pot_y = int(config.getint('Bets', 'pot % y') * window_size_x / 100)
    pot_size_x = int(config.getint('Bets', 'pot % x size') * window_size_x / 100)
    pot_size_y = int(config.getint('Bets', 'pot % y size') * window_size_x / 100)

    # Make evert variable global.
    globals().update(locals())