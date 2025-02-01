# Current state of the World

Here is a file that lays out the basics for the current state of the randomizer (as far as I know)

## Settings

All settings not vanilla to Archipelago are assumed to not work.
(I thought they worked but did not test so I was wrong)

### Settings the "Should work"

(Please create an issue if you find they don't):

- progression blancing
- accessibility
- death link
- local items
- non local items
- start inventory
- start hints
- start_location_hints
- exclude_locations
- priority_locations
- item_links
- start_inventory_from_pool

## Client

The client has been given a command `/name` to allow you to change your in-game name upto 16 characters. (This is to be done before connecting to the server)

The client now checks for version numbers of the generate seed and will log a message if the versions do not match. (I can not and do not plan to keep backwards compatiblity for a while as things change so often)

With custom randomizer gci, defeating ganon will trigger the release of the world.

## Locations

With ther being 475 locations in the game there are bound to be mistakes in the data. If you notice a location not triggering please leave a comment on the [Issue thread for it](https://github.com/WritingHusky/Twilight_Princess_apworld/issues/2)

## Generation

When generating the world, all locations possible locations will be created and given an item. Logic is currently static in glitchless, based off the world data from the base randomizer web generator. (If you find logic weridness please make an issue for it)

Newer versions will be focusing on building out the generation process with the implentation of settings and other features.

## Dungeons

Currently dungeons are treated as just another region. This includes keys, which can currently be anywhere. Part of the planned features for the generation update will include key settings.

# Message

Thank you all for spending the time to enjoy this. I would also like to thank every one who has been reporting things for us to fix.

If you feel something is wrong with this file let me know so I can fix it. If it is wrong here then its is highly likely that I don't know about it.
