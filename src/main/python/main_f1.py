from secure_all import AccessManager, AccessRequest, AccessKey
from pathlib import Path

def main():
    ar = AccessRequest(id_document="11111111H", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
    #ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

if __name__ == "__main__":
    main()
main()
