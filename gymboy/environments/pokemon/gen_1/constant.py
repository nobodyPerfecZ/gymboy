# Memory ADRs:
# https://datacrystal.romhacking.net/wiki/Pok%C3%A9mon_Red/Blue:RAM_map
# Memory Values:
# https://github.com/pret/pokered/blob/91dc3c9f9c8fd529bb6e8307b58b96efa0bec67e/constants/event_constants.asm

# (1 Byte) Number of pokemons in team
TEAM_SIZE_ADDRESS = 0xD163

# (1 Byte) Number of badges obtained
BADGE_COUNT_ADDRESS = 0xD356

# (3 Bytes) Current money
MONEY_ADDRESS = 0xD347

# (1 Byte) Pokemon levels of each team member
LEVELS_ADDRESSES = [0xD18C, 0xD1B8, 0xD1E4, 0xD210, 0xD23C, 0xD268]

# (2 Bytes) Current Pokemon HPs of each team member
HP_ADDRESSES = [0xD16C, 0xD198, 0xD1C4, 0xD1F0, 0xD21C, 0xD248]

# (2 Bytes) Max Pokemon HPs of each team member
MAX_HP_ADDRESSES = [0xD18D, 0xD1B9, 0xD1E5, 0xD211, 0xD23D, 0xD269]

# (3 Bytes) Pokemon EXPs of each team member
EXP_ADDRESSES = [0xD179, 0xD1A5, 0xD1D1, 0xD1FD, 0xD229, 0xD255]

# (4 Bytes) Pokemon Moves of each team member
MOVE_ADDRESSES = [0xD173, 0xD19F, 0xD1CB, 0xD1F7, 0xD223, 0xD24F]

# (4 Bytes) Pokemon PPs of each attack of each team member
PP_ADDRESSES = [0xD188, 0xD1B4, 0xD1E0, 0xD20C, 0xD238, 0xD264]

# (X Bytes) Pokemons seen in the pokedex
POKEDEX_SEEN_START_ADDRESS = 0xD30A
POKEDEX_SEEN_END_ADDRESS = 0xD31D

# (X Bytes) Event flags
EVENT_FLAGS_START_ADDRESS = 0xD747
EVENT_FLAGS_END_ADDRESS = 0xD886
MUSEUM_TICKET_ADDRESS = 0xD754


