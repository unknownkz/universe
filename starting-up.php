<?php

    $starting = "\n\e\x1b[1;4;41m[ STARTING UP ]\e[0m";
    $copy = "\e\x1b[1;97mCopyright (C) 2022 Unknown <https://github.com/unknownkz/universe> \n";
    $copy1 = "All Rights Reserved\n";
    $copy2 = "Credits : @unknownkz (axel) \n";
    $copy3 = "This file is a part of < https://github.com/unknownkz/universe/ > \n";
    $copy4 = "Please read the GNU Affero General Public License in; \n";
    $copy5 = "< https://www.github.com/unknownkz/universe/main/LICENSE/ > \n\n\e[0m";
    $copy6 = "\e\x1b[1;93mRunning script... \n\n\e[0m";
    $copy7 = "\n\n\e\x1b[48;5;171m[ MAINTAINER ]\e[0m : \e[1;4;124m@unknownkz\e[0m \e[1;4;35m<unknownkz@outlook.co.id>\e[0m\n\n\e\x1b[38;5;195m";

    $clear = "\n\n";

    $shxa = "\e\x1b[38;5;154m";
    $str_ascii = "X18gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgfCAgXCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogX18gICAgX18gIF9fX19fX18gICBcJCQgX18gICAgIF9fICAgX19fX19fICAgIF9fX19fXyAgICBfX19fX19fICAgX19fX19fICAKfCAgXCAgfCAgXHwgICAgICAgXCB8ICBcfCAgXCAgIC8gIFwgLyAgICAgIFwgIC8gICAgICBcICAvICAgICAgIFwgLyAgICAgIFwgCnwgJCQgIHwgJCR8ICQkJCQkJCRcfCAkJCBcJCRcIC8gICQkfCAgJCQkJCQkXHwgICQkJCQkJFx8ICAkJCQkJCQkfCAgJCQkJCQkXAp8ICQkICB8ICQkfCAkJCAgfCAkJHwgJCQgIFwkJFwgICQkIHwgJCQgICAgJCR8ICQkICAgXCQkIFwkJCAgICBcIHwgJCQgICAgJCQKfCAkJF9fLyAkJHwgJCQgIHwgJCR8ICQkICAgXCQkICQkICB8ICQkJCQkJCQkfCAkJCAgICAgICBfXCQkJCQkJFx8ICQkJCQkJCQkCiBcJCQgICAgJCR8ICQkICB8ICQkfCAkJCAgICBcJCQkICAgIFwkJCAgICAgXHwgJCQgICAgICB8ICAgICAgICQkIFwkJCAgICAgXAogIFwkJCQkJCQgIFwkJCAgIFwkJCBcJCQgICAgIFwkICAgICAgXCQkJCQkJCQgXCQkICAgICAgIFwkJCQkJCQkICAgXCQkJCQkJCQ=";
    $shxb = "\e[0m";

    echo $starting;
    echo $clear;
    echo $copy;
    echo $copy1;
    echo $copy2;
    echo $copy3;
    echo $copy4;
    echo $copy5;
    echo $copy6;
    echo $shxa;
    echo base64_decode($str_ascii);
    echo $shxb;
    echo $copy7;
    /**
    * execute command.
    */
    $command2 = escapeshellcmd('python3 __main__.py');
    $output2 = shell_exec($command2);
    echo $output2;

?>
