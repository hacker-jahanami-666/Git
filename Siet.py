import builtwith

import whois

from colorama import init, Fore

init()

from random import choice, randint

print(Fore.RED+"   hacker jahanami 🖤🖤")

print(Fore.RED+''' 

░██████╗██╗████████╗███████╗         

██╔════╝██║╚══██╔══╝██╔════╝          

╚█████╗░██║░░░██║░░░█████╗░░          

░╚═══██╗██║░░░██║░░░██╔══╝░░         

██████╔╝██║░░░██║░░░███████╗                   

╚═════╝░╚═╝░░░╚═╝░░░╚══════╝       

██╗███╗░░██╗███████╗░█████╗░██████╗░███╗░░░███╗

██║████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░████║

██║██╔██╗██║█████╗░░██║░░██║██████╔╝██╔████╔██║

██║██║╚████║██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║

██║██║░╚███║██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║

╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝

                                              

         

                                            ,--,  ,.-.

               ,                   \,       '-,-,'-.' | ._

              /|           \    ,   |\         }  )/  / -,',

              [ ,          |\  /|   | |        /  \|  |/  ,

              | |       ,.  , , | |  _,...(   (      .',

              \  \  __ ,-   ,  , / |,'      Y     (   /_L\

                      \  \_\,,    , ,  /  |         )         _,/

                \  '    ,_ __,-,<._.<        /         /

                 ', >.,       ,., |_      |         /

                   \/  ,      ,  | /__,.-    _,   \

                          -,-..\  _  \    /  ,  / ._) _,-\       \

                               \_,,.) /\     /  / ) (-,,     ,    |

               , )  | \_\       '-  |  (               \

                       /  /``(   , --, ,' \   |<    ,            |

             /  /_,--\   <\  V /> , )<_/)  | \      _)

       ,-, ,      (_,\ \    |   /) / __/  /   ----

      (-, \           ) \ ('_.-._)/ /,    /

      | /            / \\ V   V, /     /

   ,--\(        ,     <_/\\     ||      /

  (   ,-     \/|         \-A.A-|     /

 ,>,_ )_,..(    )\          -,,_-  _--

(_ \|   _,/_  /  \_            ,--

 \(    <.,../     -.._   _,-                ''')

smg = print(f'\33[92m    Version 1.0.1')

siet = input(f'\033[94m    Enter siet targit ====>: ')

domain = whois.whois('https://'+siet)

res = builtwith.builtwith("https://"+siet)

for i in res:

		print(res[i])

for i in domain:

	print(domain[i])
