def on_block_broken_dead_bush():
    mobs.give(mobs.target(LOCAL_PLAYER), DEAD_BUSH, 1)
blocks.on_block_broken(DEAD_BUSH, on_block_broken_dead_bush)

def on_on_died():
    mobs.give(mobs.target(LOCAL_PLAYER), BONE_BLOCK, 10)
player.on_died(on_on_died)

def on_travelled_swim_lava():
    mobs.apply_effect(FIRE_RESISTANCE, mobs.target(NEAREST_PLAYER), 600, 255)
player.on_travelled(SWIM_LAVA, on_travelled_swim_lava)

def on_travelled_swim_water():
    mobs.apply_effect(WATER_BREATHING, mobs.target(LOCAL_PLAYER), 600, 255)
player.on_travelled(SWIM_WATER, on_travelled_swim_water)

def on_item_interacted_echo_shard():
    blocks.place(LAVA, pos(0, 0, 0))
player.on_item_interacted(ECHO_SHARD, on_item_interacted_echo_shard)

def on_block_placed_bone():
    blocks.place(AIR, pos(0, 0, 0))
    blocks.place(AIR, pos(0, 0, 0))
    mobs.give(mobs.target(LOCAL_PLAYER), BONE_BLOCK, 1)
blocks.on_block_placed(BONE_BLOCK, on_block_placed_bone)

def on_travelled_walk():
    mobs.apply_effect(WATER_BREATHING, mobs.target(LOCAL_PLAYER), 0, 0)
    mobs.apply_effect(FIRE_RESISTANCE, mobs.target(NEAREST_PLAYER), 0, 0)
player.on_travelled(WALK, on_travelled_walk)

def on_travelled_fall():
    pass
player.on_travelled(FALL, on_travelled_fall)

def on_forever():
    gameplay.time_set(gameplay.time(DAY))
    gameplay.set_weather(CLEAR)
    gameplay.set_difficulty(HARD)
    mobs.apply_effect(NIGHT_VISION, mobs.target(LOCAL_PLAYER), 600, 255)
    mobs.apply_effect(HEALTH_BOOST, mobs.target(LOCAL_PLAYER), 0, 0)
    mobs.apply_effect(HASTE, mobs.target(LOCAL_PLAYER), 600, 255)
    mobs.apply_effect(STRENGTH, mobs.target(LOCAL_PLAYER), 600, 255)
loops.forever(on_forever)

def on_travelled_sneak():
    mobs.spawn(CHICKEN, pos(0, 0, 0))
player.on_travelled(SNEAK, on_travelled_sneak)

def on_item_interacted_coal():
    player.run_chat_command("/sumon ender_dragon")
player.on_item_interacted(COAL, on_item_interacted_coal)

def on_travelled_sprint():
    mobs.apply_effect(WATER_BREATHING, mobs.target(LOCAL_PLAYER), 0, 0)
    mobs.apply_effect(FIRE_RESISTANCE, mobs.target(NEAREST_PLAYER), 0, 0)
player.on_travelled(SPRINT, on_travelled_sprint)

def on_item_interacted_stick():
    blocks.place(WATER, pos(0, 0, 0))
player.on_item_interacted(STICK, on_item_interacted_stick)

player.tell(mobs.target(LOCAL_PLAYER), "starting")
mobs.apply_effect(JUMP_BOOST, mobs.target(LOCAL_PLAYER), 0, 0)
mobs.give(mobs.target(LOCAL_PLAYER), BONE_BLOCK, 1)
gameplay.title(mobs.target(LOCAL_PLAYER), "started", "")
