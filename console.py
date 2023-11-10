#!/usr/bin/python3
"""
console module

Implements the command interpreter for the AirBnB clone project.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class

    Implements the command interpreter for the AirBnB clone project.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a new line before exiting
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
