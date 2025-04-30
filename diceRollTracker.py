import matplotlib.pyplot as plt
import random 

FILENAME = "dice_data.txt"

def roll_die():
    return random.randint(1,6)

def read_data():
    try:
        with open(FILENAME,"r") as file:
            return[int(line.strip()) for line in file if line.strip().isdigit()]
    except FileNotFoundError:
        print("No data found yet")
        return[]


def show_histagram(data):
    if not data:
        print ("No roll data shown yet.")
        return

    plt.figure(figsize= (10,6))
    plt.hist(data,bins= range(1,8),edgecolor='black',align='left',rwidth=0.8)
    plt.xticks([1,2,3,4,5,6])
    plt.xlabel("Die Face")
    plt.ylabel("Frequency")
    plt.title("Dice Roll Frequency Histogram")
    plt.grid(True,axis='y',linestyle='--',alpha=.7)
    plt.tight_layout()
    plt.savefig("dice_histogram.png")
    plt.show()
    print("Chart saved as: dice_histogram.png")
def main ():
    while True:
        print("\n Dice Roll Simulator")
        print("1.Roll Die Once")
        print("2.Show Histogram")

        choice = input("Choose an Option (1-5)")
        if choice == "1":
            result = roll_die()
            print (f"You rolled a {result}")
            with open(FILENAME,"a") as file:
                file.write(str(result)+"\n")
        elif choice =="2":
            data= read_data()
            show_histagram(data)
        elif choice =="3":
          result= roll_die()
          print(f"You a {result}")
       
main()