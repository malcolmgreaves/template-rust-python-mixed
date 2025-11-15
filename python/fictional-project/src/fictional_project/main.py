__all__: tuple[str, ...] = ("main",)


def main() -> None:
    print("Hello from fictional-project!")


def entrypoint() -> None:
    main()


if __name__ == "__main__":
    main()
