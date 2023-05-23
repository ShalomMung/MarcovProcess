import numpy as np
import matplotlib.pyplot as plt

def transition_matrix(m):
    M = np.zeros((m+1, m+1))
    for x in range(m+1):
        if x > 0:
            M[x - 1, x] = 0.5
        if x < m:
            M[x + 1, x] = 0.5

    M[0, 0] = 0.5
    M[-1, -1] = 0.5
    assert np.all(np.isclose(np.sum(M, axis=0), 1.0))
    return M

def main():
    m = 100
    N = 200
    p = np.zeros((N+1, m+1))
    M = transition_matrix(m)
    p[0, m // 2] = 1

    for i in range(N):
        p[i+1, :] = M @ p[i, :]

    fig, ax = plt.subplots(2, 2, sharey=True, sharex=True)
    ax[0, 0].bar(np.arange(m + 1), p[5, :])
    ax[0, 0].set_title("5 iterasjoner")

    ax[0, 1].bar(np.arange(m + 1), p[10, :])
    ax[0, 1].set_title("10 iterasjoner")

    ax[1, 0].bar(np.arange(m + 1), p[20, :])
    ax[1, 0].set_title("20 iterasjoner")

    ax[1, 1].bar(np.arange(m + 1), p[50, :])
    ax[1, 1].set_title("50 iterasjoner")

    xticks = np.linspace(0, 100, 5)
    xtickslabels = np.linspace(-50, 50, 5)
    for axi in ax.flatten():
        axi.grid()
        axi.set_xticks(xticks)
        axi.set_xticklabels(xtickslabels)

    plt.show()

if __name__ == "__main__":
    main()