#system
import argparse
import os
#project
import DriveToNetwork
from Config import Windows as Config

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--actual", "-a", action="store_true", default=False)

    args = parser.parse_args()

    print("Transfering Photos (Windows Edition!)")

    DriveToNetwork.Transfer(Config["Cameras"], Config["RemotePath"], Config["RemoteRawPath"], actual=args.actual)
