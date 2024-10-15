# Memory ADRs:
# https://datacrystal.tcrf.net/wiki/Pok%C3%A9mon_Gold_and_Silver/RAM_map
# Index Number of Pokemons:
# https://bulbapedia.bulbagarden.net/wiki/Index_number
# Index Number of Moves:
# https://bulbapedia.bulbagarden.net/wiki/List_of_moves

# (1 Byte) Number of badges obtained (Johto)
JOHTO_BADGE_COUNT_ADDRESS = 0xD57C

# (1 Byte) Number of badges obtained (Kanto)
KANTO_BADGE_COUNT_ADDRESS = 0xD57D

# (3 Bytes) Current money
MONEY_ADDRESS = 0xD573

# (1 Byte) Pokemon IDs of each team member
POKEMON_IDS_ADDRESSES = [0xDA2A, 0xDA5A, 0xDA8A, 0xDABA, 0xDAEA, 0xDB1A]

# (1 Byte) Number of pokemons in team
TEAM_SIZE_ADDRESS = 0xDA22

# (1 Byte) Pokemon levels of each team member
LEVELS_ADDRESSES = [0xDA49, 0xDA79, 0xDAA9, 0xDAD9, 0xDB09, 0xDB39]

# (2 Bytes) Current Pokemon HPs of each team member
HP_ADDRESSES = [0xDA4C, 0xDA7C, 0xDAAC, 0xDADC, 0xDB0C, 0xDB3C]

# (2 Bytes) Max Pokemon HPs of each team member
MAX_HP_ADDRESSES = [0xDA4E, 0xDA7E, 0xDAAE, 0xDADE, 0xDB0E, 0xDB3E]

# (3 Bytes) Pokemon EXPs of each team member
EXP_ADDRESSES = [0xDA32, 0xDA62, 0xDA92, 0xDAC2, 0xDAF2, 0xDB22]

# (4 Bytes) Pokemon Moves of each team member
MOVE_ADDRESSES = [0xDA2C, 0xDA5C, 0xDA8C, 0xDABC, 0xDAEC, 0xDB1C]

# (4 Bytes) Pokemon PPs of each attack of each team member
PP_ADDRESSES = [0xDA41, 0xDA71, 0xDAA1, 0xDAD1, 0xDB01, 0xDB31]

# (X Bytes) Pokemons owned in the pokedex
POKEDEX_OWNED_START_ADDRESS = 0xDBE4
POKEDEX_OWNED_END_ADDRESS = 0xDC04

# (X Bytes) Pokemons seen in the pokedex
POKEDEX_SEEN_START_ADDRESS = 0xDC04
POKEDEX_SEEN_END_ADDRESS = 0xDC24


