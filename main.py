# ---------------------------- Libraries ------------------------------- #
from random import randint
import gmpy2
from sympy import isprime


# ----------------------------- Classes -------------------------------- #
class RsaAttack:

    # Methods

    def factoring_attack(self, e_key_pub: int, n_key_pub: int, enc_message: int) -> int:
        """
        Performs a factoring attack on RSA encrypted message.
        :param e_key_pub: The public key 'e'.
        :param n_key_pub: The public key 'n'.
        :param enc_message: The RSA encrypted message.
        :return: The decrypted message if the factors of 'n' are prime, otherwise -1.
        """

        prim_factors = self.__quadratic_sieve(n_key_pub)

        # Check if the factors are prime
        if self.__miller_rabin(prim_factors[0]) is True and self.__miller_rabin(prim_factors[1]) is True:
            phi = (prim_factors[0] - 1) * (prim_factors[1] - 1)
            d_key_priv = self.__get_invert(e_key_pub, phi)
            dec_message = self.__montgomery_ladder(enc_message, d_key_priv, n_key_pub)

            # Only for university purposes
            print()
            print(f"Prime factors of 'n': {prim_factors}")
            print(f"Phi: {phi}")
            print(f"Private key 'd': {d_key_priv}")

            return dec_message

        else:
            return -1

    @staticmethod
    def __miller_rabin(n, k=1000):
        """
        Miller-Rabin primality test.
        :param n: Number to test.
        :param k: Number of iterations.
        :return: True if n is prime, False otherwise.
        """
        # Variables
        d = n - 1
        s = 0

        # Body
        while d % 2 == 0:
            d //= 2
            s += 1

        for _ in range(k):
            a = randint(2, n - 1)
            x = pow(a, d, n)

            if x == 1 or x == n - 1:
                continue

            for _ in range(s - 1):
                x = pow(x, 2, n)

                if x == n - 1:
                    break

            else:
                return False

        return True

    @staticmethod
    def __quadratic_sieve(n: int) -> list[int]:
        """
        Function to perform the quadratic sieve algorithm.
        :param int n: The number to factorize.
        :return: The factors of the number.
        """

        if isprime(n):
            return [n]

        # Step 1: Find a square root of n
        x = gmpy2.isqrt(n) + 1

        # Step 2: Find a perfect square congruent to n modulo x
        while True:
            y2 = gmpy2.powmod(x, 2, n)
            y = gmpy2.isqrt(y2)

            if y * y == y2:
                break

            x += 1

        # Step 3: Find the factors of n
        p = gmpy2.gcd(x - y, n)
        q = gmpy2.gcd(x + y, n)

        return [int(p), int(q)]

    @staticmethod
    def __get_invert(num: int, mod: int) -> int:
        """
        Calculates the modular multiplicative inverse of a number.
        :param num: The number to find the inverse of.
        :param mod: The modulo.
        :return: The modular multiplicative inverse of 'num' modulo 'mod'. If the inverse does not exist, the function returns -1.
        """

        m = mod
        x = 0
        y = 1
        x_prev, y_prev = 1, 0

        while m != 0:
            quotient = num // m
            num, m = m, num % m
            x, x_prev = x_prev - quotient * x, x
            y, y_prev = y_prev - quotient * y, y

        return x_prev % mod

    @staticmethod
    def __montgomery_ladder(base: int, exponent: int, modulo: int) -> int:
        """
        Perform the Montgomery Ladder algorithm.
        :param int base: The base number for the calculation.
        :param int exponent: The exponent for the calculation.
        :param int modulo: The modulo for the calculation.
        :return: The result of the Montgomery Ladder calculation.
        """

        x = 1
        y = base % modulo
        exponent_in_bit = bin(exponent)[2:]

        for bit in exponent_in_bit:
            if bit == "1":
                x = (x * y) % modulo
                y = (y ** 2) % modulo
            else:
                y = (x * y) % modulo
                x = (x ** 2) % modulo

        return x


# ---------------------------- Functions ------------------------------- #

def validate_user_input(prompt: str) -> int:
    """
    Validate the user input.
    :param str prompt: The prompt message to display to the user.
    :return: The validated integer input from the user.
    """

    while True:
        user_input = input(prompt)

        try:
            value = int(user_input)

            if value <= 0:
                raise ValueError("Invalid Input: Please enter a positive number.")
            break

        except ValueError:
            print("Invalid Input: Please enter a positiv number.")

    return value


def main():
    """
    Main function of the program.
    :return: None
    """

    print()

    # Variables
    attack = RsaAttack()
    e_key_pub = validate_user_input("Enter the public key 'e': ")
    n_key_pub = validate_user_input("Enter the public key 'n': ")
    enc_message = validate_user_input("Enter the encrypted message: ")

    # Body
    dec_message = attack.factoring_attack(e_key_pub, n_key_pub, enc_message)
    print("-" * 50)
    print(f"The decrypted message is: {dec_message}")


# ------------------------------ Main ---------------------------------- #

if __name__ == "__main__":
    main()
