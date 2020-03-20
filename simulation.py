import math

"""
              mi * mj
Fi =  Σ   ───────────────
     i≠j  |ri - rj + e|^2  
"""

class NBodySimulation:
    def __init__(self, w, h, G = 40, dt = 0.05, e = 0.15):
        # Window height x widfh
        self.w = w
        self.h = h
        # Simulation constants
        self.G = G
        self.dt = dt
        self.e = e
        # This list stores masses to be simulated
        self.bodies = []

    # todo: pass in vector and acceleration vectors instead
    def create_body(self, m = 1.0, x = 0.0, y = 0.0, vx = 0.0, vy = 0.0, ax = 0.0, ay = 0.0):
        self.bodies.append({
            "m": m,
            # Displacement
            "x": x,
            "y": y,
            # Velocities
            "vx": vx,
            "vy": vy,
            # Acceleration
            "ax": ax,
            "ay": ay
        })
    
    # # todo: pass in vector and acceleration vectors instead
    # def destroy_body(self):
    #     for body in self.bodies:
    #         if b[x]
    
    def _bleed(self, x, x_max):
        if x < 0:
            return x_max
        elif x > x_max:
            return 1
        return x
    
    def _bounce(self, x, x_max):
        if x < 0:
            return 0
        elif x > x_max:
            return x_max
        return x

    def _updatePositions(self):
        dt = self.dt
        bodies = self.bodies
        for b in bodies:
            x_ = b['x'] + (b['vx'] * dt)
            y_ = b['y'] + (b['vy'] * dt)
            # Bleed positions within boundaries
            b['x'] = x_ # self._bleed(x_, self.w)
            b['y'] = y_ # self._bleed(y_, self.h)


    def _updateAcceleration(self):
        bodies = self.bodies
        G = self.G
        for bi in bodies:
            ax = 0.0
            ay = 0.0
            for bj in bodies:
                if bi != bj:
                    # Update the dx and dy
                    dx = bj['x'] - bi['x']
                    dy = bj['y'] - bi['y']
                    # Calculate radius-radius
                    # distance between the two
                    # bodies
                    d = (dx * dx) + (dy * dy)
                    R = math.pow(d, 0.5)
                    # Calculate force
                    # on the body
                    f = (G * bj['m']) / R
                    # Update individual
                    # acceleration components
                    ax += dx * f
                    ay += dy * f
            # Acceleration on each
            # body is equal to
            # accumulated forces
            # onto each component
            bi['ax'] = ax * self.dt
            bi['ay'] = ay * self.dt
            # uncomment for bounded walls
            # if bi['x'] <= 0 or bi['x'] >= self.w:
            #     bi['ax'] = -bi['ax']
            # if bi['y'] <= 0 or bi['y'] >= self.h:
            #     bi['ay'] = -bi['ay']

    def _updateVelocities(self):
        dt = self.dt
        bodies = self.bodies
        for b in bodies:
            b['vx'] += b['ax'] * dt
            b['vy'] += b['ay'] * dt
            # uncomment for bounded walls
            # if b['x'] <= 0 or b['x'] >= self.w:
            #     b['vx'] = -b['vx']
            # if b['y'] <= 0 or b['y'] >= self.h:
            #     b['vy'] = -b['vy']
    
    def _removeOutOfBounds(self):
        thr = 5000
        bodies = self.bodies
        to_delete = []
        for i in range(len(bodies)):
            body = bodies[i]
            if body['x'] > thr or body['y'] > thr:
                to_delete.append(body)
                print('yeet')
        [bodies.remove(d) for d in to_delete]

    def start(self):
        while True:
            # Update bodies
            self._updateAcceleration()
            self._updateVelocities()
            self._updatePositions()
            
            # # Check bouncing
            # self._updateBouncing()

            # # Remove out of bounds planets
            # self._removeOutOfBounds()
            
            # Yield the coords at each
            # time step that is called
            yield [
                {
                    "x": body['x'],
                    "y": body['y'],
                    "m": body['m'],
                } for body in self.bodies
            ]

if __name__ == '__main__':
    import time
    # Run standalone version
    sim = NBodySimulation(w=50, h=50)
    sim.create_body(x=40, y=11, vx=0.2, vy=-0.1)
    sim.create_body(x=37, y=12, vx=-0.1, vy=0.5)
    for state in sim.start():
        print(state)
        time.sleep(0.005)