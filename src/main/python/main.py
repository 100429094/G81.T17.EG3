from secure_all import AccessManager, AccessRequest, AccessKey
from pathlib import Path

""""""
def main():
    cwd = str(Path.cwd()) + "/../../../JsonFilesRequests/"
    my_file = cwd + "12345678Z.json"
    ak = AccessKey(dni="12345678Z", access_code="a921b3947c32bfd5f6a3130eedfc802f",
                   notification_emails=["100429094@alumnos.uc3m.es"], validity=3)

    am = AccessManager()
    am.get_access_key(my_file)
    am.check_key(ak.key)

    am2 = AccessManager()
    am2.request_access_code(id_document="11111111H", full_name="Beatriz Benitez",
                            access_type="Guest", email_address="100429094@alumnos.uc3m.es", days=3)

if __name__ == "__main__":
    main()

""""""