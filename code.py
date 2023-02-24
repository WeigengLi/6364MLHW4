import numpy as np

def alpha(A,B,O,pi):
    alpha_matrix=np.zeros((len(O),len(A)))
    for t in range(len(O)):
        for i in range(len(A)):
            if t == 0:
                alpha_matrix[t][i] =pi[i]*B[i][O[t]]
            else:
                for j in range(len(A)):
                    alpha_matrix[t][i] += alpha_matrix[t-1][j]*A[j][i]
                alpha_matrix[t][i] = alpha_matrix[t][i]*B[i][O[t]]
    print(alpha_matrix)
    return alpha_matrix
    
def beta(A,B,O,pi):
    beta_matrix=np.zeros((len(O),len(A)))
    for t in range(len(O)-1,-1,-1):
        for i in range(len(A)):
            if t==len(O)-1:
                beta_matrix[t][i]=1
            else:
                for j in range(len(A)):
                    beta_matrix[t][i] += A[i][j]*B[j][O[t+1]]*beta_matrix[t+1][j]
    print(beta_matrix)
    return beta_matrix

def gamma(alpha_matrix,beta_matrix,A,B,O,pi):
    gamma_matrix = np.zeros((len(O),len(A)))
    prob = round(np.sum(alpha_matrix[len(A)]),6)
    for t in range(len(O)):
        for i in range(len(A)):
            gamma_matrix[t][i]=round(alpha_matrix[t][i]*beta_matrix[t][i]/prob,5)
    print(gamma_matrix)
    return(gamma_matrix)
    

def main():
    A = np.array([[0.7, 0.3], [0.4, 0.6]])
    B = np.array([[0.1, 0.4, 0.5], [0.7, 0.2, 0.1]])
    pi = np.array([0.6,0.4])
    O = np.array([0,2,2])
    alpha_matrix = alpha(A,B,O,pi)
    beta_matrix = beta(A,B,O,pi)
    gamma_matrix = gamma(alpha_matrix,beta_matrix,A,B,O,pi)
    pass


if __name__ == '__main__':
    main()
