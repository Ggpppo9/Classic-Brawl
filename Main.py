from Core.Networking.Server import Server


def main():

    print(r"""
    ____                      __   _____ __                 
   / __ )_________ __      __/ /  / ___// /_____ ___________
  / __  / ___/ __ `/ | /| / / /   \__ \/ __/ __ `/ ___/ ___/
 / /_/ / /  / /_/ /| |/ |/ / /   ___/ / /_/ /_/ / /  (__  ) 
/_____/_/   \__,_/ |__/|__/_/   /____/\__/\__,_/_/  /____/  
                                                            
    """)

    Server("0.0.0.0", 9339).start()pip install -r requirements.txtconfig.json


if __name__ == '__main__':
    main()
