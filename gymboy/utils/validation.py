"""Utilities for ROM checksum validation."""

# Official ROM hashes for the supported environments
SUPPORTED_ROMS = {
    "SUPER MARIOLAND": {
        "md5": "b259feb41811c7e4e1dc200167985c84",
        "sha1": "418203621b887caa090215d97e3f509b79affd3e",
    },
    "KIRBY DREAM LAN": {
        "md5": "a66e4918edcd042ec171a57fe3ce36c3",
        "sha1": "90979baa1d0e24b41b5c304c5ddaf77450692d5a",
    },
    "TETRIS": {
        "md5": "982ed5d2b12a0377eb14bcdc4123744e",
        "sha1": "74591cc9501af93873f9a5d3eb12da12c0723bbc",
    },
    "POKEMON_GLDAAU": {
        "md5": "a6924ce1f9ad2228e1c6580779b23878",
        "sha1": "d8b8a3600a465308c9953dfa04f0081c05bdcb94",
    },
    "POKEMON_SLVAAX": {
        "md5": "2ac166169354e84d0e2d7cf4cb40b312",
        "sha1": "49b163f7e57702bc939d642a18f591de55d92dae",
    },
    "POKEMON YELLOW": {
        "md5": "d9290db87b1f0a23b89f99ee4469e34b",
        "sha1": "cc7d03262ebfaf2f06772c1a480c7d9d5f4a38e1",
    },
    "POKEMON BLUE": {
        "md5": "50927e843568814f7ed45ec4f944bd8b",
        "sha1": "d7037c83e1ae5b39bde3c30787637ba1d4c48ce2",
    },
    "POKEMON RED": {
        "md5": "3d45c1ee9abd5738df46d2bdda8b57dc",
        "sha1": "ea9bcae617fdf159b045185467ae58b2e4a48b9a",
    },
}
