blocks.onBlockBroken(DEAD_BUSH, function on_block_broken_dead_bush() {
    mobs.give(mobs.target(LOCAL_PLAYER), DEAD_BUSH, 1)
})
player.onDied(function on_on_died() {
    mobs.give(mobs.target(LOCAL_PLAYER), BONE_BLOCK, 10)
})
player.onTravelled(SWIM_LAVA, function on_travelled_swim_lava() {
    mobs.applyEffect(FIRE_RESISTANCE, mobs.target(NEAREST_PLAYER), 600, 255)
})
player.onTravelled(SWIM_WATER, function on_travelled_swim_water() {
    mobs.applyEffect(WATER_BREATHING, mobs.target(LOCAL_PLAYER), 600, 255)
})
player.onItemInteracted(ECHO_SHARD, function on_item_interacted_echo_shard() {
    blocks.place(LAVA, pos(0, 0, 0))
})
blocks.onBlockPlaced(BONE_BLOCK, function on_block_placed_bone() {
    blocks.place(AIR, pos(0, 0, 0))
    blocks.place(AIR, pos(0, 0, 0))
    mobs.give(mobs.target(LOCAL_PLAYER), BONE_BLOCK, 1)
})
player.onTravelled(WALK, function on_travelled_walk() {
    mobs.applyEffect(WATER_BREATHING, mobs.target(LOCAL_PLAYER), 0, 0)
    mobs.applyEffect(FIRE_RESISTANCE, mobs.target(NEAREST_PLAYER), 0, 0)
})
player.onTravelled(FALL, function on_travelled_fall() {
    
})
loops.forever(function on_forever() {
    gameplay.timeSet(gameplay.time(DAY))
    gameplay.setWeather(CLEAR)
    gameplay.setDifficulty(HARD)
    mobs.applyEffect(NIGHT_VISION, mobs.target(LOCAL_PLAYER), 600, 255)
    mobs.applyEffect(HEALTH_BOOST, mobs.target(LOCAL_PLAYER), 0, 0)
    mobs.applyEffect(HASTE, mobs.target(LOCAL_PLAYER), 600, 255)
    mobs.applyEffect(STRENGTH, mobs.target(LOCAL_PLAYER), 600, 255)
})
player.onTravelled(SNEAK, function on_travelled_sneak() {
    mobs.spawn(CHICKEN, pos(0, 0, 0))
})
player.onItemInteracted(COAL, function on_item_interacted_coal() {
    player.runChatCommand("/sumon ender_dragon")
})
player.onTravelled(SPRINT, function on_travelled_sprint() {
    mobs.applyEffect(WATER_BREATHING, mobs.target(LOCAL_PLAYER), 0, 0)
    mobs.applyEffect(FIRE_RESISTANCE, mobs.target(NEAREST_PLAYER), 0, 0)
})
player.onItemInteracted(STICK, function on_item_interacted_stick() {
    blocks.place(WATER, pos(0, 0, 0))
})
player.tell(mobs.target(LOCAL_PLAYER), "starting")
mobs.applyEffect(JUMP_BOOST, mobs.target(LOCAL_PLAYER), 0, 0)
mobs.give(mobs.target(LOCAL_PLAYER), BONE_BLOCK, 1)
gameplay.title(mobs.target(LOCAL_PLAYER), "started", "")
