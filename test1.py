from ssh_chekers import ssh_checkout, upload_files
import yaml

with open('config2.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)


class TestPositive:
    def test_step1(self):
        res = []
        upload_files(
            data.get("ip"),
            data.get("user"),
            data.get("password"),
            data.get("local_path"),
            data.get("remote_path"))

        res.append(ssh_checkout(
            data.get("ip"),
            data.get("user"),
            data.get("password"),
            f"echo {data.get('password')} | sudo -S dpkg -i {data.get('remote_path')}",
            "Настраивается пакет"))

        res.append(ssh_checkout(
            data.get("ip"),
            data.get("user"),
            data.get("password")
            , f"echo {data.get('password')} | sudo -S dpkg -s p7zip-full",
            "Status: install ok installed"))
        assert all(res)

    def test_step2(self):
        res = []
        upload_files(
            data.get("ip"),
            data.get("user"),
            data.get("password"),
            data.get("local_path"),
            data.get("remote_path"))

        res.append(ssh_checkout(
            data.get("ip"),
            data.get("user"),
            data.get("password"),
            f"echo {data.get('password')} | sudo -S dpkg -r {data.get('remote_path')}",
            "Удаляется"))

        res.append(ssh_checkout(
            data.get("ip"),
            data.get("user"),
            data.get("password"),
            f"echo {data.get('password')} | sudo -S dpkg -s p7zip-full",
            "Status: deinstall ok"))
        assert all(res)
