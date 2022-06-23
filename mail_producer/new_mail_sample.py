import base64
import os
import json
import zlib  # https://en.wikipedia.org/wiki/Zlib
from time import time_ns


def json_to_b64(data_json: dict) -> bytes:
    data_bytes = bytes(json.dumps(data_json, separators=(',', ':')), "utf-8")
    compressed = zlib.compress(data_bytes, level=9)  # Gzip
    return base64.b64encode(compressed)


def b64_to_json(data_b64: bytes) -> dict:
    compressed = base64.b64decode(data_b64)
    data_bytes = zlib.decompress(compressed)  # Gzip
    return json.loads(data_bytes)


def generate_file_name(header: dict) -> str:

    header_bytes = bytes(json.dumps(header, separators=(',', ':')), "utf-8")

    # E-mail ID
    eid = hex(zlib.crc32(header_bytes))[2:]

    # Timestamp to prevent duplications and to order by
    ts = time_ns()

    # Random value to farther insure no duplications
    # uid = str(base64.b64encode(os.urandom(2)), "utf-8")

    euid = header.get("uid")

    return f"{eid}.{ts}.{euid}.json"


def assign_uid(entry: dict) -> dict:
    # TODO: Use inner timestamp and a random value to generate the UID
    pass


def main():
    mail_entry = {

        # Unique ID of the entry
        "uid": None,

        "ts": 0,  # TODO: Call timestamp function here

        # E-mail addresses to notify in case of error
        "notify_error": ["Developers <dev-team@somemail.com>"],

        # Header from which a unique E-mail ID is constructed
        "header": {

            # Name of the external system that produced this entry
            "system": "MyExternalSystem",

            # Name of the subsystem that produced this entry
            "subsystem": "[ID:12345] Trigger: Server Disk Out-of-Space",

            # E-mail header
            "from": "Mail System <some@email.com>",
            "to": ["Some One <someone@somemail.com>"],
            "cc": [],
            "bcc": [],
            "reply_to": [],
            "subject": "Warning: Your server's disk is out-of-space",
            "template": "ops_department",  # Name of the Template.
            "alternative_content": "Unable to render HTML. Please refer to the Ops department for details.",
            "attachments": []

        },

        # Template variables
        "data": {
            "hello": "world",
            "some_values": [1, 2, 3, 4],
            "table": {
                "Hostname": "MailServer01",
                "IP Address": "192.168.0.1",
                "Disk Capacity Percentage": 95
            }
        }
    }

    b64 = json_to_b64(mail_entry)
    restored_entry = b64_to_json(b64)

    # noinspection Assert
    assert mail_entry == restored_entry

    filename = generate_file_name(restored_entry.get('header'))

    with open(filename, 'w', encoding='utf-8') as fs:
        json.dump(restored_entry, fs, indent=4)


if __name__ == '__main__':
    main()
