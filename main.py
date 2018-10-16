import cv2
import time
import play
import cfg

def main():

    cfg.config()
    play.play()

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()