'''Copyright 2018 KNet Solutions, India, http://knetsolutions.in

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

from mCli.commands.base import Command
from KNet.lib.topology import Topology
import sys
import yaml
import traceback

# Topology object
t = Topology()


class Exit(Command):
    description = "Exit"
    details = '''
    Exit from the shell
    Args: None
    return: result
    Example:  Exit
    '''

    def __call__(self, args):
        sys.exit()


class CreateTopology(Command):
    description = "Create Topology in SDN Test Bed"
    details = '''
    Create a Test Topology in SDN Test bed
    Args: Topology filename in absolute path(yaml)
    Example:   CreateTopology  /home/ubuntu/topology1.yaml
    '''

    def __validate(self, args):
        if args and args[0]:
            return True
        else:
            return False

    def __call__(self, args):
        if not self.__validate(args):
            err = "Error : Topology File not given \n ********* Help **********\n"+CreateTopology.details
            return err

        try:
            with open(args[0]) as fp:
                tdata = yaml.load(fp)
        except Exception as e:
            print e.__doc__
            return e.message

        try:
            result = t.create(tdata)
        except Exception as e:
            print e.__doc__
            return e.message
        return result


class DeleteTopology(Command):
    description = "Delete the Topology in SDN Test Bed"
    details = '''
    Delete a Test Topology in SDN Test bed
    Args: None
    return: result
    Example:   DeleteTopology
    '''

    def __call__(self, args):
        try:
            result = t.delete()
        except Exception as e:
            print e.__doc__
            return e.message
        return result


class GetTopology(Command):
    description = "Get the Topology objects in Detail"
    details = '''
    Get the Topology Objects(Nodes, Switchs, Links, QoS)
    Args: None
    return: result
    Example:   GetTopology
    '''

    def __call__(self, args):
        try:
            result = t.get()
        except Exception as e:
            print e.__doc__
            return e.message
        return result


class DeleteNode(Command):
    description = "Delete the Node in the Topology"
    details = '''
    Delete a Node in the Topology
    Args: node name
    return: result
    Example:   DeleteNode a1
    '''

    def __call__(self, args):
        try:
            result = t.deleteNode(args[0])
        except Exception as e:
            print e.__doc__
            return e.message
        return result


class DeleteSwitch(Command):
    description = "Delete the Switch in the Topology"
    details = '''
    Delete a Switch in the Topology
    Args: switch name
    return: result
    Example:   DeleteSwitch switch1
    '''

    def __call__(self, args):
        try:
            result = t.deleteSwitch(args[0])
        except Exception as e:
            print e.__doc__
            return e.message
        return result


class AdminDownLink(Command):
    description = "Admin down the Link"
    details = '''
    Admin shut down the link
    Args: interface name
    return: result
    Example:   AdminDownLink 6d025ab95ff04_l
    '''

    def __call__(self, args):
        try:
            result = t.adminDownLink(args[0])
        except Exception as e:
            print e.__doc__
            return e.message
        return result


class AdminUpLink(Command):
    description = "Admin up the Link"
    details = '''
    Admin up the link
    Args: interface name
    return: result
    Example:   AdminUpLink 6d025ab95ff04_l
    '''

    def __call__(self, args):
        try:
            result = t.adminUpLink(args[0])
        except Exception as e:
            print e.__doc__
            return e.message
        return result


class PingAll(Command):
    description = "Ping All nodes with each other"
    details = '''
    Initiate the 20 Ping  Packets between the nodes.
    Args: None
    return: result
    Example:   PingAll
    '''

    def __call__(self, args):
        try:
            result = t.pingAll()
        except Exception as e:
            print e.__doc__
            return e.message
        return result


class Ping(Command):
    description = "Ping the soruce node to destination node"
    details = '''
    Initiate the 20 Ping  Packets between the source node to destination node.
    Args: Source   Destination
    return: result
    Example:   Ping  a1  a2
    '''

    def __validate(self, args):
        if args and args[0] and args[1]:
            return True
        else:
            return False

    def __call__(self, args):
        if not self.__validate(args):
            err = "Error : Input args \n ********* Help **********\n"+Ping.details
            return err
        try:
            result = t.ping(args[0], args[1])
        except Exception as e:
            print e.__doc__
            return e.message
        return result
