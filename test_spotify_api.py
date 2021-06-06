from  assertpy import assert_that
from  spotify_api import get_user_playlists_amount

list_amount = 20
assert_that(get_user_playlists_amount("12163032134")).is_equal_to(list_amount)