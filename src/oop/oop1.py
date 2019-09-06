"""
Write classes for the following class hierarchy:

 [Vehicle]->[FlightVehicle]->[Starship]
     |                |
     v                v
[GroundVehicle]      [Airplane]
  |       |
  v       v
[Car]  [Motorcycle]

Each class can simply "pass" for its body. The exercise is about setting up
the hierarchy.

e.g.

class Whatever:
    pass

Put a comment noting which class is the base class
"""

# Base class


class Vehicle:
    def __init__(self):
        pass

    def __repr__(self):
        return type(self).__name__


# Ground vehicles


class GroundVehicle(Vehicle):
    def __init__(self):
        pass

    def __repr__(self):
        return type(self).__name__


class Car(GroundVehicle):
    def __init__(self):
        pass

    def __repr__(self):
        return type(self).__name__


class Motorcycle(GroundVehicle):
    def __init__(self):
        pass

    def __repr__(self):
        return type(self).__name__


# Flight vehicles


class FlightVehicle(Vehicle):
    def __init__(self):
        pass

    def __repr__(self):
        return type(self).__name__


# Aircraft


class Airplane(FlightVehicle):
    def __init__(self):
        pass

    def __repr__(self):
        return type(self).__name__


# Spacecraft


class Starship(FlightVehicle):
    def __init__(self):
        pass

    def __repr__(self):
        return type(self).__name__
