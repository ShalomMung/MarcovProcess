import numpy as np
import matplotlib.pyplot as plt

def main():
    m = 20 # Number of balls
    N = 100
    x = np.zeros(N+1)
    x[0] = 10

    for i in range(N):
        ball_nr = np.random.randint(m)
        if ball_nr < x[i]: # da blir i venstre ulren
            x[i+1] = x[i] - 1
        else:
            x[i+1] = x[i] + 1

    fig, ax = plt.subplots()
    ax.step(np.arange(N+1), x)
    plt.show()

if __name__ == "__main__":
    main()