# IDs:
# https://github.com/pret/pokered/blob/91dc3c9f9c8fd529bb6e8307b58b96efa0bec67e/constants/move_constants.asm
# Max PPs:
# https://pokemondb.net/move/generation/1
MOVES_TO_MAX_PP = {
    0x01: 35, # POUND
    0x02: 25, # KARATE_CHOP
    0x03: 10, # DOUBLESLAP
    0x04: 15, # COMET_PUNCH
    0x05: 20, # MEGA_PUNCH
    0x06: 20, # PAY_DAY
    0x07: 15, # FIRE_PUNCH
    0x08: 15, # ICE_PUNCH
    0x09: 15, # THUNDERPUNCH
    0x0a: 35, # SCRATCH
    0x0b: 30, # VISE GRIP
    0x0c: 5,  # GUILLOTINE
    0x0d: 10, # RAZOR_WIND
    0x0e: 20, # SWORDS_DANCE
    0x0f: 30, # CUT
    0x10: 35, # GUST
    0x11: 35, # WING_ATTACK
    0x12: 20, # WHIRLWIND
    0x13: 15, # FLY
    0x14: 20, # BIND
    0x15: 20, # SLAM
    0x16: 25, # VINE_WHIP
    0x17: 20, # STOMP
    0x18: 30, # DOUBLE_KICK
    0x19: 5,  # MEGA_KICK
    0x1a: 10, # JUMP_KICK
    0x1b: 15, # ROLLING_KICK
    0x1c: 15, # SAND_ATTACK
    0x1d: 15, # HEADBUTT
    0x1e: 25, # HORN_ATTACK
    0x1f: 20, # FURY_ATTACK
    0x20: 5,  # HORN_DRILL
    0x21: 35, # TACKLE
    0x22: 15, # BODY_SLAM
    0x23: 20, # WRAP
    0x24: 20, # TAKE_DOWN
    0x25: 10, # THRASH
    0x26: 15, # DOUBLE_EDGE
    0x27: 30, # TAIL_WHIP
    0x28: 35, # POISON_STING
    0x29: 20, # TWINEEDLE
    0x2a: 20, # PIN_MISSILE
    0x2b: 30, # LEER
    0x2c: 25, # BITE
    0x2d: 40, # GROWL
    0x2e: 20, # ROAR
    0x2f: 15, # SING
    0x30: 20, # SUPERSONIC
    0x31: 20, # SONICBOOM
    0x32: 20, # DISABLE
    0x33: 30, # ACID
    0x34: 25, # EMBER
    0x35: 15, # FLAMETHROWER
    0x36: 30, # MIST
    0x37: 25, # WATER_GUN
    0x38: 5,  # HYDRO_PUMP
    0x39: 15, # SURF
    0x3a: 10, # ICE_BEAM
    0x3b: 5,  # BLIZZARD
    0x3c: 20, # PSYBEAM
    0x3d: 20, # BUBBLEBEAM
    0x3e: 20, # AURORA_BEAM
    0x3f: 5,  # HYPER_BEAM
    0x40: 35, # PECK
    0x41: 20, # DRILL_PECK
    0x42: 20, # SUBMISSION
    0x43: 20, # LOW_KICK
    0x44: 20, # COUNTER
    0x45: 20, # SEISMIC_TOSS
    0x46: 15, # STRENGTH
    0x47: 25, # ABSORB
    0x48: 15, # MEGA_DRAIN
    0x49: 10, # LEECH_SEED
    0x4a: 20, # GROWTH
    0x4b: 25, # RAZOR_LEAF
    0x4c: 10, # SOLARBEAM
    0x4d: 35, # POISONPOWDER
    0x4e: 30, # STUN_SPORE
    0x4f: 15, # SLEEP_POWDER
    0x50: 10, # PETAL_DANCE
    0x51: 40, # STRING_SHOT
    0x52: 10, # DRAGON_RAGE
    0x53: 15, # FIRE_SPIN
    0x54: 30, # THUNDERSHOCK
    0x55: 15, # THUNDERBOLT
    0x56: 20, # THUNDER_WAVE
    0x57: 10, # THUNDER
    0x58: 15, # ROCK_THROW
    0x59: 10, # EARTHQUAKE
    0x5a: 5,  # FISSURE
    0x5b: 10, # DIG
    0x5c: 10, # TOXIC
    0x5d: 25, # CONFUSION
    0x5e: 10, # PSYCHIC_M
    0x5f: 20, # HYPNOSIS
    0x60: 40, # MEDITATE
    0x61: 30, # AGILITY
    0x62: 30, # QUICK_ATTACK
    0x63: 20, # RAGE
    0x64: 20, # TELEPORT
    0x65: 15, # NIGHT_SHADE
    0x66: 10, # MIMIC
    0x67: 40, # SCREECH
    0x68: 15, # DOUBLE_TEAM
    0x69: 5,  # RECOVER
    0x6a: 30, # HARDEN
    0x6b: 10, # MINIMIZE
    0x6c: 20, # SMOKESCREEN
    0x6d: 10, # CONFUSE_RAY
    0x6e: 40, # WITHDRAW
    0x6f: 40, # DEFENSE_CURL
    0x70: 20, # BARRIER
    0x71: 30, # LIGHT_SCREEN
    0x72: 30, # HAZE
    0x73: 20, # REFLECT
    0x74: 30, # FOCUS_ENERGY
    0x75: 10, # BIDE
    0x76: 10, # METRONOME
    0x77: 20, # MIRROR_MOVE
    0x78: 5,  # SELFDESTRUCT
    0x79: 10, # EGG_BOMB
    0x7a: 30, # LICK
    0x7b: 20, # SMOG
    0x7c: 20, # SLUDGE
    0x7d: 20, # BONE_CLUB
    0x7e: 5,  # FIRE_BLAST
    0x7f: 15, # WATERFALL
    0x80: 15, # CLAMP
    0x81: 20, # SWIFT
    0x82: 10, # SKULL_BASH
    0x83: 15, # SPIKE_CANNON
    0x84: 35, # CONSTRICT
    0x85: 20, # AMNESIA
    0x86: 15, # KINESIS
    0x87: 5,  # SOFTBOILED
    0x88: 10, # HIGH_JUMP_KICK
    0x89: 30, # GLARE
    0x8a: 15, # DREAM_EATER
    0x8b: 40, # POISON_GAS
    0x8c: 20, # BARRAGE
    0x8d: 10, # LEECH_LIFE
    0x8e: 10, # LOVELY_KISS
    0x8f: 5,  # SKY_ATTACK
    0x90: 10, # TRANSFORM
    0x91: 20, # BUBBLE
    0x92: 10, # DIZZY_PUNCH
    0x93: 15, # SPORE
    0x94: 20, # FLASH
    0x95: 15, # PSYWAVE
    0x96: 40, # SPLASH
    0x97: 20, # ACID_ARMOR
    0x98: 10, # CRABHAMMER
    0x99: 5,  # EXPLOSION
    0x9a: 15, # FURY_SWIPES
    0x9b: 10, # BONEMERANG
    0x9c: 5,  # REST
    0x9d: 10, # ROCK_SLIDE
    0x9e: 15, # HYPER_FANG
    0x9f: 30, # SHARPEN
    0xa0: 30, # CONVERSION
    0xa1: 10, # TRI_ATTACK
    0xa2: 10, # SUPER_FANG
    0xa3: 20, # SLASH
    0xa4: 10, # SUBSTITUTE
}
