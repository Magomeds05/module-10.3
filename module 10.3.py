import time
import random
import threading


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            value = random.randint(50,100)
            if self.balance >= value and self.lock.locked():
                self.lock.release()
            self.balance += value
            print(f'Пополнение: {value}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            value = random.randint(50,100)
            print(f'Запрос на {value}')
            if value > self.balance:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            else:
                self.balance -= value
                print(f'Снятие: {value}. Баланс: {self.balance}')
                time.sleep(0.001)



bk = Bank()


th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
