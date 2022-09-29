import os

def print_env(env):
    """This method displays the environment variables"""
        for k, v in env.items():
        print("%s: %s" % (k, v))

if __name__ == "__main__":
    print('ENV variables:')
    print("---")
    print_env(os.environ)
