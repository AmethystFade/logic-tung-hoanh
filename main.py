from scripts.core.game import Game
from scripts.core.main_scene import MainScene


def main():
    game = Game(initial_scene_factory=MainScene)
    game.run()


if __name__ == "__main__":
    main()
