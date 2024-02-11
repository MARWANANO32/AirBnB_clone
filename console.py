#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
