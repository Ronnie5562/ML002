import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("square", help="Squares a given number", type=int, default=10)
    parser.add_argument("cube", help="Computes the cube of a given number", type=int)
    parser.add_argument(
        "-v", "--verbose", help="Enable verbose output", action="store_true"
    )

    args: argparse.Namespace = parser.parse_args()

    if args.verbose:
        print(f"{args.square} squared is: {args.square ** 2}")
        print(f"{args.cube} cube is: {args.cube ** 3}")
    else:
        print(args.square**2)
        print(args.cube**3)
