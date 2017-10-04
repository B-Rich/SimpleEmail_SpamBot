# v0.1 BETA:

* SimpleEmail_SpamBot

# v0.2 BETA:

* Added the delay feature.

# v0.3 BETA:

* just type in your username.

* Changed more stuff.

# v0.3.4 BETA:
* Changed some stuff

# v0.4 BETA:

+ New features should be easily added.

* Completely rewritten.

* Still in BETA.

* Added support for iCloud.

* Added support for Outlook.

* Added support to spam more than one target at the exact time.

* Added a command-line version. To run it, use `python SESB.py -c` (Still in beta)

# v0.4 BETA: (2)

* It's useless now. Moved to **OLD CODE**

# v0.5:

* More exception handling.

* Stuff.

# v0.5.5:

[removed]

# v0.6:

* All in one.

* More exception handling.

* Command Mode 0.2. :)

    * import = import settings from config.cfg.

    * about = about.

    * try2login = check if your email or password is working.

    * send email = send a normal email to all of your targets..

    + you can now use Command Mode without having to rerun it every time you want to spam again. Meaning: "KeyboardInterrupt" won't cause the script to stop running anymore.

# v0.7:

[R = REPLACED]

* Check for updates.

* Support for Yahoo! Mail. (haven't tested it yet)

* Support for Zoho Mail. (haven't tested it yet)

* Support for GMX. (haven't tested it yet)

* Support for Fastmail. (haven't tested it yet)

- Please use GMail to spam.

* Command Mode 0.3
    + more expection handling

    + Colored commands in "commands"

    + Added lots of new commands.

        * `del account`
            * Remove your account.

        * `del password`
            * Remove your password.

        * `del passacc`
            * Remove your account and your password.

        * `del subject`
            * Remove the subject.

        * `del message` 
            * Remove the message.

        * `del submsg`
            * Remove the subject and the message.

        * `add target x`
            * Automatically add x amount of targets.

        * `del target x`
            * Delete a specific target.

        * `del target all`
            * You never guessed it, this command deletes all of the targets.

        * `print targets`
            *{R} now gives you numbers for the targets. (example: del target 1 = delete target number 1)

        * `manual`
            * same as "-m".

        * `print target x`
            * Print a specific target.

        * `checkver`
            * Check this script's version.

        * `latestver`
            * Check the latest version.

        * `set delay x`
            * {R} Same thing, except you can do it now directly.

        * `CTRL+D` / `exit` / `exit()` / `quit` / `quit()` / `:q` / `:q!`
            * vim is life.

        * `write`
            * Write your current settings to config.cfg

        * `day x`
            * Convert days to seconds and automatically assign the value to "delay".

        * `hour x`
            * Convert hours to seconds and automatically assign the value to "delay".

        * `minute x`
            * Convert minutes to seconds and automatically assign the value to "delay".

        * `reset all`
            * Reset everything. Same as "-c"

    -. Not sure if i added any more commands. I might have added some commands but didn't list them in "commands"

# v0.8:

+1 - Seems like someone forked SESB. I don't know what they're going to do with it, but cool :3

0.8 is here. The compiled standalone version of SESB + GSESB is about **250mb**. Well, that's because it's standalone. Meaning, doesn't matter if you have **PyQt** installed or not.

* Python3 support (For SESB-cli).
    * Python3 is now officially supported and is recommended to use. (Because Python3.6.2 is awesome and 2.7 should die already :p.) **SESB.py** now works with Python3 and Python2.

* Completely rewritten.
    * I haven't tested it that much at all. I'll commit any changes when I see stupid issues.
    * Changed everything.
    * Fixed some stupid issues.
    * The new interfaces are still in beta, and I'd recommend using them over 0.7's interfaces.
    * From about **1400+** lines of shitty code, to **500+** lines of nice code.

* Extended `help`. 
    * You can pretty much use it to get help for everything in **SESB**.

* You can add your own domain now.
    
    * Command-Mode
        1. Type `man 123.456.789:xxxx` and it should be added.

    * Manual-Mode
        1. When typing an email, type `{123.456.789:xxxx}` (__with the port__). It should give you an option to type your email after that. 

    * Quick-Mode
        1. Since this mode uses `config.cfg`, you'd have to type your email there.

<!-- * Random Mode.

    * How to use it (Type `python3 SESB.py -h r` to see what's up):

        1. OK, first off, this mode requires a working `config.cfg`.

        2. Not sure if your `config.cfg` is working? Well, you can enter the **Command Mode** and type `import` (this will import the settings from `config.cfg`), then type `try2login`. Or you can just use `python3 SESB.py -x -c`.

        3. Create a file with a lot of messages in it. The messages should be sperated by a new line.

        4. Open up a terminal. Type `python3 SESB.py -r r filename.txt`

        5. Watch it doing its thing, I guess.

        Run `python3 SESB.py -h r` to see what you can do. You will get some information on using **Random Mode**.
        For an example, you can also use `python3 SESB.py -r rrm` -->
    
    * ~~Random Mode.~~
        * Sorry. Delayed until SESB 0.9

* Compiled SESB files. 
    * I'm not sure if the `SESB.exe` works, but `SESB` (linux executable) works. You don't need Python to run it. If you're using Linux, just type `./SESB` in the terminal, and if you're using Windows, run `SESB.exe`. The standalone build files (which are about **250mb** total because they're standalone.) are inside `SESB.build` and `SESB.dist`. Download them from `releases`. But the normal compiled files are inside the `compiled` folder.

* SESB is now split into two:
    1. _SESB-cli_
        * **SESB-cli**. SESB-cli is the same one you've been using. SESB-cli is the default SESB and you can access it with the same way. Type `./SESB --help cli`

    2. _SESB-gui_
        * **SESB-gui** is SESB, but with a graphical user interface. Using **PyQt5**. ~~To open up the GUI, type `./SESB -g` or `./SESB --gui`. For help, type `./SESB -h g`. Very experimental~~. I decided I'd __actually__ split it. It's in the **GUI** directory. Just run it. No arguments. There is a compiled version for it as well.

* Command-Mode 0.4:
    * Completely rewritten.
    * All the new commands/changed commands.
        * `add [option]`
            * You can use this command to add everything. `set` is removed. And whatever you wanna add, is actually an argument, not a command itself.
            * `add account your_email`
                * It's now used directly.
            * `add delay N`
                * Arguments:
                * `add delay -m N`
                    * Was: `minute N`
                * `add delay -h N`
                    * Was: `hour N`
                * `add delay -d N`
                    * Was: `day N`
            * `add password`
                * You cannot add a password directly, because I'd like to hide your password with `getpass`.
            * `add targets`
                * This command was changed completely. Before, to add **one** target, you would type `add target`, and then type your target. To add more than **one** target, you would type `add target N` (N being how many targets you wanna add), and then keep on typing your targets' email addresses. Now, to add a target, type `add targets` and keep on typing your targets' email addresses until you're done, then press **ENTER**.
            * `add subject`
                * Was: `set subject`.

            * `add message`
                * Was: `set message`
            
        * `del [option]`
            * You can use this command to delete whatever you want. Meaning, commands like `reset all` were removed. Example: `del all`

            * `del account`
            * `del password`
            * `del message`
            * `del subject`
            * `del delay`
            * `del passacc`
            * `del submsg`
            * `del all`
        * `print [option]`
            * IIRC, the `print` in 0.7 was `show` for some commands. Well, now it's `print` for everything. Requires an argument, not a command itself (for an example, `print something`.)
            * `print account`
            * `print password`
            * `print targets`
            * `print message`
            * `print subject`
            * `print delay`
            * `print cservice`
                * prints your detected settings for your custom email domain service.

        * `commands`
        * `start`
        * `import`
        * `write`
        * `t2l`
            * This command replaces `try2login`.
        * `man [option]`
            * This command will add your custom email service.
            * Usage:
                * `man xxx.xxx.xxx:zzz`
                * `zzz` is the port.
        ~~* `random`~~
            ~~* This command activates the new **RandomMode**, which requires a working `config.cfg`~~
        * `manual`
            * This command activates the new **ManualMode** interface. 
        * `ver [option]`
            * Replaces `latestver` and `checkver`
            * `ver -l` | `ver --latest`
                * Checks the latest version, I don't think you'd need it anyways. Since the script automatically checks for the latest version when trying to run it.
            * `ver -c` | `ver --current`
                * Checks the current **SESB** version.
            
        * `quit | exit`
            * Replaces `quit()`, `exit()`, `quit`, `exit`, `:q` and `:q!`.