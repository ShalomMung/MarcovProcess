import numpy as np
import matplotlib.pyplot as plt

def transition_matrix():
    M = np.zeros((101, 101))

    for i in range(95): # all pktene opp til 94
        M[i+1:i+7, i] = 1 / 6

    M[96:, 95] = 1 / 6
    M[100, 95] = 2 / 6
            
    M[97:, 96] = 1 / 6
    M[100, 96] = 3 / 6
            
    M[98:, 97] = 1 / 6
    M[100, 97] = 4 / 6

    M[99:, 98] = 1 / 6
    M[100, 98] = 5 / 6

    M[100:, 99] = 1
    M[100, 100] = 1

    return M
    
def main_mc():
    m = 100
    N = 50
    p = np.zeros((N+1, m+1))
    p[0, 0] = 1
    M = transition_matrix()

    for i in range(N):
        p[i+1, :] = M @ p[i, :]

    #fig, ax = plt.subplots(2, 2, sharey=True, sharex=True)
    #ax[0, 0].bar(np.arange(m + 1), p[5, :])
    #ax[0, 0].set_title("5 iterasjoner")

    #ax[0, 1].bar(np.arange(m + 1), p[10, :])
    #ax[0, 1].set_title("10 iterasjoner")

    #ax[1, 0].bar(np.arange(m + 1), p[15, :])
    #ax[1, 0].set_title("15 iterasjoner")

    #ax[1, 1].bar(np.arange(m + 1), p[20, :])
    #ax[1, 1].set_title("20 iterasjoner")

    #for axi in ax.flatten():
    #    axi.grid()

    #plt.show()
    

    #kummulative
    fig, ax = plt.subplots()
    ax.step(np.arange(N+1), np.gradient(p[:, -1]))
    ax.grid()
    plt.show()
    
def main():
    N = 1000
    all_throws = np.zeros(N)

    for i in range(N):
        posisjon = 0
        number_throws = 0
        while posisjon < N:
            throw = np.random.randint(1, 7)
            posisjon += throw
            number_throws += 1
        all_throws[i] = number_throws

    fig, ax = plt.subplots()
    ax.hist(all_throws)
    ax.grid()
    plt.show()
    
    print(f"Minimum number of throws: {all_throws.min()}")
    print(f"Maximum number of throws: {all_throws.max()}")
    print(f"Mean number of throws: {all_throws.mean()}")


if __name__ == "__main__":
    #main()
    main_mc()