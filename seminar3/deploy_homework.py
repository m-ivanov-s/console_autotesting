from ssh_chekers import ssh_checkout, upload_files
import yaml


with open('config2.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)

def deploy():
    res = []
    upload_files(data.get("ip"), data.get("user2"), data.get("password"), data.get("local_path"), data.get("remote_path"))
    res.append(ssh_checkout(data.get("ip"), data.get("user2"), data.get("password"), f"echo {data.get('password')} | sudo -S dpkg -i {data.get('remote_path')}", "Настраивается пакет"))
    res.append(ssh_checkout(data.get("ip"), data.get("user2"), data.get("password"), f"echo {data.get('password')} | sudo -S dpkg -s p7zip-full", "Status: install ok installed"))
    return all(res)

if deploy():
    print("Деплой успешен")
else:
    print("Ошибка деплоя")

