import numpy as np
import matplotlib.pyplot as plt

def transistion_matrix(m):
    M = np.zeros((m+1, m+1))
    for x in range(m+1):
        M[x, x] = 0.5
        if x < m:
            M[x+1, x] = (m - x)/(2 * m)
        if x > 0:
            M[x-1, x] = x/(2 * m)
    assert np.all(np.isclose(np.sum(M, axis=0), 1.0))
    return M

def main_mc():
    N = 100
    m = 20
    p = np.zeros((N+1, m+1)) #sannsynlighet vektor
    M = transistion_matrix(m)
    p[0,0] = 1
    for i in range(N):
        p[i+1, :] = M @ p[i, :]
    
    #fig, ax = plt.subplots()
    #ax.bar(np.arange(m + 1), p[-1])
    #ax.set_xlabel("Tilstand hvor mange baller i venstre urne")
    #ax.set_ylabel(f"Sannsynlighet for å være i tilstand etter {N} iterasjoner")
    #ax.grid()
    #plt.show()

    fig, ax = plt.subplots(2, 2, sharey=True, sharex=True)
    ax[0, 0].bar(np.arange(m + 1), p[5, :])
    ax[0, 0].set_title("5 iterasjoner")

    ax[0, 1].bar(np.arange(m + 1), p[10, :])
    ax[0, 1].set_title("10 iterasjoner")

    ax[1, 0].bar(np.arange(m + 1), p[20, :])
    ax[1, 0].set_title("20 iterasjoner")

    ax[1, 1].bar(np.arange(m + 1), p[50, :])
    ax[1, 1].set_title("50 iterasjoner")

    for axi in ax.flatten():
        axi.grid()

    plt.show()

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
    #main()
    main_mc()