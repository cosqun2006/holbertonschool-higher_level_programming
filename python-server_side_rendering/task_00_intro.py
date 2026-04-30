import os


def generate_invitations(template, attendees):
    # 1. Giriş Tiplərinin Yoxlanılması
    if not isinstance(template, str):
        print("Error: Invalid input type for template. Expected str.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Invalid input type for attendees. Expected list of dictionaries.")
        return

    # 2. Boş Girişlərin Yoxlanılması
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Prosesin İcrası
    for index, attendee in enumerate(attendees, start=1):
        try:
            invitation_content = template

            # Lazım olan bütün açarlar
            placeholders = ["name", "event_title", "event_date", "event_location"]

            for key in placeholders:
                # Dəyəri götürürük, yoxdursa və ya None-dırsa "N/A" yazırıq
                value = attendee.get(key)
                if value is None:
                    value = "N/A"

                # Placeholder-i əvəz edirik (Məsələn: {name})
                placeholder = "{" + key + "}"
                invitation_content = invitation_content.replace(placeholder, str(value))

            # 4. Faylın Yazılması (f-string yerinə .format() istifadə edirik)
            file_name = "output_{}.txt".format(index)

            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(invitation_content)

        except Exception as e:
            print("An error occurred: {}".format(e))
