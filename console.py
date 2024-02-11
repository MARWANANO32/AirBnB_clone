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

    def Create(self, args):
        if args == "":
            print("** class name missing **")
        elif args not in HBNBCommand:
            print("** class doesn't exist **")

    def Show(self, args):
        a = 0
        arg = args.split()

        if args == "":
            print("** class name missing **")
        elif arg[0] not in HBNBCommand:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
