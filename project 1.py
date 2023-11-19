import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
PARTICLE_RADIUS = 0.02
CONTAINER_SIZE = 10.0
NUM_PARTICLES = 100
TEMPERATURE = 300  # in Kelvin

class GasParticle:
    def __init__(self):
        self.x = random.uniform(0, CONTAINER_SIZE)
        self.y = random.uniform(0, CONTAINER_SIZE)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce back if hitting the container walls
        if self.x - PARTICLE_RADIUS < 0 or self.x + PARTICLE_RADIUS > CONTAINER_SIZE:
            self.vx *= -1
        if self.y - PARTICLE_RADIUS < 0 or self.y + PARTICLE_RADIUS > CONTAINER_SIZE:
            self.vy *= -1

# Initialize gas particles
particles = [GasParticle() for _ in range(NUM_PARTICLES)]

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(0, CONTAINER_SIZE)
ax.set_ylim(0, CONTAINER_SIZE)

scatter = ax.scatter([particle.x for particle in particles],
                     [particle.y for particle in particles],
                     s=PARTICLE_RADIUS * 1000, alpha=0.7)

def update(frame):
    for particle in particles:
        particle.move()

    scatter.set_offsets([(particle.x, particle.y) for particle in particles])

ani = animation.FuncAnimation(fig, update, frames=200, interval=50)
plt.show()
