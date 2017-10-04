from __future__ import print_function

# 0.8, BLOATED.

"""SimpleEmail_SpamBot or SESB is a script that lets you spam people using Gmail, Outlook or/and iCloud"""

# TODO:
# Test SESB 0.8, because I haven't really tested it yet.

__author__ = "DizAzTor"
__license__ = "MIT"
__version__ = "v0.8"
services = {"gmail.com": "smtp.gmail.com:587", "outlook.com": "smtp-mail.outlook.com:587", "icloud.com": "smtp.mail.me.com:587", "yahoo.com": "smtp.mail.yahoo.com:587", "zoho.com": "smtp.zoho.eu:587", "gmx.com": "smtp.gmx.com:25", "fastmail.com": "mail.messagingengine.com:587"}

try:
    import sys
    if sys.version_info[:2] <= (2, 7):
        import ConfigParser
        from urllib import urlopen
    elif sys.version_info[:2] <= (3, 6):
        import configparser as ConfigParser
        from urllib.request import urlopen
    import smtplib
    import getpass
    import time
    import os
    import random

except ImportError as err:
    print("{}".format(err))
    sys.exit(0)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class CheckFor(object):

    def internet(self):
        try:
            print("\rChecking for internet connection...")
            google = urlopen("https://www.google.com")
        except:
            print("\rInternet connection is required to run SESB.")
            sys.exit(0)

    def latestver(self):
        try:
            versionx = urlopen("https://raw.githubusercontent.com/DizAzTor/SimpleEmail_SpamBot/master/version.txt")
            version = versionx.read().rstrip()
            version = version.decode("utf-8")
            if version != __version__:
                print("\rThere is an update available. Please download it.")
                print("\rNewest version is: {}".format(version))
            else:
                print("\rLatest update installed.")
        except ValueError:
            print("\rERROR while getting updates.")

class QuickMode(object):
    def __init__(self):
        self.account = None
        self.password = None
        self.delay = None
        self.subject = None
        self.message = None
        self.service = None
        self.cservice = None
        self.targets = []
        self.start = None

    def core(self):
        try:
            config = ConfigParser.RawConfigParser()
            path = "config.cfg"
            config.read(path)
            self.account = config.get("account", "account")
            self.password = config.get("account", "password")
            self.cservice = config.get("spamfo", "cservice")
            self.delay = config.get("spamfo", "delay")
            self.delay = int(self.delay)
            self.subject = config.get("spamfo", "subject")
            self.message = config.get("spamfo", "message")
            self.targets = config.get("targets", "targets")
            self.targets = self.targets.split(", ")


            at = self.account.find("@")
            at += 1
            self.service = self.account[at:]
            if self.cservice != "None":
                services[self.service] = self.cservice
            try:
                if self.service in services.keys():
                    server = smtplib.SMTP(services[self.service])
                    server.ehlo()
                    server.starttls()
                    server.login(self.account, self.password)
                    msg = "\r\n".join([
                        "From: {0}",
                        "To: {1}",
                        "Subject: {2}",
                        "",
                        "{3}"]).format(self.account, self.targets, self.subject, self.message)
                    counter = 0;
                    while(True):
                        server.sendmail(self.account, self.targets, msg)
                        counter += 1;
                        print("\rMail sent! {}".format(counter))
            except (KeyboardInterrupt, EOFError):
                print("\rGoodbye!")
                sys.exit(0)
            except:
                print("\rERROR: exiting.")
                sys.exit(0)

        except ValueError:
            print("\rERROR: couldn't cast an int to the delay variable. Must be an integer.")
            sys.exit(0)
        except (EOFError, KeyboardInterrupt):
            print("\rGoodbye!")
        except:
            print("\rERROR: error while importing the settings.")
            sys.exit(0)

