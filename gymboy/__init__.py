"""GymBoy: A library for creating and registering PyBoy environments as Gym environments."""

from gymboy import registration

make = registration.make
registered_envs = registration.registered_envs


__all__ = ["make", "registered_envs"]
