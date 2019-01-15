from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcHgbz05lUncghNqwkZuIklc9WT1dg98JQaUaA3dEwOcE2lFe4VreNX1LY4xFoATVmFoeKYxjCCfh-b8JTtVP8C4p3IH4Iz3eFbOSVyRql7LHNV9H1O2hYNH9ndFt9HtyUQd1-cO-YGrdk3aFukrNwrODB110HqdOsjMK6TDuUUiUEQT8YFOwspDfFd4pPt4wWiqfe'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ != "__quiz__":
    main()
    