import math


def find_nth_prime_number(n: int):
    prime_count, candidate, iteration_count = 0, 2, 0
    previous_percent = -1

    while True:
        if is_prime(candidate):
            prime_count += 1
            if prime_count == n:
                return candidate

        iteration_count += 1
        candidate += 1
        current_percent = int((candidate / n) * 100)

        if current_percent != previous_percent and current_percent in range(0, 101):
            previous_percent = current_percent


def is_prime(number):
    if number % 6 not in [1, 5]:
        return False

    for i in range(5, math.isqrt(number) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


if __name__ == '__main__':
    k = find_nth_prime_number(100)
    print(k)
    print(is_prime(k))

    k = find_nth_prime_number(1000)
    print(k)
    print(is_prime(k))

