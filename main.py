from random import sample

from matplotlib.pyplot import bar, cla, show, gcf, xlabel, ylabel, title
from numpy import arange, array, int_
from numpy.core.fromnumeric import argmin
from numpy.typing import NDArray
from matplotlib.animation import FuncAnimation
from time import sleep

LIST_SIZE = 50

# please do something about these global variables later
itr = 0  # 1 for insertsort, 0 for everything else
itr_bubble = 0
bubble_sorted_count = 0
itr_insert = 1
waiting_for_start_delay = True


def selectsort_step_ints(frame, list: NDArray[int_]):
    global waiting_for_start_delay
    global itr
    last_idx = LIST_SIZE - 1

    cla()
    title("Selection Sort")
    xlabel("Indeks")
    ylabel("Nilai")

    if itr < last_idx:
        min_idx = argmin(list[itr:]) + itr

        bar(arange(start=0, stop=itr), list[:itr], width=1, color="teal")
        bar(
            arange(start=itr, stop=itr + 1),
            list[itr : itr + 1],
            width=1,
            color="orange",
        )
        bar(
            arange(start=itr + 1, stop=min_idx),
            list[itr + 1 : min_idx],
            width=1,
            color="teal",
        )
        bar(
            arange(start=min_idx, stop=min_idx + 1),
            list[min_idx : min_idx + 1],
            width=1,
            color="orange",
        )
        bar(
            arange(start=min_idx + 1, stop=LIST_SIZE),
            list[min_idx + 1 :],
            width=1,
            color="teal",
        )

        list[itr], list[min_idx] = list[min_idx], list[itr]

        print(f"Iter {itr + 1}: {list}")

        itr += 1
    else:
        bar(arange(LIST_SIZE), list, width=1, color="teal")

    if waiting_for_start_delay:
        sleep(1)
        waiting_for_start_delay = False


def bubblesort_step_ints(frame, list: NDArray[int_]):
    global waiting_for_start_delay
    global itr_bubble
    global bubble_sorted_count
    last_idx = LIST_SIZE - 1

    cla()
    title("Bubble Sort")
    xlabel("Indeks")
    ylabel("Nilai")
    bar(arange(start=0, stop=itr_bubble), list[:itr_bubble], width=1, color="teal")

    if bubble_sorted_count < last_idx:
        if itr_bubble < last_idx - bubble_sorted_count:
            bar(
                arange(start=itr_bubble, stop=itr_bubble + 2),
                list[itr_bubble : itr_bubble + 2],
                width=1,
                color="orange",
            )
            bar(
                arange(start=itr_bubble + 2, stop=LIST_SIZE),
                list[itr_bubble + 2 :],
                width=1,
                color="teal",
            )

            if list[itr_bubble] > list[itr_bubble + 1]:
                list[itr_bubble], list[itr_bubble + 1] = (
                    list[itr_bubble + 1],
                    list[itr_bubble],
                )
            itr_bubble += 1
        else:
            bar(
                arange(start=itr_bubble, stop=LIST_SIZE),
                list[itr_bubble:],
                width=1,
                color="teal",
            )

            bubble_sorted_count += 1
            itr_bubble = 0
    else:
        bar(
            arange(start=itr_bubble, stop=LIST_SIZE),
            list[itr_bubble:],
            width=1,
            color="teal",
        )

    if waiting_for_start_delay:
        sleep(1)
        waiting_for_start_delay = False


def insertsort_step_ints(frame, list: NDArray[int_]):
    global itr
    global itr_insert

    cla()
    title("Insertion Sort")
    xlabel("Indeks")
    ylabel("Nilai")

    if itr < LIST_SIZE:
        bar(arange(start=0, stop=itr_insert), list[:itr_insert], width=1, color="teal")
        bar(
            arange(start=itr_insert, stop=itr_insert + 1),
            list[itr_insert : itr_insert + 1],
            width=1,
            color="orange",
        )
        bar(
            arange(start=itr_insert + 1, stop=LIST_SIZE),
            list[itr_insert + 1 :],
            width=1,
            color="teal",
        )

        if itr_insert > 0 and list[itr_insert] < list[itr_insert - 1]:
            list[itr_insert], list[itr_insert - 1] = (
                list[itr_insert - 1],
                list[itr_insert],
            )
            itr_insert -= 1
        else:
            itr += 1
            itr_insert = itr

    else:
        bar(arange(LIST_SIZE), list, width=1, color="teal")


def main():
    random_list = array(sample([num for num in range(1, LIST_SIZE + 1)], k=LIST_SIZE))
    print(random_list)

    animation = FuncAnimation(
        gcf(), bubblesort_step_ints, fargs=[random_list], interval=75
    )
    show()


if __name__ == "__main__":
    main()