# IDs:
# https://github.com/pret/pokegold/blob/master/constants/move_constants.asm
# Max PPs:
# https://pokemondb.net/move/generation/2
MOVES_TO_MAX_PP = {
0x00: 0,    # NO_MOVE
    0x01: 35,   # POUND
    0x02: 25,   # KARATE_CHOP
    0x03: 10,   # DOUBLESLAP
    0x04: 15,   # COMET_PUNCH
    0x05: 20,   # MEGA_PUNCH
    0x06: 20,   # PAY_DAY
    0x07: 15,   # FIRE_PUNCH
    0x08: 15,   # ICE_PUNCH
    0x09: 15,   # THUNDERPUNCH
    0x0A: 35,   # SCRATCH
    0x0B: 30,   # VISE GRIP
    0x0C: 5,    # GUILLOTINE
    0x0D: 10,   # RAZOR_WIND
    0x0E: 20,   # SWORDS_DANCE
    0x0F: 30,   # CUT
    0x10: 35,   # GUST
    0x11: 35,   # WING_ATTACK
    0x12: 20,   # WHIRLWIND
    0x13: 15,   # FLY
    0x14: 20,   # BIND
    0x15: 20,   # SLAM
    0x16: 25,   # VINE_WHIP
    0x17: 20,   # STOMP
    0x18: 30,   # DOUBLE_KICK
    0x19: 5,    # MEGA_KICK
    0x1A: 10,   # JUMP_KICK
    0x1B: 15,   # ROLLING_KICK
    0x1C: 15,   # SAND_ATTACK
    0x1D: 15,   # HEADBUTT
    0x1E: 25,   # HORN_ATTACK
    0x1F: 20,   # FURY_ATTACK
    0x20: 5,    # HORN_DRILL
    0x21: 35,   # TACKLE
    0x22: 15,   # BODY_SLAM
    0x23: 20,   # WRAP
    0x24: 20,   # TAKE_DOWN
    0x25: 10,   # THRASH
    0x26: 15,   # DOUBLE_EDGE
    0x27: 30,   # TAIL_WHIP
    0x28: 35,   # POISON_STING
    0x29: 20,   # TWINEEDLE
    0x2A: 20,   # PIN_MISSILE
    0x2B: 30,   # LEER
    0x2C: 25,   # BITE
    0x2D: 40,   # GROWL
    0x2E: 20,   # ROAR
    0x2F: 15,   # SING
    0x30: 20,   # SUPERSONIC
    0x31: 20,   # SONICBOOM
    0x32: 20,   # DISABLE
    0x33: 30,   # ACID
    0x34: 25,   # EMBER
    0x35: 15,   # FLAMETHROWER
    0x36: 30,   # MIST
    0x37: 25,   # WATER_GUN
    0x38: 5,    # HYDRO_PUMP
    0x39: 15,   # SURF
    0x3A: 10,   # ICE_BEAM
    0x3B: 5,    # BLIZZARD
    0x3C: 20,   # PSYBEAM
    0x3D: 20,   # BUBBLEBEAM
    0x3E: 20,   # AURORA_BEAM
    0x3F: 5,    # HYPER_BEAM
    0x40: 35,   # PECK
    0x41: 20,   # DRILL_PECK
    0x42: 20,   # SUBMISSION
    0x43: 20,   # LOW_KICK
    0x44: 20,   # COUNTER
    0x45: 20,   # SEISMIC_TOSS
    0x46: 15,   # STRENGTH
    0x47: 25,   # ABSORB
    0x48: 15,   # MEGA_DRAIN
    0x49: 10,   # LEECH_SEED
    0x4A: 20,   # GROWTH
    0x4B: 25,   # RAZOR_LEAF
    0x4C: 10,   # SOLARBEAM
    0x4D: 35,   # POISONPOWDER
    0x4E: 30,   # STUN_SPORE
    0x4F: 15,   # SLEEP_POWDER
    0x50: 10,   # PETAL_DANCE
    0x51: 40,   # STRING_SHOT
    0x52: 10,   # DRAGON_RAGE
    0x53: 15,   # FIRE_SPIN
    0x54: 30,   # THUNDERSHOCK
    0x55: 15,   # THUNDERBOLT
    0x56: 20,   # THUNDER_WAVE
    0x57: 10,   # THUNDER
    0x58: 15,   # ROCK_THROW
    0x59: 10,   # EARTHQUAKE
    0x5A: 5,    # FISSURE
    0x5B: 10,   # DIG
    0x5C: 10,   # TOXIC
    0x5D: 25,   # CONFUSION
    0x5E: 10,   # PSYCHIC_M
    0x5F: 20,   # HYPNOSIS
    0x60: 40,   # MEDITATE
    0x61: 30,   # AGILITY
    0x62: 30,   # QUICK_ATTACK
    0x63: 20,   # RAGE
    0x64: 20,   # TELEPORT
    0x65: 15,   # NIGHT_SHADE
    0x66: 10,   # MIMIC
    0x67: 40,   # SCREECH
    0x68: 15,   # DOUBLE_TEAM
    0x69: 5,    # RECOVER
    0x6A: 30,   # HARDEN
    0x6B: 10,   # MINIMIZE
    0x6C: 20,   # SMOKESCREEN
    0x6D: 10,   # CONFUSE_RAY
    0x6E: 40,   # WITHDRAW
    0x6F: 40,   # DEFENSE_CURL
    0x70: 20,   # BARRIER
    0x71: 30,   # LIGHT_SCREEN
    0x72: 30,   # HAZE
    0x73: 20,   # REFLECT
    0x74: 30,   # FOCUS_ENERGY
    0x75: 10,   # BIDE
    0x76: 10,   # METRONOME
    0x77: 20,   # MIRROR_MOVE
    0x78: 5,    # SELFDESTRUCT
    0x79: 10,   # EGG_BOMB
    0x7A: 30,   # LICK
    0x7B: 20,   # SMOG
    0x7C: 20,   # SLUDGE
    0x7D: 20,   # BONE_CLUB
    0x7E: 5,    # FIRE_BLAST
    0x7F: 15,   # WATERFALL
    0x80: 15,   # CLAMP
    0x81: 20,   # SWIFT
    0x82: 10,   # SKULL_BASH
    0x83: 15,   # SPIKE_CANNON
    0x84: 35,   # CONSTRICT
    0x85: 20,   # AMNESIA
    0x86: 15,   # KINESIS
    0x87: 5,    # SOFTBOILED
    0x88: 10,   # HIGH_JUMP_KICK
    0x89: 30,   # GLARE
    0x8A: 15,   # DREAM_EATER
    0x8B: 40,   # POISON_GAS
    0x8C: 20,   # BARRAGE
    0x8D: 15,   # LEECH_LIFE
    0x8E: 10,   # LOVELY_KISS
    0x8F: 5,    # SKY_ATTACK
    0x90: 10,   # TRANSFORM
    0x91: 30,   # BUBBLE
    0x92: 10,   # DIZZY_PUNCH
    0x93: 15,   # SPORE
    0x94: 20,   # FLASH
    0x95: 15,   # PSYWAVE
    0x96: 40,   # SPLASH
    0x97: 20,   # ACID_ARMOR
    0x98: 10,   # CRABHAMMER
    0x99: 5,    # EXPLOSION
    0x9A: 15,   # FURY_SWIPES
    0x9B: 10,   # BONEMERANG
    0x9C: 5,    # REST
    0x9D: 10,   # ROCK_SLIDE
    0x9E: 15,   # HYPER_FANG
    0x9F: 30,   # SHARPEN
    0xA0: 30,   # CONVERSION
    0xA1: 10,   # TRI_ATTACK
    0xA2: 10,   # SUPER_FANG
    0xA3: 20,   # SLASH
    0xA4: 10,   # SUBSTITUTE
    0xA5: 0,    # STRUGGLE
    0xA6: 1,    # SKETCH
    0xA7: 10,   # TRIPLE_KICK
    0xA8: 25,   # THIEF
    0xA9: 10,   # SPIDER_WEB
    0xAA: 5,    # MIND_READER
    0xAB: 15,   # NIGHTMARE
    0xAC: 25,   # FLAME_WHEEL
    0xAD: 15,   # SNORE
    0xAE: 10,   # CURSE
    0xAF: 15,   # FLAIL
    0xB0: 30,   # CONVERSION_2
    0xB1: 5,    # AEROBLAST
    0xB2: 40,   # COTTON_SPORE
    0xB3: 15,   # REVERSAL
    0xB4: 10,   # SPITE
    0xB5: 25,   # POWDER_SNOW
    0xB6: 10,   # PROTECT
    0xB7: 30,   # MACH_PUNCH
    0xB8: 10,   # SCARY_FACE
    0xB9: 20,   # FEINT_ATTACK
    0xBA: 10,   # SWEET_KISS
    0xBB: 10,   # BELLY_DRUM
    0xBC: 10,   # SLUDGE_BOMB
    0xBD: 10,   # MUD_SLAP
    0xBE: 10,   # OCTAZOOKA
    0xBF: 20,   # SPIKES
    0xC0: 5,    # ZAP_CANNON
    0xC1: 40,   # FORESIGHT
    0xC2: 5,    # DESTINY_BOND
    0xC3: 5,    # PERISH_SONG
    0xC4: 15,   # ICY_WIND
    0xC5: 5,    # DETECT
    0xC6: 10,   # BONE_RUSH
    0xC7: 5,    # LOCK_ON
    0xC8: 10,   # OUTRAGE
    0xC9: 10,   # SANDSTORM
    0xCA: 10,   # GIGA_DRAIN
    0xCB: 10,   # ENDURE
    0xCC: 20,   # CHARM
    0xCD: 20,   # ROLLOUT
    0xCE: 40,   # FALSE_SWIPE
    0xCF: 15,   # SWAGGER
    0xD0: 5,    # MILK_DRINK
    0xD1: 20,   # SPARK
    0xD2: 20,   # FURY_CUTTER
    0xD3: 25,   # STEEL_WING
    0xD4: 5,    # MEAN_LOOK
    0xD5: 15,   # ATTRACT
    0xD6: 10,   # SLEEP_TALK
    0xD7: 5,    # HEAL_BELL
    0xD8: 20,   # RETURN
    0xD9: 15,   # PRESENT
    0xDA: 20,   # FRUSTRATION
    0xDB: 25,   # SAFEGUARD
    0xDC: 20,   # PAIN_SPLIT
    0xDD: 5,    # SACRED_FIRE
    0xDE: 30,   # MAGNITUDE
    0xDF: 5,    # DYNAMICPUNCH
    0xE0: 10,   # MEGAHORN
    0xE1: 20,   # DRAGONBREATH
    0xE2: 40,   # BATON_PASS
    0xE3: 5,    # ENCORE
    0xE4: 20,   # PURSUIT
    0xE5: 40,   # RAPID_SPIN
    0xE6: 20,   # SWEET_SCENT
    0xE7: 15,   # IRON_TAIL
    0xE8: 35,   # METAL_CLAW
    0xE9: 10,   # VITAL_THROW
    0xEA: 5,    # MORNING_SUN
    0xEB: 5,    # SYNTHESIS
    0xEC: 5,    # MOONLIGHT
    0xED: 15,   # HIDDEN_POWER
    0xEE: 5,    # CROSS_CHOP
    0xEF: 20,   # TWISTER
    0xF0: 5,    # RAIN_DANCE
    0xF1: 5,    # SUNNY_DAY
    0xF2: 15,   # CRUNCH
    0xF3: 20,   # MIRROR_COAT
    0xF4: 10,   # PSYCH_UP
    0xF5: 5,    # EXTREMESPEED
    0xF6: 5,    # ANCIENTPOWER
    0xF7: 15,   # SHADOW_BALL
    0xF8: 10,   # FUTURE_SIGHT
    0xF9: 15,   # ROCK_SMASH
    0xFA: 15,   # WHIRLPOOL
    0xFB: 10,   # BEAT_UP
}
