from Map import Map

# Kind of stupid but playing around i noticed
# if i wrote like the following code i clear the coverage.
# Now is this a test or not?

map = Map()

map.print_map()

map.mark_player_position((0, 0))

map.print_map()

map.mark_visited_room((0, 1))

map.print_map()

map.mark_player_leave_room()

map.print_map()

map.move_player((0, 1))

map.print_map()

map.mark_player_position((0, 1))
