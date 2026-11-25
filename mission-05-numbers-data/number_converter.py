# Number Converter


def main():
    print("=== Decimal to Binary & Hexadecimal Converter ===")
    try:
        user_input = input("Enter a positive decimal number: ").strip()
        decimal_num = int(user_input)

        if decimal_num < 0:
            print("Please enter a positive decimal integer.")
            return

        binary_full = bin(decimal_num)
        binary_raw = binary_full[2:]
        hex_full = hex(decimal_num)
        hex_upper = hex_full[2:].upper()

        print(f"\nResults for decimal {decimal_num}:")
        print(f"  Binary:      {binary_full}  ( {binary_raw})")
        print(f"  Hexadecimal: 0x{hex_upper}  ({hex_upper})")

    except ValueError:
        print("Invalid input! Please enter a valid decimal integer.")


if __name__ == "__main__":
    main()
