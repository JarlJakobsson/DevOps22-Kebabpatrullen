# test te load and save functions
from SaveLoad import Load, Save


# Create a new save with 10 names
def make_list():
    for i in range(10):
        Save(f"Name{i}", f"Character{i}", f"Score{i*50}").save_data()


def load_name(name):
    load = Load(name)
    load.load_data()
    print(load.name)
    print(load.character)
    print(load.score)


def main():
    # make_list()
    load_name("Name")


if __name__ == "__main__":
    main()
