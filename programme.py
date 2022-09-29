import os

def print_env(env):
for k, v in env.items():
  print("%s: %s" % (k, v))

 """This method displays the environment variables"""
 pass

if __name__ == "__main__":
    print('ENV variables:')
    print("---")
    print_env(os.environ)
