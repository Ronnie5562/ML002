#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""
import sys

file_size = 0
status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
iter = 0
try:
    for line in sys.stdin:
        iter += 1
        line_list = line.split()
        if len(line_list) >= 2:
            if line_list[-2] in status_code:
                status_code[line_list[-2]] += 1
            try:
                file_size += int(line_list[-1])
            except FileNotFoundError:
                pass

        if iter % 10 == 0:
            print(f"File size: {file_size:d}")
            for key, value in sorted(status_code.items()):
                if value:
                    print(f"{key}: {value:d}")

    print(f"File size: {file_size:d}")
    for key, value in sorted(status_code.items()):
        if value:
            print(f"{key}: {value:d}")

except KeyboardInterrupt:
    print(f"File size: {file_size:d}")
    for key, value in sorted(status_code.items()):
        if value:
            print(f"{key}: {value:d}")