from dolar_abstraction.consumer.get_dollar import GetDollar


def banner() -> None:
    banner_txt = """                                                                            
    ooo.          8 8              .oPYo.                                                 
    8  `8.        8 8              8    8                                                 
    8   `8 .oPYo. 8 8 .oPYo. oPYo. 8      .oPYo. odYo. .oPYo. o    o ooYoYo. .oPYo. oPYo. 
    8    8 8    8 8 8 .oooo8 8  `' 8      8    8 8' `8 Yb..   8    8 8' 8  8 8oooo8 8  `' 
    8   .P 8    8 8 8 8    8 8     8    8 8    8 8   8   'Yb. 8    8 8  8  8 8.     8     
    8ooo'  `YooP' 8 8 `YooP8 8     `YooP' `YooP' 8   8 `YooP' `YooP' 8  8  8 `Yooo' 8     
    .....:::.....:....:.....:..:::::.....::.....:..::..:.....::.....:..:..:..:.....:..::::
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    """
    print(banner_txt)


def interact_user() -> None:
    get_dollar = GetDollar()
    while True:
        year = input("[<<] Write the year for get dollar\n[>>]")
        get_dollar.year = year
        month = input("[<<] Write the month for get dollar\n[>>]")
        get_dollar.month = month
        day = input("[<<] Write the day for get dollar\n[>>]")
        get_dollar.day = day
        value = get_dollar()
        print(f" [ Value: {value} ]")
        again = input("[<<] try again? [yes] | [not]\n[>>]")
        if again == "yes":
            print("Let's the next value")
        elif again == "not":
            print("By by!")
            break
        else:
            print(f"Value {again} not found!")
            break



