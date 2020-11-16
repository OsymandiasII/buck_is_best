
import random


def get_fact(factor):
    if factor == 1:
        return 100
    else:
        return 1000 / factor

def results(grp_list):
    end_result = []
    while len(grp_list) > 0:
        num = random.randint(0, len(grp_list))
        end_result.append(grp_list.pop(num-1))
    return end_result

def stats(list_of_res, grp_list, factor):
    end_stats = []
    n_positions = len(grp_list)
    n_runs = len(list_of_res)
    for grp in grp_list:
        l = [str(grp)]
        for position in range(0, n_positions):
            value = 0
            for event in list_of_res:
                if (event[position] == grp):
                    value += 1
            p = value/n_positions * factor

            l.append(str(round(p,2)) + "%")
        end_stats.append(l)
    return end_stats

def pretty_print(grp_list, end_stats ):
    l = len(grp_list)
    max_len = -1
    # find longuest elem in grp_list - to pretty print after
    for elem in grp_list:
        if len(elem) > max_len:
            max_len = len(elem)
    # display results nicely
    for line in end_stats:
        elem = ""
        for i in range(0, l + 1):
            if i == 0:
                space_numbers = max_len - len(line[i])
                elem += str(line[i]) + " " * space_numbers +" | "
            else:
                space_numbers = 6 - len(line[i])
                elem += str(line[i]) + " " * space_numbers +" | "
        print(elem)
    return 0

def not_usefull():
    print("-------------------------------------------------")
    print("-                    WELCOME                    -")
    print("-     If you want to find the TRUE order of     -")
    print("-  the groups for the next event, this program  -")
    print("-                    IS FOR YOU                 -")
    print("-------------------------------------------------")

if __name__ == "__main__":
    not_usefull()
    print("[STARTING]")
    grp_list = ["Lumos", "Patronus", "Vif d'or", "Horcruxes", "Buck", "Nymbus 2000", "Felix Felicis", "Leviosa", "L'ordre du phoenix", "Magyars"]

    inp = input("Do you want a TRUE random list of group (Y/n) : ")
    if inp == "Y" or inp == "y" or inp == "":
        res = results(grp_list.copy())
        print(res)
        print("The truth has been spoken")
        exit(0)
    else:
        inp = input("Do you want TRUE stats about the chances of being selected (Y/n) : ")
        if inp == "Y" or inp == "y" or inp == "":
            val  = input("Enter your value (must be 1 or more): ")
            end_res = []
            try:
                factor = int(val)
                if factor < 1:
                    print("I said 1 or more, are you stoopid or something ?")
                    exit(0)
                for i in range(factor):                  # number of runs
                    res = results(grp_list.copy())      # get a set a random ordered groups
                    print("-> " + str(i), end='\r')
                    end_res.append(res)
                print("", end='\r')
                print("[DONE]")
                print("[PRETTY PRINTING]")
                fact = get_fact(factor)
                end_stats = stats(end_res, grp_list, fact)    # get matrix of groups positions percentages
                l = len(grp_list)
                pretty_print(grp_list, end_stats)
                exit(0)
            except ValueError:
                print("That's not even a number, dumbass")
                exit(1)
        else:
            print("You don't know what you want or what...")
            exit(0)
