#!/usr/bin/python
"""
Author: Josh VanDeraa

Filters related to the Ansible Config testing Playbooks
"""
# pylint disable=R0911
import requests
import ipaddress


class FilterModule:
    """
    Defines a filter module object.
    """

    @staticmethod
    def filters():
        """
        Return a list of hashes where the key is the filter
        name exposed to playbooks and the value is the function.
        """
        return {
            "get_ciscoios_serial_list": FilterModule.get_ciscoios_serial_list,
            "compare_lists": FilterModule.compare_lists,
            "convert_mac_address": FilterModule.convert_mac_address,
            "get_role_from_hostname": FilterModule.get_role_from_hostname,
            "get_interface_type": FilterModule.get_interface_type,
            "get_interface_by_bandwidth": FilterModule.get_interface_by_bandwidth,
            "build_ipv4_from_facts": FilterModule.build_ipv4_from_facts,
            "get_interface_id": FilterModule.get_interface_id,
            "get_primary_ip": FilterModule.get_primary_ip,
            "proxmox_vm_interface": FilterModule.proxmox_vm_interface,
            
            
        }

    @staticmethod
    def get_ciscoios_serial_list(ansible_facts):
        """
        Goal: Take information in Ansible Facts and return a list of serial numbers for the logical
        device. If it is a stack of switches with a single management, this should return multiple
        serial numbers. If it is a single unit then it should return the single serial number within
        a list.

        ansible_net_serialnum (string)         The serial number of the remote device

        ansible_net_stacked_serialnums (list)  when multiple devices are configured in a stack
                                                The serial numbers of each device in the stack

        """
        # Check if net_stacked_serialnums exists, then return it
        if ansible_facts.get("net_stacked_serialnums") is not None:
            return ansible_facts.get("net_stacked_serialnums")

        # Check that net_serialnum exists, returning the string back as a list of one
        if ansible_facts.get("net_serialnum") is not None:
            return [ansible_facts.get("net_serialnum")]

        return None

    @staticmethod
    def convert_mac_address(mac_address):
        """
        Goal: Return all MAC addresses sent in as a type of EAU-48 Address type
        Default: If None or 'None' is sent in as the Mac address, then all 0s are returned
        A method to verify that the MAC address is in a valid format for Netbox
        and returns a 00:00:00:00:00:00 if the MAC address is of type None

        EUI48      : AB:CD:EF:01:23:45
        "Cisco"    : abcd.ef01.2345
        "Microsoft": AB-CD-EF-01-23-45
        """
        if mac_address in ("None", None):
            mac_address = "0000.0000.0000"

        mac_address = mac_address.upper()
        mac_address = mac_address.replace(".", "")
        mac_address = mac_address.replace("-", "")
        mac_address = mac_address.replace(":", "")
        mac_address = ":".join(
            [mac_address[i : i + 2] for i, j in enumerate(mac_address) if not i % 2]
        )

        return mac_address

    @staticmethod
    def compare_lists(device_serial_numbers, netbox_serial_numbers):
        """
        A method to verify that the serial number(s) of a device/virtual chassis
        are in fact the same
        """
        device_serials_set = set(device_serial_numbers)
        netbox_serials_set = set(netbox_serial_numbers)

        return device_serials_set == netbox_serials_set

    @staticmethod
    def get_role_from_hostname(hostname):
        """
        Method to get a role from the hostname

        Args:
            hostname (string): String representation of the hostname
        """
        if "sw" in hostname:
            return "Switch"

        if "rtr" in hostname:
            return "Router"

        if "fw" in hostname:
            return "Firewall"

        if "nxos" in hostname:
            return "Switch"

        if "veos" in hostname:
            return "Switch"

        return None

    @staticmethod
    def get_interface_by_bandwidth(bandwidth_value):
        """
        Method to get the interface type based on the bandwidth value

        Args:
            bandwidth_value (int): Integer of the bandwith speed
        """
        if bandwidth_value == 8000000:
            return "Virtual"

        if bandwidth_value == 1000000:
            return "1000base-t"

        if bandwidth_value == 10000000:
            return "10gbase-t"

        return None

    @staticmethod
    def build_ipv4_from_facts(ansible_facts):
        def get_proxmox_vars():

            return
        
        def convert_mac_address(mac_address):
            if mac_address in ("None", None):
                mac_address = "0000.0000.0000"

            mac_address = mac_address.upper()
            mac_address = mac_address.replace(".", "")
            mac_address = mac_address.replace("-", "")
            mac_address = mac_address.replace(":", "")
            mac_address = ":".join(
                [mac_address[i : i + 2] for i, j in enumerate(mac_address) if not i % 2]
            )

            return mac_address
        
        return_list = []
        interface_list = ansible_facts.get("interfaces")

        for interface in interface_list:
            interface_facts = ansible_facts.get(interface)
            if interface_facts is not None:

                device_name = interface_facts.get("device")
                mtu         = interface_facts.get("mtu")
                mac_address  = interface_facts.get("macaddress")
                converted_mac = convert_mac_address(mac_address)
                ipv4         = interface_facts.get("ipv4")
                if ipv4 is not None:
                    ip_address = ipv4.get("address")
                    netmask = ipv4.get("netmask")
                    subnetmask = (ipaddress.IPv4Network((0,netmask))).prefixlen
                    cidr = f"{ip_address}/{subnetmask}"

                    untagged_vlan = 

                    return_list.append({"interface": device_name, "address": cidr, "mac_address": converted_mac, "mtu": mtu, untagged_vlan:[{name:'Mickey Mouse', site: "test"}]})

        return return_list

    @staticmethod
    def proxmox_vm_interface(ansible_facts):

        def convert_mac_address(mac_address):
            if mac_address in ("None", None):
                mac_address = "0000.0000.0000"

            mac_address = mac_address.upper()
            mac_address = mac_address.replace(".", "")
            mac_address = mac_address.replace("-", "")
            mac_address = mac_address.replace(":", "")
            mac_address = ":".join(
                [mac_address[i : i + 2] for i, j in enumerate(mac_address) if not i % 2]
            )

            return mac_address
        
        return_list = []
        interface_list = ansible_facts.get("interfaces")

        for interface in interface_list:
            interface_facts = ansible_facts.get(interface)
            if interface_facts is not None:

                device_name = interface_facts.get("device")
                mtu         = interface_facts.get("mtu")
                mac_address  = interface_facts.get("macaddress")
                converted_mac = convert_mac_address(mac_address)
                ipv4         = interface_facts.get("ipv4")
                if ipv4 is not None:
                    ip_address = ipv4.get("address")
                    netmask = ipv4.get("netmask")
                    subnetmask = (ipaddress.IPv4Network((0,netmask))).prefixlen
                    cidr = f"{ip_address}/{subnetmask}"
                    return_list.append({"interface": device_name, "address": cidr, "mac_address": converted_mac, "mtu": mtu})

        return return_list

    @staticmethod
    def get_primary_ip(ansible_facts):

        return_list = []
        interface_list = ansible_facts.get("default_ipv4")
        if interface_list is not None:
            interface = interface_list.get("interface")
            address = interface_list.get("address")
            prefix = interface_list.get("prefix")
            cidr = f"{address}/{prefix}"
            return_list.append({"interface": interface, "address": cidr})
        return return_list

    @staticmethod
    def get_interface_id(vm_name, netbox_headers):
        """
        Get an Interface ID from Netbox

        Args:
            vm_name (string): Name of the VM
        """
        url = (
            "http://65.21.252.14:8000/api/virtualization/interfaces/?virtual_machine=%s"
            % vm_name
        )
        result = requests.get(url, headers=netbox_headers)
        return result.json()["results"][0]["id"]

    @staticmethod
    def get_interface_type(interface_name):
        """
        Method to return the interface type (Physical, Virtual, speed) based on the name of the
        interface

        Args:
            interface_name (string): Interface Name
        """
        if "eth" in interface_name:
            return "1000base-t"

        if "Gigabit" in interface_name:
            return "1000base-t"

        if "Ethernet" in interface_name:
            return "1000base-t"

        if "switch0" in interface_name:
            return "Virtual"

        if "lo" in interface_name:
            return "Virtual"

        if "Loopback" in interface_name:
            return "Virtual"

        if "vlan" in interface_name.lower():
            return "Virtual"

        if "Port-channel" in interface_name:
            return "LAG"

        if "mgmt0" in interface_name:
            return "1000base-t"

        if "Management1" in interface_name:
            return "1000base-t"

        return None