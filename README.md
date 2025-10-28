## IE-Com As Shell

The following repository demonstrates the abstraction of the communication of `Windows COM Objects` with a remote attacker machine for performing an `HTTP Reverse Shell connection` in order to simulate a certain sorting scenario for Firewall rules.

Basically, not all traffic relies on a built-in server firewall, but a local firewall can limit what data can access the internet. The key point of this is to trick the firewall by using good and well-intended (white-list programs) software as middleware to infiltrate connections to the attacker's `C&C machine`.

## Why IE?

1. Comes in all Windows installations
2. It can be considered as a backup browser that nobody cares about updates, occasionally.
3. Works very well with COM Objects

## Background

Microsoft offers a "component object model" or `COM object`, which is software that enables inter-process communication. This `COM` interface creates an object (programmatically) to control and automate multiple related built-in software such as Excel, Outlook, IE and many others

## The plan

Use the `client.py` file to control the `IE Browser` to force a connection to Kali in the background for bypassing a possible firewall
policy. This file initiates an IE process in the background, then uses the `iexplore.exe` and transfers the data using GET/POST back and forth between machines


It is the same principle as a single `HTTP Reverse Shell`, but instead of using Python's `request`, it uses the `IE Browser requests` itself as a background program.

This is not limited to a shell; you can transfer files, and more related to the COMM protocol

## Lab

A virtualized Win7 32-bit Machine.

## Credits
[David Lares S](https://davidlares.com)

## License
[MIT](https://opensource.org/licenses/MIT)
