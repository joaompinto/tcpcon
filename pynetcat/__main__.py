from .args import CommandArgs

if __name__ == "__main__":
    cmd = CommandArgs()
    cmd.parse()
    cmd.validate()
    cmd.run()
