import os

def print_env(env):
    for k, v in env.items():
        print("%s: %s" % (k, v))

if __name__ == "__main__":
    print_env(os.environ)
