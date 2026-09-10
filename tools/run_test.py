import pytest


# This will create host.yaml and custom worlds folder as it uses relative paths
def main():
    test_directories = [
        "worlds\\twilight_princess\\tests",
        "test\\general",
        "test\\multiworld",
        # "test",
        "-s",
    ]

    pytest_args = test_directories

    # Run pytest
    pytest.main(pytest_args)


if __name__ == "__main__":
    main()
