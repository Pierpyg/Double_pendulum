import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp
import random
import os

def main():
    # check that the input is a float and greater than 0
    def get_positive_float(x):
        while True:
            try:
                value = float(input(x))
                if value <= 0:
                    print("Enter a positive number")
                    continue
                return value
            except ValueError:
                print("Enter an integer or a float")

    # check that the input is a float and between -180 and 180
    def get_angle(x):
        while True:
            try:
                value = float(input(x))
                if not -180 <= value <= 180:
                    print("Enter a number between -180 and 180")
                    continue
                return value
            except ValueError:
                print("Enter an integer or a float")

    # check that the number is a float
    def get_number(x):
        while True:
            try:
                value = float(input(x))
                return value
            except ValueError:
                print("Enter a number")

    # initial conditions of two pendulums: lenght, mass, angle and angular speed
    L1 = get_positive_float("What's the lengh of the 1st pendulum: ")
    m1 = get_positive_float("What's the mass of the 1st pendulum: ")
    theta1_init = get_angle("What's the initial angle of the 1st pendulum(between -180 and 180): ")
    omega1_init = get_number(
        "What's the initial angular valocity of the 1st pendulum: "
    )
    L2 = get_positive_float("What's the lengh of the 2nd pendulum: ")
    m2 = get_positive_float("What's the mass of the 2st pendulum: ")
    theta2_init = get_angle("What's the intial angle of the 2nd pendulum(between -180 and 180): ")
    omega2_init = get_number(
        "What's the initial angular velocity of the 2st pendulum: "
    )
    # integrate the equations of motion
    solution = integrate(
        L1, m1, theta1_init, omega1_init, L2, m2, theta2_init, omega2_init
    )

    # create and display the animation
    ani = create_animation(L1, L2, solution)

    # save the animation as GIF in the same directory as the script
    script_dir = os.path.dirname(__file__)
    save_path = os.path.join(script_dir, 'double_pendulum.gif')
    ani.save(save_path, writer='pillow', fps=120)




# function to create the animation
def create_animation(L1, L2, solution):
    # create a new figure and axes for the graph
    fig, ax = plt.subplots()
    # set the axis length
    ax.set_xlim(-(L1 + L2), L1 + L2)
    ax.set_ylim(-(L1 + L2), L1 + L2)
    # set axis aspect ratio to maintain the correct proportion
    ax.set_aspect("equal")
    # add grid
    ax.grid()
    #set title
    ax.set_title("Double Pendulum")
    # create blank lines to represent the pendulums in the graph
    (line1,) = ax.plot(
        [],
        [],
        lw=5,
        color=np.random.rand(
            3,
        ),
    )
    (line2,) = ax.plot(
        [],
        [],
        lw=5,
        color=np.random.rand(
            3,
        ),
    )

    # initialize blank lines in the graph
    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        return line1, line2

    def animate(i):
        # calculation of coordinates of pendulum points
        x1 = L1 * np.sin(solution.y[0, i])
        y1 = -L1 * np.cos(solution.y[0, i])
        x2 = x1 + L2 * np.sin(solution.y[2, i])
        y2 = y1 - L2 * np.cos(solution.y[2, i])
        # update lines with new coordinates
        line1.set_data([0, x1], [0, y1])
        line2.set_data([x1, x2], [y1, y2])
        return line1, line2

    # creation of the animation object
    ani = animation.FuncAnimation(
        # figure on which to view the animation
        fig,
        # function animation
        animate,
        # number of frames to be animated
        frames=solution.y.shape[1],
        # Initialization function
        init_func=init,
        # enable fast rendering
        blit=True,
        # time interval between frames (in milliseconds)
        interval=8.3333,
    )
    #return ani
    # show animation
    plt.show()


def derivate(t, state, L1, m1, L2, m2):
    theta1, omega1, theta2, omega2 = state
    # Earth's gravitational acceleration
    g = 9.81
    # angular acceleration of the 1st pendulum
    alpha1 = (
        -g * (2 * m1 + m2) * np.sin(theta1)
        - m2 * g * np.sin(theta1 - 2 * theta2)
        - 2
        * np.sin(theta1 - theta2)
        * m2
        * (omega2**2 * L2 + omega1**2 * L1 * np.cos(theta1 - theta2))
    ) / (L1 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2)))
    # angular acceleration of the 2nd pendulum
    alpha2 = (
        2
        * np.sin(theta1 - theta2)
        * (
            omega1**2 * L1 * (m1 + m2)
            + g * (m1 + m2) * np.cos(theta1)
            + omega2**2 * L2 * m2 * np.cos(theta1 - theta2)
        )
    ) / (L2 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2)))

    return [omega1, alpha1, omega2, alpha2]


def integrate(L1, m1, theta1_init, omega1_init, L2, m2, theta2_init, omega2_init):
    # creation of the initial state vector
    initial_state = [theta1_init, omega1_init, theta2_init, omega2_init]
    # integration of the equations of motion
    solution = solve_ivp(
        derivate,
        # interval integration time
        (0, 20),
        # initial state
        initial_state,
        # additional arguments for the derivative function
        args=(L1, m1, L2, m2),
        # time values in which to evaluate the solution
        t_eval=np.linspace(0, 16.6, 1000),
    )
    return solution


if __name__ == "__main__":
    main()
