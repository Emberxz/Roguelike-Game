#!/usr/bin/env python3
import tcod

def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2) # Player start position( middle of the screen)
    player_y = int(screen_height / 2) # Player start position( middle of the screen)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="AJ's Roguelike", # Game title
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")#<-order F flips the [y][x] indexing to [x][y]
        while True: # Main game loop
            root_console.print(x=player_x, y=player_y  , string="@")
    
            context.present(root_console)

            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()

if __name__ == "__main__":
    main()