class ManualMode(object):
    def __init__(self):
        self.account = None
        self.password = None
        self.delay = None
        self.subject = None
        self.message = None
        self.service = None
        self.cservice = None
        self.targets = []
        self.start = None

    def interface(self):
        print("""Supported emails are:
1. GMail\n2. Outlook\n3. iCloud\n4. Yahoo! 5. Mail\n6. Zoho Mail\n7. GMX\n8. Fastmail""")
        self.account = get_input("\r(1/6) Account: ")
        if self.account[1] == "{" and self.account[-1] == "}":
            a1 = self.account.find("{")
            a1 += 1
            a2 = self.account.find("}")
            self.service = self.account[a1:a2]
            print("\rOK, log in with your account now.")
            self.account = get_input(bcolors.OKBLUE + "\r(1/6) Account: " + bcolors.ENDC)
            ax = self.account.find("@")
            ax += 1
            services[self.account[ax:]] = self.service
        else:
            at = self.account.find("@")
            at += 1
            self.service = self.account[at:]
            if self.service in services.keys():
                pass
            else:
                self.service = None
                print("\rERROR: unsupported email service.")
                sys.exit(0)
        self.password = getpass.getpass("\r(2/6) Password: ")
        counter = 1;
        print("\rEvery line is a new target.")
        print("\rOnce you're done, press ENTER.")
        while True:
            a_new_target = get_input("\r(3/6) Target {}: ".format(counter))
            if a_new_target == "":
                break
            else:
                counter += 1;
                self.targets.append(a_new_target)

        self.delay = get_input("\r(4/6) Delay: ")
        try:
            self.delay = int(self.delay)
        except:
            print("\rNot an integer.")
            sys.exit(0)
        self.subject = get_input("\r(5/7) Subject: ")
        self.message = get_input("\r(6/6) Message: ")

        try:
            if self.service in services.keys():
                server = smtplib.SMTP(services[self.service])
                server.ehlo()
                server.starttls()
                server.login(self.account, self.password)
                msg = "\r\n".join([
                    "From: {0}",
                    "To: {1}",
                    "Subject: {2}",
                    "",
                    "{3}"]).format(self.account, self.targets, self.subject, self.message)
                counter = 0;
                while(True):
                    server.sendmail(self.account, self.targets, msg)
                    counter += 1;
                    print("\rMail sent! {}".format(counter))
        except (KeyboardInterrupt, EOFError):
            print("\rGoodbye!")
            sys.exit(0)
        except:
            print("\rERROR: exiting.")
            sys.exit(0)

