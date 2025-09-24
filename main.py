#!/usr/bin/env python3
import tcod

#!/usr/bin/env python3
from pathlib import Path
import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    # Resolve tilesheet path relative to this script
    tilesheet_file = Path(__file__).parent / "dejavu10x10_gs_tc.png"
    if not tilesheet_file.exists():
        raise FileNotFoundError(
            f"Tilesheet not found: {tilesheet_file}\nMake sure dejavu10x10_gs_tc.png is in the Roguelike_Game folder."
        )

    tileset = tcod.tileset.load_tilesheet(
        str(tilesheet_file), 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        player=player,
    )

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    # Create a context and console using the modern tcod API
    with tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="AJ's Roguelike",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")

        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()