import matplotlib.pyplot as plt
import numpy as np

# import npz results
results = np.load("reb-6d-80k-gCorr.npz")

def plot_times(results):
    plt.figure()
    xs = results['Nsample']
    r = results['MAE_kNN_Abr'].shape[0]
    print("r is ", r)
    m = np.mean(results['time_kNN_Abr'],axis=0)
    s = np.std(results['time_kNN_Abr'],axis=0)/np.sqrt(r)
    plt.plot(xs, m, label="kNN-Abr")
    plt.fill_between(xs, m-s, m+s, alpha=0.5)
    m = np.mean(results['time_kNN_Zhao'],axis=0)
    s = np.std(results['time_kNN_Zhao'],axis=0)/np.sqrt(r)
    plt.plot(xs, m, label="kNN-Zhao")
    plt.fill_between(xs, m-s, m+s, alpha=0.5)
    m = np.mean(results['time_kstarNN'],axis=0)
    s = np.std(results['time_kstarNN'],axis=0)/np.sqrt(r)
    plt.plot(xs, m, label="kstarNN")
    plt.fill_between(xs, m-s, m+s, alpha=0.5)
    m = np.mean(results['time_GKDE_Sil'],axis=0)
    s = np.std(results['time_GKDE_Sil'],axis=0)/np.sqrt(r)
    plt.plot(xs, m, label="GKDE-Sil")
    plt.fill_between(xs, m-s, m+s, alpha=0.5)
    m = np.mean(results['time_PAk'],axis=0)
    s = np.std(results['time_PAk'],axis=0)/np.sqrt(r)
    plt.plot(xs, m, label="PAk")
    plt.fill_between(xs, m-s, m+s, alpha=0.5)
    m = np.mean(results['time_BMTI'],axis=0)
    s = np.std(results['time_BMTI'],axis=0)/np.sqrt(r)
    plt.plot(xs, m, label="BMTI")
    plt.fill_between(xs, m-s, m+s, alpha=0.5)
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.xlabel("Nsample")
    plt.ylabel("time (s)")
    plt.title("6d-80k-gCorr")
    plt.savefig("plots/reb-times-6d-80k-gCorr.png")
    plt.show()



def plot_MAEs(results):
    plt.figure()
    xs = results['Nsample']
    r = results['MAE_kNN_Abr'].shape[0]

    m = np.mean(results['MAE_kNN_Abr'],axis=0)
    s = np.std(results['MAE_kNN_Abr'],axis=0)/np.sqrt(r)
    plt.plot(xs, m, label="kNN-Abr")
    plt.fill_between(xs, m-s, m+s, alpha=0.5)
    m = np.mean(results['MAE_kNN_Zhao'],axis=0)
    s = np.std(results['MAE_kNN_Zhao'],axis=0)/np.sqrt(r)
    plt.plot(xs, m, label="kNN-Zhao")
    plt.fill_between(xs, m-s, m+s, alpha=0.5)
    m = np.mean(results['MAE_kstarNN'],axis=0)
    s = np.std(results['MAE_kstarNN'],axis=0)/np.sqrt(r)
    plt.plot(xs, m, label="kstarNN")
    plt.fill_between(xs, m-s, m+s, alpha=0.5)
    m = np.mean(results['MAE_GKDE_Sil'],axis=0)
    s = np.std(results['MAE_GKDE_Sil'],axis=0)/np.sqrt(r)
    plt.plot(xs, m, label="GKDE-Sil")
    plt.fill_between(xs, m-s, m+s, alpha=0.5)
    m = np.mean(results['MAE_PAk'],axis=0)
    s = np.std(results['MAE_PAk'],axis=0)/np.sqrt(r)
    plt.plot(xs, m, label="PAk")
    plt.fill_between(xs, m-s, m+s, alpha=0.5)
    m = np.mean(results['MAE_BMTI'],axis=0)
    s = np.std(results['MAE_BMTI'],axis=0)/np.sqrt(r)
    plt.plot(xs, m, label="BMTI")
    plt.fill_between(xs, m-s, m+s, alpha=0.5)
    plt.xscale("log")
    plt.legend()
    plt.xlabel("Nsample")
    plt.ylabel("MAE")
    plt.title("6d-80k-gCorr")
    plt.savefig("plots/reb-MAE-6d-80k-gCorr.png")
    plt.show()


plot_times(results)

plot_MAEs(results)