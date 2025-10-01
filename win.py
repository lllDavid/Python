import winreg
import os

def get_installed():
    programs = []
    reg_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]
    
    for reg_hive in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
        for reg_path in reg_paths:
            try:
                with winreg.OpenKey(reg_hive, reg_path) as key:
                    for i in range(0, winreg.QueryInfoKey(key)[0]):
                        try:
                            subkey_name = winreg.EnumKey(key, i)
                            with winreg.OpenKey(key, subkey_name) as subkey:
                                name, _ = winreg.QueryValueEx(subkey, "DisplayName")
                                programs.append(name.strip())
                        except FileNotFoundError:
                            continue
                        except OSError:
                            continue
            except FileNotFoundError:
                continue
    return programs

if __name__ == "__main__":
    programs = get_installed()
    output_file = os.path.join(os.getcwd(), "win_installed_programs.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        for program in programs:
            f.write(program + "\n")