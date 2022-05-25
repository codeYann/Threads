# Nome: Yan Rodrigues da Silva
# Matrícula: 495532

from inversal import inversal_sort
from regular import regular_sort
from threading import Thread
from time import sleep

import random

main_list = []
for i in range(0, 200):
    random_number = random.randint(0, 999)
    main_list.append(random_number)


def regular_sort_fn():
    print("Starting regular sort in main_list\n")
    sleep(6)
    regular_list = regular_sort(main_list)
    print(regular_list)
    print("\nDone regular thread\n")


def inversal_sort_fn():
    print("Starting inversal sort in main_list\n")
    sleep(4)
    inversal_list = inversal_sort(main_list)
    print(inversal_list)
    print("\nDone inversal thread\n")


if __name__ == "__main__":
    regular_thread = Thread(target=regular_sort_fn)
    inversal_thread = Thread(target=inversal_sort_fn)
    regular_thread.start()
    inversal_thread.start()

    regular_thread.join()
    inversal_thread.join()
