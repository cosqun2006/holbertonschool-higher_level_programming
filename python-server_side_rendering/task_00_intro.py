#!/usr/bin/python3

import os

from debugpy._vendored.pydevd.pydevd_attach_to_process.winappdbg import event


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return
    if not isinstance(attendees, list):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries.")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for index, attendee in enumerate(attendees, start=1):
        try:
            invitation_content = template
            placeholders = ["name", "event_title", "event_date", "event_location"]

            for key in placeholders:
                value = attendee.get(key)
                if value is None:
                    value = "N/A"

                invitation_content = invitation_content.replace(f"{{{key}}}", str(value))

        file_name = f"output_{index}.txt"

        # Eyni adlı faylın olub-olmadığını yoxlamaq olar (opsional)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(invitation_content)

    except Exception as e:
    print(f"An error occurred while processing attendee {index}: {e}")


# --- Test üçün nümunə ---
if __name__ == "__main__":
    template_text = """Hello {name},

        You are invited to the {event_title} on {event_date} at {event_location}.

        We look forward to your presence.

        Best regards,
        Event Team"""

    test_attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20",
         "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_text, test_attendees)
