"""GymBoy: A library for creating and registering PyBoy environments as Gym environments."""

from gymboy import registration

make = registration.make
make_vec = registration.make_vec
registered_envs = registration.registered_envs


__all__ = ["make", "make_vec", "registered_envs"]
