import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
g = 9.81  # acceleration due to gravity (m/s^2)
length = 1.0  # length of the pendulum (m)
theta0 = np.radians(45)  # initial angle in radians
omega0 = 0.0  # initial angular velocity (rad/s)
time_step = 0.05  # time step for simulation
duration = 10.0  # duration of the simulation (s)

# Function to calculate angular acceleration
def calculate_angular_acceleration(theta, omega):
    return -g / length * np.sin(theta)

# Function to update the pendulum state
def update_pendulum_state(state, dt):
    theta, omega = state
    alpha = calculate_angular_acceleration(theta, omega)
    omega += alpha * dt
    theta += omega * dt
    return [theta, omega]

# Function to animate the pendulum motion
def animate_pendulum(i, pendulum, line):
    pendulum.state = update_pendulum_state(pendulum.state, time_step)
    x = length * np.sin(pendulum.state[0])
    y = -length * np.cos(pendulum.state[0])
    line.set_data([0, x], [0, y])
    return line,

class Pendulum:
    def __init__(self, initial_state):
        self.state = initial_state

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-length, length)
ax.set_ylim(-length, length)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the pendulum
pendulum = Pendulum([theta0, omega0])

# Create the pendulum line
line, = ax.plot([], [], 'o-', lw=2)

# Set up the animation
ani = animation.FuncAnimation(fig, animate_pendulum, fargs=(pendulum, line),
                              frames=int(duration / time_step), interval=time_step * 1000, blit=True)

plt.show()
