# graviterm

A two-body simulation in your terminal!

This project implements a two-body gravity simulation using some basic force equations.


## Example

```bash
$ python3 ncurses-sim.py
```

![](2-body-sim.gif)

## How does it work?

It works by iteratively calculating the position, velocity and acceleration of the individuals bodies at every time-step.

```python
self._updateAcceleration()
self._updateVelocities()
self._updatePositions()
```

First, it updates the x and y components of the acceleration forced experienced by every body as a result of the other bodies's force according to the following formula.

```plain
              mi * mj
Fi =  Σ   ───────────────
     i≠j  |ri - rj + e|^2
```

Acceleration is the change in velocity over time. By updating the acceleration, we can know how much the velocities need to change for the next time step. Hence, the updated acceleration values are used to calculate the new updated velocities.

Finally, the updated velocities are used to calculate the updated positions (x, y) of the bodies.

### Separating simulation and visual display

The core file `simulation.py` is what actually performs the calculations mentioned above. This is separate from the visual displays i.e. `ncurses-sim.py` and `smooth.py` used to render out the bodies onto a screen/terminal. Both of these files use the core `simulation.py` python library to yield positions of the bodies to be rendered onto the screen.

Loosely separated python files allow for anyone to build their own frontend for displaying the data in their own manner