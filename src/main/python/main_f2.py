from secure_all import AccessManager, AccessRequest, AccessKey
from pathlib import Path


def main():
    cwd = str(Path.cwd()) + "/../../../JsonFilesRequests/"
    my_file = cwd + "12345678Z.json"
    ak = AccessKey(dni="12345678Z", access_code="299350376deadf07044aaa5035f93a6f",
                   notification_emails=["100429094@alumnos.uc3m.es"], validity=3)
    ak.get_access_key(my_file)

    my_file = cwd + "11111111H.json"
    ak = AccessKey(dni="11111111H", access_code="d382a416259e01cbd63b75792036025d",
                   notification_emails=["100429094@alumnos.uc3m.es"], validity=3)
    ak.get_access_key(my_file)

    return


    am = AccessManager()
    am.get_access_key(my_file)
    am.check_key(ak.key)

    am2 = AccessManager()
    am2.request_access_code(id_document="11111111H", full_name="Beatriz Benitez",
                            access_type="Guest", email_address="100429094@alumnos.uc3m.es", days=3)


if __name__ == "__main__":
    main()