class CommandMode(object):

    def __init__(self):
        self.account = None
        self.password = None
        self.delay = 0
        self.subject = None
        self.message = None
        self.service = None
        self.cservice = None
        self.targets = []
        self.start = None

    def interface(self):
        try:
            command = get_input(bcolors.OKBLUE + "\r>>> "+ bcolors.ENDC).lower()
            co = command.split()
        except KeyboardInterrupt:
            print("\rNo service to stop.")
            self.interface()

        except EOFError:
            print("\rGoodbye!\r")
            sys.exit(0)

        if "add" in command:
            if len(co) == 3:
                if co[0] == "add":
                    if co[1] == "account":
                        self.account = co[2]
                        at = self.account.find("@")
                        at += 1
                        self.service = self.account[at:]
                        print("\rAdded an account.")
                    elif co[1] == "delay":
                        try:
                            self.delay = int(co[2])
                        except ValueError:
                            print("\rERROR: must be an integer.")

            elif len(co) == 2:
                if co[0] == "add":
                    if co[1] == "password":
                        self.password = getpass.getpass(bcolors.OKBLUE + "\r>>> " + bcolors.ENDC)
                        print("\rAdded a password.")
                    elif co[1] == "targets":
                        counter = 0
                        while(True):
                            new_target = get_input("\rNew target: ")
                            if new_target == "":
                                print("\r{} target(s) added.".format(counter))
                                break
                            else:
                                self.targets.append(str(new_target))
                                counter += 1

            elif len(co) == 4:
                if co[0] == "add":
                    if co[1] == "delay":
                        try:
                            if co[2] == "-m":
                                self.delay = int(co[3]) * 60
                            elif co[2] == "-h":
                                self.delay = int(co[3]) * 3600
                            elif co[2] == "-d":
                                self.delay = int(co[3]) * 86400
                            print("\rDelay set to {} seconds.".format(self.delay))
                        except ValueError:
                            print("\rERROR: must be an integer.")
                    print("\rERROR: add: delay: unknown argument(s).")
            else:
                print("\rERROR: add: unknown argument(s).")

        elif "del" in command:
            if len(co) == 2 and co[0] == "del":
                if co[1] == "account":
                    self.account = None
                elif co[1] == "password":
                    self.password = None
                elif co[1] == "message":
                    self.message = None
                elif co[1] == "subject":
                    self.subject = None
                elif co[1] == "delay":
                    self.delay = 0
                elif co[1] == "passacc":
                    self.account = None
                    self.password = None
                elif co[1] == "submsg":
                    self.message = None
                    self.subject = None
                elif co[1] == "all":
                    self.account = None
                    self.password = None
                    self.delay = 0
                    self.subject = None
                    self.message = None
                    self.service = None
                    self.cservice = None
                    self.targets = []
                    self.start = None
                else:
                    print("\rERROR: del: unknown argument(s).")
            else:
                print("\rERROR: del: unknown argument(s).")

        elif "help" in command:
            pass

        elif command == "clear":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print("\rCommand Mode v0.4")


        elif "print" in command:
            if len(co) == 2 and co[0] == "print":
                if co[1] == "account":
                    print("\rAccount: {} | Detected service: {}".format(self.account, self.service))
                elif co[1] == "password":
                    print("\rPassword: {}".format(self.password))
                elif co[1] == "targets":
                    print("\rTarget(s): {} | Number of targets: {}".format(", ".join(self.targets), len(self.targets)))
                elif co[1] == "message":
                    print("\rMessage: {}".format(self.message))
                elif co[1] == "subject":
                    print("\rSubject: {}".format(self.subject))
                elif co[1] == "delay":
                    print("\rDelay: {}".format(self.delay))
                else:
                    print("\rERROR: print: unknown argument(s).")

            elif len(co) == 3 and co[0] == "print":
                if co[1] == "targets":
                    try:
                        target_number = int(co[2])
                        target_number -= 1
                        print("\rTarget {0}: {1}".format(target_number, self.targets[target_number]))
                    except ValueError:
                        print("\rERROR: Must be an integer.")
                    except IndexError:
                        print("\rTarget not found.")
                else:
                    print("\rERROR: print: unknown argument(s).")

        elif command == "commands":
            print(bcolors.OKGREEN + "   add [option]" + bcolors.ENDC, "= Add an account.")
            print(bcolors.OKGREEN + "   del [option]" + bcolors.ENDC, "= Remove your password.")
            print(bcolors.OKGREEN + "   ver [option]" + bcolors.ENDC, "= Either the latest version or the current one.")
            print(bcolors.OKGREEN + "   print [option]" + bcolors.ENDC, "= Print something to the terminal.")
            print(bcolors.OKGREEN + "   start" + bcolors.ENDC, "= Start spamming.")
            print(bcolors.OKGREEN + "   CTRL+D | CTRL+C" + bcolors.ENDC, "= Stop the current process.")
            print(bcolors.OKGREEN + "   CTRL+D | exit | quit" + bcolors.ENDC, "= Quit SESB.")
            print(bcolors.OKGREEN + "   clear" + bcolors.ENDC, "= Clear the terminal.")
            print(bcolors.OKGREEN + "   send email" + bcolors.ENDC, "= Send a normal email to all targets.")
            print(bcolors.OKGREEN + "   import" + bcolors.ENDC, "= Import settings from config.cfg")
            print(bcolors.OKGREEN + "   write" + bcolors.ENDC, "= Write your current settings to config.cfg")
            print(bcolors.OKGREEN + "   t2l" + bcolors.ENDC, "= Check if your email or password is working.")
            print(bcolors.OKGREEN + "   manual" + bcolors.ENDC, "= Enter manual mode.")
            print(bcolors.OKGREEN + "   random" + bcolors.ENDC, "= Enter random mode.")

        elif "start" in command:
            if len(co) == 1 and co[0] == "start":
                if self.account is not None and self.subject is not None and self.message is not None and self.service is not None and len(self.targets) != 0:
                    try:
                        if self.service in services.keys():
                            server = smtplib.SMTP(services[self.service])
                            server.ehlo()
                            server.starttls()
                            server.login(self.account, self.password)
                            msg = "\r\n".join([
                                "From: {0}",
                                "To: {1}",
                                "Subject: {2}",
                                "",
                                "{3}"]).format(self.account, self.targets, self.subject, self.message)
                            self.start = True
                            while(self.start is True):
                                server.sendmail(self.account, self.targets, msg)
                    except smtplib.SMTPAuthenticationError:
                        print("\rERROR: email or password is not correct.")
                    except:
                        print("\rERROR: error while trying to spam.")
                else:
                    print("\rERROR: missing something.")
            else:
                print("\rERROR: start: unknown argument(s).")

        elif "import" in command:
            if len(co) == 1 and co[0] == "import":
                try:
                    config = ConfigParser.RawConfigParser()
                    path = "config.cfg"
                    config.read(path)
                    self.account = config.get("account", "account")
                    self.password = config.get("account", "password")
                    self.delay = config.get("spamfo", "delay")
                    self.delay = int(self.delay)
                    self.subject = config.get("spamfo", "subject")
                    self.message = config.get("spamfo", "message")
                    self.targets = config.get("targets", "targets")
                    self.targets = self.targets.split(", ")

                except ValueError:
                    print("\rERROR: couldn't cast an int to the delay variable. Must be an integer.")
                except:
                    print("\rERROR: error while importing the settings.")
            else:
                print("\rERROR: import: unknown argument(s).")
        elif "t2l" in command:
            if len(co) == 1 and co[0] == "t2l":
                if self.account is not None and self.password is not None and self.service is not None:
                    try:
                        server = smtplib.SMTP(services[self.service])
                        server.login(self.account, self.password)
                        print("\rSuccess.")
                    except smtplib.SMTPAuthenticationError:
                        print("\rERROR: email or password is not correct.")
                print("\rERROR: please make sure you add an account and a password.")
            else:
                print("\rERROR: t2l: unknown argument(s).")

        elif "write" in command:
            if len(co) == 1 and co[0] == "write":
                try:
                    config = ConfigParser.RawConfigParser()
                    config.add_section("account")
                    config.set("account", "account", self.account)
                    config.set("account", "password", self.password)
                    config.add_section("spamfo")
                    config.set("spamfo", "delay", self.delay)
                    config.set("spamfo", "subject", self.subject)
                    config.set("spamfo", "message", self.message)

                    config.add_section("targets")
                    config.set("targets", "targets", self.targets)
                    with open("config.cfg", "wb") as cfgfile:
                        config.write(cfgfile)
                        cfgfile.close()
                        print("\rSuccess")
                except ValueError:
                    print("\rERROR: error while writing to file.")
        
        elif "man" in command:
            if len(co) == 2 and co[0] == "man":
                self.cservice = co[1]
                if self.service is None:
                    services["unknown"] = self.cservice
                else:
                    services[self.service] = self.cservice

        elif "ver" in command:
            checkfor = CheckFor()
            if len(co) == 2 and co[0] == "ver":
                if co[1] == "-l" or co[1] == "--latest":
                    checkfor.latestver()
                elif co[1] == "-c" or co[1] == "--current":
                    print(__version__)
                else:
                    print("\rERROR: ver: unknown argument(s).")
            else:
                print("\rERROR: ver: unknown argument(s).")
        elif command == "quit" or command == "exit":
            print("\rGoodbye!")
            sys.exit(0)
        else:
            print("SESB: {}: command not found.".format(str(co[0])))

        self.interface()

if __name__ == "__main__":
    if sys.version_info[:2] <= (3, 6):
        get_input = input
    elif sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    checkfor = CheckFor()
    checkfor.internet()
    checkfor.latestver()

    if len(sys.argv) == 2 and sys.argv[1] == "-c":
        commandmode = CommandMode()
        commandmode.interface()
    elif len(sys.argv) == 2 and sys.argv[1] == "-m":
        manualmode = ManualMode()
        manualmode.interface()
    else:
        quickmode = QuickMode()
        quickmode.core()